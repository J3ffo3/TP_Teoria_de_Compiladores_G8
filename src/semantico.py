from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

import ast_voltio as A
from ast_voltio import BOOLEANO, DECIMAL, ENTERO, PORCENTAJE, TEXTO, Tipo
from errores import ErrorCompilacion

DESCRIPCION_ERRORES = {
    "SEM-01": "Identificador no declarado",
    "SEM-02": "Identificador redeclarado en el mismo ambito",
    "SEM-03": "Unidades de dominio incompatibles",
    "SEM-04": "Tipos incompatibles",
    "SEM-05": "Modificacion de una constante",
    "SEM-06": "Condicion no booleana",
    "SEM-07": "retornar fuera de una regla",
    "SEM-08": "Valor de retorno incompatible",
    "SEM-09": "Numero de argumentos incorrecto",
    "SEM-10": "Tipo de argumento incompatible",
    "SEM-11": "Regla que no retorna en todos los caminos",
    "SEM-12": "Porcentaje fuera de rango",
    "SEM-13": "Division entre cero",
}

# ----------------------------------------------------------------------------
# Tabla de Simbolos y Ambitos
# ----------------------------------------------------------------------------
@dataclass(eq=False)
class Simbolo:
    nombre: str
    categoria: str                 # variable, constante, parametro, regla, contador
    tipo: Optional[Tipo]
    linea: int
    columna: int
    parametros: list = field(default_factory=list)
    ambito: str = ""

@dataclass
class Ambito:
    nombre: str
    padre: Optional["Ambito"]
    simbolos: dict = field(default_factory=dict)

    def buscar_local(self, nombre: str) -> Optional[Simbolo]:
        return self.simbolos.get(nombre)

    def buscar(self, nombre: str) -> Optional[Simbolo]:
        curr = self
        while curr is not None:
            if nombre in curr.simbolos:
                return curr.simbolos[nombre]
            curr = curr.padre
        return None

class TablaSimbolos:
    def __init__(self):
        self.global_ = Ambito("global", None)
        self.actual = self.global_
        self.todos: list[Ambito] = [self.global_]

    def abrir(self, nombre: str) -> None:
        self.actual = Ambito(nombre, self.actual)
        self.todos.append(self.actual)

    def cerrar(self) -> None:
        self.actual = self.actual.padre

# ----------------------------------------------------------------------------
# Analizador Semantico
# ----------------------------------------------------------------------------
class AnalizadorSemantico:
    def __init__(self):
        self.tabla = TablaSimbolos()
        self.errores: list[ErrorCompilacion] = []
        self.regla_actual: Optional[A.Regla] = None

    def _error(self, codigo: str, nodo, mensaje: str) -> None:
        self.errores.append(ErrorCompilacion("SEM", codigo, nodo.linea, nodo.columna, mensaje))

    def _declarar(self, simbolo: Simbolo, nodo) -> Optional[Simbolo]:
        previo = self.tabla.actual.buscar_local(simbolo.nombre)
        if previo is not None:
            self._error("SEM-02", nodo, f"'{simbolo.nombre}' ya fue declarado en este ambito (linea {previo.linea}).")
            return None
        simbolo.ambito = self.tabla.actual.nombre
        self.tabla.actual.simbolos[simbolo.nombre] = simbolo
        return simbolo

    @staticmethod
    def compatible(destino: Optional[Tipo], origen: Optional[Tipo]) -> bool:
        if destino is None or origen is None or destino == origen:
            return True
        return destino == DECIMAL and origen == ENTERO

    def _verificar_asignable(self, destino: Optional[Tipo], origen: Optional[Tipo], nodo, que: str) -> None:
        if self.compatible(destino, origen):
            return
        if destino and origen and destino.es_dominio and origen.es_dominio and destino != origen:
            self._error("SEM-03", nodo, f"Unidades incompatibles: no se puede asignar {origen} a {que} de tipo {destino}.")
            return
        self._error("SEM-04", nodo, f"Tipos incompatibles: no se puede asignar {origen} a {que} de tipo {destino}.")

    def analizar(self, programa: A.Programa) -> None:
        # Pasada 1: Registrar reglas globales para permitir llamadas antes de definicion
        for s in programa.sentencias:
            if isinstance(s, A.Regla):
                self._registrar_regla(s)
        # Pasada 2: Analisis de sentencias
        self._sentencias(programa.sentencias)
        self.errores.sort(key=lambda e: (e.linea, e.columna))

    def _sentencias(self, lista) -> None:
        for s in lista:
            metodo = getattr(self, "_s_" + type(s).__name__, None)
            if metodo:
                metodo(s)

    def _bloque_nuevo_ambito(self, bloque: A.Bloque, nombre: str) -> None:
        self.tabla.abrir(nombre)
        self._sentencias(bloque.sentencias)
        self.tabla.cerrar()

    def _s_Bloque(self, b: A.Bloque) -> None:
        self._bloque_nuevo_ambito(b, f"bloque (linea {b.linea})")

    # 1. Declaraciones
    def _s_Declaracion(self, d: A.Declaracion) -> None:
        if d.valor is not None:
            t_val = self._expr(d.valor)
            self._verificar_asignable(d.tipo_decl, t_val, d.valor, f"'{d.nombre}'")
        categoria = "constante" if d.constante else "variable"
        d.simbolo = self._declarar(Simbolo(d.nombre, categoria, d.tipo_decl, d.linea, d.columna), d)

    # 2. Asignacion
    def _s_Asignacion(self, a: A.Asignacion) -> None:
        tipo_valor = self._expr(a.valor)
        sim = self.tabla.actual.buscar(a.nombre)
        if sim is None:
            self._error("SEM-01", a, f"'{a.nombre}' no ha sido declarado.")
            return
        a.simbolo = sim
        if sim.categoria == "constante":
            self._error("SEM-05", a, f"No se puede modificar la constante '{a.nombre}'.")
            return
        if sim.categoria == "regla":
            self._error("SEM-04", a, f"'{a.nombre}' es una regla y no puede recibir asignacion.")
            return
        if a.op in ("+=", "-="):
            tipo_valor = self._tipo_binario(a.op[0], sim.tipo, tipo_valor, a.valor)
        self._verificar_asignable(sim.tipo, tipo_valor, a.valor, f"'{a.nombre}'")

    # 4. Selectivas
    def _condicion(self, expr: A.Expr, donde: str) -> None:
        t = self._expr(expr)
        if t is not None and t != BOOLEANO:
            self._error("SEM-06", expr, f"La condicion de '{donde}' debe ser booleana; se recibio {t}.")

    def _s_Si(self, s: A.Si) -> None:
        for i, (cond, bloque) in enumerate(s.ramas):
            self._condicion(cond, "si" if i == 0 else "sino si")
            self._s_Bloque(bloque)
        if s.sino is not None:
            self._s_Bloque(s.sino)

    # 5. Iterativas
    def _s_Mientras(self, m: A.Mientras) -> None:
        self._condicion(m.condicion, "mientras")
        self._s_Bloque(m.cuerpo)

    def _s_Para(self, p: A.Para) -> None:
        for nombre, expr in (("desde", p.desde), ("hasta", p.hasta), ("paso", p.paso)):
            if expr is None:
                continue
            t = self._expr(expr)
            if t is not None and t != ENTERO:
                self._error("SEM-04", expr, f"Tipos incompatibles: el limite '{nombre}' de 'para' debe ser entero, se recibio {t}.")
        self.tabla.abrir(f"para {p.variable} (linea {p.linea})")
        p.simbolo = self._declarar(Simbolo(p.variable, "contador", ENTERO, p.linea, p.columna), p)
        self._sentencias(p.cuerpo.sentencias)
        self.tabla.cerrar()

    # 6. Reglas
    def _registrar_regla(self, r: A.Regla) -> None:
        sim = Simbolo(r.nombre, "regla", r.tipo_retorno, r.linea, r.columna, [p.tipo_decl for p in r.parametros])
        r.simbolo = self._declarar(sim, r)
        r.registrada = True

    def _s_Regla(self, r: A.Regla) -> None:
        if not getattr(r, "registrada", False):
            self._registrar_regla(r)
        anterior, self.regla_actual = self.regla_actual, r
        self.tabla.abrir(f"regla {r.nombre}")
        for p in r.parametros:
            p.simbolo = self._declarar(Simbolo(p.nombre, "parametro", p.tipo_decl, p.linea, p.columna), p)
        self._sentencias(r.cuerpo.sentencias)
        self.tabla.cerrar()
        if r.tipo_retorno is not None and not self._retorna_siempre(r.cuerpo.sentencias):
            self._error("SEM-11", r, f"La regla '{r.nombre}' declara tipo {r.tipo_retorno} pero no retorna un valor en todos los caminos.")
        self.regla_actual = anterior

    def _retorna_siempre(self, sentencias) -> bool:
        for s in sentencias:
            if isinstance(s, A.Retornar):
                return True
            if isinstance(s, A.Bloque) and self._retorna_siempre(s.sentencias):
                return True
            if isinstance(s, A.Si) and s.sino is not None:
                ramas = [b for _, b in s.ramas] + [s.sino]
                if all(self._retorna_siempre(b.sentencias) for b in ramas):
                    return True
        return False

    def _s_Retornar(self, r: A.Retornar) -> None:
        tipo_valor = self._expr(r.valor) if r.valor is not None else None
        regla = self.regla_actual
        if regla is None:
            self._error("SEM-07", r, "'retornar' solo puede usarse dentro de una regla.")
            return
        esperado = regla.tipo_retorno
        if esperado is None and r.valor is not None:
            self._error("SEM-08", r, f"La regla '{regla.nombre}' no declara tipo de retorno y no puede retornar un valor.")
        elif esperado is not None and r.valor is None:
            self._error("SEM-08", r, f"La regla '{regla.nombre}' debe retornar un valor de tipo {esperado}.")
        elif esperado is not None and not self.compatible(esperado, tipo_valor):
            self._error("SEM-08", r.valor, f"Valor de retorno incompatible: la regla '{regla.nombre}' retorna {esperado} y se recibio {tipo_valor}.")

    def _s_LlamadaSentencia(self, s: A.LlamadaSentencia) -> None:
        self._llamada(s.llamada)

    # 7. Entrada / Salida
    def _s_Mostrar(self, m: A.Mostrar) -> None:
        for arg in m.args:
            self._expr(arg)

    def _s_Leer(self, l: A.Leer) -> None:
        sim = self.tabla.actual.buscar(l.nombre)
        if sim is None:
            self._error("SEM-01", l, f"'{l.nombre}' no ha sido declarado.")
        elif sim.categoria == "constante":
            self._error("SEM-05", l, f"No se puede leer un valor sobre la constante '{l.nombre}'.")
        elif sim.categoria == "regla":
            self._error("SEM-04", l, f"'{l.nombre}' es una regla; 'leer' requiere una variable.")
        else:
            l.simbolo = sim

    # --- Expresiones -----------------------------------------------------------------
    def _expr(self, e: A.Expr) -> Optional[Tipo]:
        e.tipo = getattr(self, "_e_" + type(e).__name__)(e)
        return e.tipo

    def _e_Literal(self, e: A.Literal) -> Tipo:
        if e.clase == "porcentaje":
            if not (Decimal(0) <= e.valor <= Decimal(100)):
                self._error("SEM-12", e, f"Porcentaje fuera de rango: {e.valor}% (debe estar entre 0% y 100%).")
            return PORCENTAJE
        if e.clase == "dominio":
            unidades_map = {
                "V": "voltaje", "A": "corriente", "W": "potencia", "KW": "potencia",
                "OHM": "resistencia", "KWH": "energia", "H": "tiempo", "S": "tiempo"
            }
            base = unidades_map.get(e.unidad, "dominio")
            return Tipo(base, e.unidad)
        return Tipo(e.clase)

    def _e_Variable(self, e: A.Variable) -> Optional[Tipo]:
        sim = self.tabla.actual.buscar(e.nombre)
        if sim is None:
            self._error("SEM-01", e, f"'{e.nombre}' no ha sido declarado.")
            return None
        if sim.categoria == "regla":
            self._error("SEM-04", e, f"'{e.nombre}' es una regla; debe invocarse con parentesis.")
            return None
        e.simbolo = sim
        return sim.tipo

    def _e_Llamada(self, e: A.Llamada) -> Optional[Tipo]:
        return self._llamada(e)

    def _llamada(self, e: A.Llamada) -> Optional[Tipo]:
        tipos_args = [self._expr(a) for a in e.args]
        sim = self.tabla.actual.buscar(e.nombre)
        if sim is None:
            self._error("SEM-01", e, f"La regla '{e.nombre}' no ha sido declarada.")
            return None
        if sim.categoria != "regla":
            self._error("SEM-04", e, f"'{e.nombre}' es de tipo {sim.tipo} y no puede invocarse como regla.")
            return None
        e.simbolo = sim
        if len(tipos_args) != len(sim.parametros):
            self._error("SEM-09", e, f"La regla '{e.nombre}' espera {len(sim.parametros)} argumento(s) y recibio {len(tipos_args)}.")
        else:
            for i, (esp, rec, arg) in enumerate(zip(sim.parametros, tipos_args, e.args), 1):
                if not self.compatible(esp, rec):
                    self._error("SEM-10", arg, f"Argumento {i} de '{e.nombre}': se esperaba {esp} y se recibio {rec}.")
        return sim.tipo

    def _e_Unaria(self, e: A.Unaria) -> Optional[Tipo]:
        t = self._expr(e.expr)
        if e.op == "no":
            if t is not None and t != BOOLEANO:
                self._error("SEM-04", e, f"Tipos incompatibles: el operador 'no' requiere booleano, se recibio {t}.")
            return BOOLEANO
        if t is not None and not (t.es_numerico or t.es_dominio or t == PORCENTAJE):
            self._error("SEM-04", e, f"Tipos incompatibles: el operador '-' no se aplica a {t}.")
            return None
        return t

    def _e_Binaria(self, e: A.Binaria) -> Optional[Tipo]:
        a, b = self._expr(e.izq), self._expr(e.der)
        if e.op in ("y", "o"):
            for lado, t in ((e.izq, a), (e.der, b)):
                if t is not None and t != BOOLEANO:
                    self._error("SEM-04", lado, f"Tipos incompatibles: el operador '{e.op}' requiere operandos booleanos, se recibio {t}.")
            return BOOLEANO
        if e.op in ("==", "!=", "<", "<=", ">", ">="):
            return self._comparar(e, a, b)
        if e.op in ("/", "mod") and isinstance(e.der, A.Literal) and e.der.clase in ("entero", "decimal", "dominio") and e.der.valor == 0:
            self._error("SEM-13", e.der, f"Division entre cero: el divisor de '{e.op}' es el literal 0.")
        return self._tipo_binario(e.op, a, b, e)

    def _comparar(self, e: A.Binaria, a: Optional[Tipo], b: Optional[Tipo]) -> Tipo:
        if a is None or b is None:
            return BOOLEANO
        if a.es_numerico and b.es_numerico:
            return BOOLEANO
        if a.es_dominio and b.es_dominio:
            if a != b:
                self._error("SEM-03", e, f"Unidades incompatibles: no se puede comparar {a} con {b}.")
            return BOOLEANO
        if a == b:
            return BOOLEANO
        self._error("SEM-04", e, f"Tipos incompatibles: no se puede comparar {a} con {b} usando '{e.op}'.")
        return BOOLEANO

    def _tipo_binario(self, op: str, a: Optional[Tipo], b: Optional[Tipo], nodo) -> Optional[Tipo]:
        if a is None or b is None:
            return None
        # 1. Operaciones aritmeticas escalares
        if a.es_numerico and b.es_numerico:
            if op == "mod":
                return ENTERO if a == ENTERO and b == ENTERO else DECIMAL
            if op == "/" or DECIMAL in (a, b):
                return DECIMAL
            return ENTERO

        # 2. Suma y Resta
        if op in ("+", "-"):
            if a.es_dominio and b.es_dominio:
                if a != b:
                    self._error("SEM-03", nodo, f"Unidades incompatibles: no se puede operar {a} con {b}.")
                    return None
                return a
            if a == PORCENTAJE and b == PORCENTAJE:
                return PORCENTAJE
            if op == "+" and a == TEXTO and b == TEXTO:
                return TEXTO

        # 3. Multiplicacion (Leyes fisicas de Voltio)
        elif op == "*":
            # Potencia: V * A = W
            if (a == A.voltaje("V") and b == A.corriente("A")) or (a == A.corriente("A") and b == A.voltaje("V")):
                return A.potencia("W")
            # Ley de Ohm: I * R = V
            if (a == A.corriente("A") and b == A.resistencia("OHM")) or (a == A.resistencia("OHM") and b == A.corriente("A")):
                return A.voltaje("V")
            # Energia: P (KW) * t (H) = KWH
            if (a == A.potencia("KW") and b == A.tiempo("H")) or (a == A.tiempo("H") and b == A.potencia("KW")):
                return A.energia("KWH")
            # Escalamiento: dominio * numero o dominio * porcentaje
            if a.es_dominio and (b.es_numerico or b == PORCENTAJE):
                return a
            if b.es_dominio and (a.es_numerico or a == PORCENTAJE):
                return b
            if PORCENTAJE in (a, b) and (a.es_numerico or b.es_numerico or a == b):
                return PORCENTAJE

        # 4. Division (Leyes fisicas de Voltio)
        elif op == "/":
            # I = P / V
            if a == A.potencia("W") and b == A.voltaje("V"):
                return A.corriente("A")
            # R = V / I
            if a == A.voltaje("V") and b == A.corriente("A"):
                return A.resistencia("OHM")
            # I = V / R
            if a == A.voltaje("V") and b == A.resistencia("OHM"):
                return A.corriente("A")
            # Dominio entre numero
            if a.es_dominio and b.es_numerico:
                return a
            # Cociente adimensional: dominio / mismo dominio
            if a.es_dominio and b.es_dominio:
                if a != b:
                    self._error("SEM-03", nodo, f"Unidades incompatibles: no se puede dividir {a} entre {b}.")
                    return None
                return DECIMAL
            if a == PORCENTAJE and b.es_numerico:
                return PORCENTAJE

        self._error("SEM-04", nodo, f"Operacion '{op}' invalida entre tipos {a} y {b}.")
        return None
