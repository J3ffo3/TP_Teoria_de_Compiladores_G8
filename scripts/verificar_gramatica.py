import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def tokenizar_g4(texto: str):
    i, n, out = 0, len(texto), []
    while i < n:
        c = texto[i]
        if texto.startswith("//", i):
            j = texto.find("\n", i)
            j = n if j < 0 else j
            i = j
            continue
        if texto.startswith("/*", i):
            j = texto.index("*/", i) + 2
            i = j
            continue
        if c == "'":
            j = i + 1
            while texto[j] != "'":
                j += 2 if texto[j] == "\\" else 1
            out.append(("LIT", texto[i:j + 1]))
            i = j + 1
            continue
        if c == "[":
            j = i + 1
            while texto[j] != "]":
                j += 2 if texto[j] == "\\" else 1
            out.append(("SET", texto[i:j + 1]))
            i = j + 1
            continue
        out.append(("OTRO", c))
        i += 1
    return out

def reglas(texto: str):
    toks = tokenizar_g4(texto)
    resultado, actual = [], []
    for t in toks:
        if t == ("OTRO", ";"):
            resultado.append(actual)
            actual = []
        else:
            actual.append(t)
    salida = []
    for r in resultado:
        texto_regla = "".join(v for _, v in r)
        m = re.match(r"\s*(fragment\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*:", texto_regla)
        if not m:
            continue
        idx = texto_regla.index(":", m.start(2))
        acumulado, cuerpo = 0, []
        for tipo, v in r:
            if acumulado > idx:
                cuerpo.append((tipo, v))
            acumulado += len(v)
        salida.append((m.group(2), bool(m.group(1)), cuerpo))
    return salida

def verificar(ruta: str) -> list[str]:
    with open(ruta, encoding="utf-8") as f:
        texto = f.read()
    errores = []
    lista = reglas(texto)
    for nombre, es_fragment, cuerpo in lista:
        es_parser = nombre[0].islower()
        fuera = "".join(v for tipo, v in cuerpo if tipo == "OTRO")
        sin_accion = re.sub(r"->\s*skip", "", fuera)
        if es_parser and any(tipo == "LIT" for tipo, _ in cuerpo):
            lits = [v for tipo, v in cuerpo if tipo == "LIT"]
            errores.append(f"Regla '{nombre}': contiene literales en el parser {lits}")
        if "?" in sin_accion:
            errores.append(f"Regla '{nombre}': uso de operador '?' no permitido en forma BNF pura")
        if "*" in sin_accion or "+" in sin_accion:
            errores.append(f"Regla '{nombre}': uso de repeticiones '*' o '+' en lugar de recursion")
        if "(" in sin_accion or ")" in sin_accion:
            errores.append(f"Regla '{nombre}': subreglas agrupadas con parentesis")
        if "=" in sin_accion or "#" in sin_accion:
            errores.append(f"Regla '{nombre}': etiquetas inline o alternativas con '#'")
        if any(tipo == "LIT" and "/*" in v for tipo, v in cuerpo):
            errores.append(f"Regla '{nombre}': comentarios de bloque no permitidos")
            
    orden = [n for n, frag, _ in lista if n[0].isupper() and not frag]
    if "ID" in orden:
        pos_id = orden.index("ID")
        for nombre, frag, cuerpo in lista:
            if frag or not nombre[0].isupper():
                continue
            lits = [v.strip("'") for tipo, v in cuerpo if tipo == "LIT"]
            otros = [v for tipo, v in cuerpo if tipo == "OTRO" and v.strip() and v not in "|"]
            if lits and not otros and all(re.fullmatch(r"[A-Za-z]+", x) for x in lits):
                if orden.index(nombre) > pos_id:
                    errores.append(f"Token '{nombre}': palabra reservada declarada despues de ID")
    else:
        errores.append("Error estructural: no se encontro el token ID")
    return errores

def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "grammar", "Voltio.g4")
    errores = verificar(ruta)
    n_reglas = len(reglas(open(ruta, encoding="utf-8").read()))
    if errores:
        print(f"[FALLO] {ruta}: {len(errores)} inconsistencia(s) encontrada(s):")
        for e in errores:
            print("  - " + e)
        return 1
    print(f"[OK] {ruta}: {n_reglas} producciones analizadas. Estructura BNF estandar verificada correctamente.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
