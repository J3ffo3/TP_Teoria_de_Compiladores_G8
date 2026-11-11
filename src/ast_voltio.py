from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

# ----------------------------------------------------------------------------
# Tipos del lenguaje Voltio
# ----------------------------------------------------------------------------
@dataclass(frozen=True)
class Tipo:
    nombre: str                   # entero, decimal, porcentaje, booleano, texto, voltaje, corriente, potencia, resistencia, energia, tiempo
    unidad: Optional[str] = None  # V, A, W, KW, OHM, KWH, H, S

    def __str__(self) -> str:
        return f"{self.nombre}<{self.unidad}>" if self.unidad else self.nombre

    @property
    def es_numerico(self) -> bool:
        return self.nombre in ("entero", "decimal")

    @property
    def es_dominio(self) -> bool:
        return self.unidad is not None

ENTERO = Tipo("entero")
DECIMAL = Tipo("decimal")
PORCENTAJE = Tipo("porcentaje")
BOOLEANO = Tipo("booleano")
TEXTO = Tipo("texto")

def voltaje(u="V"): return Tipo("voltaje", u)
def corriente(u="A"): return Tipo("corriente", u)
def potencia(u="W"): return Tipo("potencia", u)
def resistencia(u="OHM"): return Tipo("resistencia", u)
def energia(u="KWH"): return Tipo("energia", u)
def tiempo(u="H"): return Tipo("tiempo", u)

# ----------------------------------------------------------------------------
# Nodos del AST
# ----------------------------------------------------------------------------
@dataclass
class Nodo:
    linea: int = field(default=0, kw_only=True)
    columna: int = field(default=0, kw_only=True)

@dataclass
class Expr(Nodo):
    tipo: Optional[Tipo] = field(default=None, kw_only=True, repr=False)

@dataclass
class Literal(Expr):
    clase: str                    # entero, decimal, porcentaje, texto, booleano, dominio
    valor: object                 # int, Decimal, str, bool
    unidad: Optional[str] = None

@dataclass
class Variable(Expr):
    nombre: str
    simbolo: object = field(default=None, repr=False)

@dataclass
class Binaria(Expr):
    op: str                       # +, -, *, /, mod, ==, !=, <, <=, >, >=, y, o
    izq: Expr
    der: Expr

@dataclass
class Unaria(Expr):
    op: str                       # -, no
    expr: Expr

@dataclass
class Llamada(Expr):
    nombre: str
    args: list
    simbolo: object = field(default=None, repr=False)

@dataclass
class Bloque(Nodo):
    sentencias: list

@dataclass
class Declaracion(Nodo):
    constante: bool
    nombre: str
    tipo_decl: Tipo
    valor: Optional[Expr]
    simbolo: object = field(default=None, repr=False)

@dataclass
class Asignacion(Nodo):
    nombre: str
    op: str                       # =, +=, -=
    valor: Expr
    simbolo: object = field(default=None, repr=False)

@dataclass
class Si(Nodo):
    ramas: list                   # [(condicion, Bloque)]
    sino: Optional[Bloque]

@dataclass
class Mientras(Nodo):
    condicion: Expr
    cuerpo: Bloque

@dataclass
class Para(Nodo):
    variable: str
    desde: Expr
    hasta: Expr
    paso: Optional[Expr]
    cuerpo: Bloque
    simbolo: object = field(default=None, repr=False)

@dataclass
class Parametro(Nodo):
    nombre: str
    tipo_decl: Tipo

@dataclass
class Regla(Nodo):
    nombre: str
    parametros: list
    tipo_retorno: Optional[Tipo]
    cuerpo: Bloque

@dataclass
class Retornar(Nodo):
    valor: Optional[Expr]

@dataclass
class Mostrar(Nodo):
    args: list

@dataclass
class Leer(Nodo):
    nombre: str
    simbolo: object = field(default=None, repr=False)

@dataclass
class LlamadaSentencia(Nodo):
    llamada: Llamada

@dataclass
class Programa(Nodo):
    sentencias: list
