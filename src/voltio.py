import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from antlr4 import CommonTokenStream, FileStream, InputStream, Token
from antlr4.tree.Tree import TerminalNode
from constructor_ast import ConstructorAST
from errores import ErrorCompilacion, RecolectorErrores
from generated.VoltioLexer import VoltioLexer
from generated.VoltioParser import VoltioParser
from semantico import AnalizadorSemantico
from generador_llvm import GeneradorLLVM

VERSION = "0.2.0 (Hito 2)"

class ResultadoCompilacion:
    def __init__(self):
        self.tokens = []
        self.arbol = None
        self.parser = None
        self.ast = None
        self.semantico = None
        self.ir = None
        self.errores: list[ErrorCompilacion] = []

    @property
    def ok(self) -> bool:
        return not self.errores

def compilar(codigo: str | None = None, ruta: str | None = None, hasta: str = "llvm") -> ResultadoCompilacion:
    res = ResultadoCompilacion()
    entrada = FileStream(ruta, encoding="utf-8") if ruta else InputStream(codigo)

    # 1. Analisis Lexico
    lexer = VoltioLexer(entrada)
    err_lex = RecolectorErrores("LEX")
    lexer.removeErrorListeners()
    lexer.addErrorListener(err_lex)
    flujo = CommonTokenStream(lexer)
    flujo.fill()
    res.tokens = [t for t in flujo.tokens if t.type != Token.EOF]
    res.errores.extend(err_lex.errores)
    if hasta == "lexico":
        return res

    # 2. Analisis Sintactico
    parser = VoltioParser(flujo)
    err_sin = RecolectorErrores("SIN")
    parser.removeErrorListeners()
    parser.addErrorListener(err_sin)
    res.arbol = parser.programa()
    res.parser = parser
    res.errores.extend(err_sin.errores)
    if hasta == "sintactico" or res.errores:
        return res

    # 3. Analisis Semantico (sobre AST)
    res.ast = ConstructorAST().visit(res.arbol)
    sem = AnalizadorSemantico()
    sem.analizar(res.ast)
    res.semantico = sem
    res.errores.extend(sem.errores)
    if hasta == "semantico" or res.errores:
        return res

    # 4. Generacion de Codigo LLVM IR (Avance Hito 2)
    try:
        gen = GeneradorLLVM()
        modulo_llvm = gen.generar(res.ast)
        res.ir = str(modulo_llvm)
    except Exception as exc:
        res.errores.append(ErrorCompilacion("GEN", "GEN-01", 1, 1, f"Error de generacion: {exc}"))

    return res

def imprimir_tokens(res: ResultadoCompilacion) -> None:
    nombres = VoltioLexer.symbolicNames
    print(f"{'#':>4}  {'Lin:Col':<9} {'Token':<20} Lexema")
    print("-" * 55)
    for i, t in enumerate(res.tokens, 1):
        print(f"{i:>4}  {f'{t.line}:{t.column + 1}':<9} {nombres[t.type]:<20} {t.text}")

def imprimir_arbol(nodo, parser, prefijo: str = "", ultimo: bool = True, raiz: bool = True) -> None:
    conector = "" if raiz else ("`-- " if ultimo else "|-- ")
    if isinstance(nodo, TerminalNode):
        tok = nodo.getSymbol()
        etiqueta = "EOF" if tok.type == Token.EOF else f"{VoltioLexer.symbolicNames[tok.type]} '{tok.text}'"
    else:
        etiqueta = parser.ruleNames[nodo.getRuleIndex()]
        if nodo.getChildCount() == 0:
            etiqueta += " (epsilon)"
    print(prefijo + conector + etiqueta)
    if isinstance(nodo, TerminalNode):
        return
    hijos = list(nodo.getChildren()) if nodo.getChildCount() else []
    nuevo_prefijo = prefijo + ("" if raiz else ("    " if ultimo else "|   "))
    for i, hijo in enumerate(hijos):
        imprimir_arbol(hijo, parser, nuevo_prefijo, i == len(hijos) - 1, False)

def imprimir_simbolos(res: ResultadoCompilacion) -> None:
    print(f"{'Ambito':<26} {'Nombre':<20} {'Categoria':<12} {'Linea':<6} Tipo")
    print("-" * 80)
    for ambito in res.semantico.tabla.todos:
        for s in ambito.simbolos.values():
            tipo = str(s.tipo) if s.tipo is not None else "(sin retorno)"
            if s.categoria == "regla":
                tipo = f"({', '.join(map(str, s.parametros))}) -> {tipo}"
            print(f"{ambito.nombre:<26} {s.nombre:<20} {s.categoria:<12} {s.linea:<6} {tipo}")

def main():
    ap = argparse.ArgumentParser(prog="voltio", description="Compilador del lenguaje Voltio")
    ap.add_argument("archivo", help="programa fuente .vo")
    ap.add_argument("--tokens", action="store_true", help="muestra la tabla de tokens")
    ap.add_argument("--arbol", action="store_true", help="muestra el arbol sintactico")
    ap.add_argument("--simbolos", action="store_true", help="muestra la tabla de simbolos")
    ap.add_argument("--solo-lexico", action="store_true", help="ejecuta solo el analisis lexico")
    ap.add_argument("--solo-sintactico", action="store_true", help="ejecuta hasta el analisis sintactico")
    ap.add_argument("--llvm", nargs="?", const="", metavar="SALIDA.ll", help="genera el codigo intermedio LLVM IR")
    args = ap.parse_args()

    if not os.path.isfile(args.archivo):
        print(f"Error: no existe el archivo '{args.archivo}'.", file=sys.stderr)
        return 2

    if args.solo_lexico:
        hasta = "lexico"
    elif args.solo_sintactico:
        hasta = "sintactico"
    elif args.llvm is not None:
        hasta = "llvm"
    else:
        hasta = "semantico"

    res = compilar(ruta=args.archivo, hasta=hasta)

    print(f"Voltio {VERSION} | {args.archivo}")
    limite = {"lexico": 1, "sintactico": 2, "semantico": 3, "llvm": 4}[hasta]
    fases = [
        ("LEX", "Analisis lexico"), 
        ("SIN", "Analisis sintactico"), 
        ("SEM", "Analisis semantico"),
        ("GEN", "Generacion LLVM IR")
    ]
    
    bloqueado = False
    for i, (fase, nombre) in enumerate(fases[:limite], 1):
        n = sum(1 for e in res.errores if e.fase == fase)
        if bloqueado:
            estado = "OMITIDO (errores previos)"
        elif n:
            estado = f"{n} error(es)"
            bloqueado = True
        else:
            estado = "OK" + (f" ({len(res.tokens)} tokens)" if fase == "LEX" else "")
        print(f"  [{i}/{limite}] {nombre:<22} {estado}")

    if args.tokens:
        print()
        imprimir_tokens(res)
    if args.arbol and res.arbol is not None:
        print()
        imprimir_arbol(res.arbol, res.parser)
    if args.simbolos and res.semantico is not None:
        print()
        imprimir_simbolos(res)

    if res.ir is not None:
        destino = args.llvm if args.llvm else os.path.splitext(args.archivo)[0] + ".ll"
        with open(destino, "w", encoding="utf-8") as f:
            f.write(res.ir)
        print(f"\n[OK] Codigo LLVM IR generado exitosamente en: {destino}")

    print()
    if res.ok:
        print("Resultado: Programa compilado exitosamente.")
        return 0
    for e in res.errores:
        print(e)
    print(f"\nResultado: {len(res.errores)} error(es) encontrados.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
