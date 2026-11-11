import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))
sys.path.insert(0, os.path.join(RAIZ, "tests"))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

from antlr4 import CommonTokenStream, InputStream, Token
from antlr4.atn.PredictionMode import PredictionMode
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNode

from construcciones import CONSTRUCCIONES
from generated.VoltioLexer import VoltioLexer
from generated.VoltioParser import VoltioParser
from gramatica_bnf import GRUPOS, producciones

class Vigilante(ErrorListener):
    def __init__(self):
        self.errores = []
        self.ambiguedades = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append(f"{line}:{column} {msg}")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        if exact:
            self.ambiguedades.append((startIndex, stopIndex, str(ambigAlts)))

def analizar(codigo: str, regla: str):
    lexer = VoltioLexer(InputStream(codigo))
    lexer.removeErrorListeners()
    tokens = CommonTokenStream(lexer)
    parser = VoltioParser(tokens)
    parser.removeErrorListeners()
    vig = Vigilante()
    parser.addErrorListener(vig)
    parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION
    arbol = getattr(parser, regla)()
    completo = parser.getCurrentToken().type == Token.EOF
    return arbol, parser, vig, completo

def simbolo(nodo, parser) -> str:
    if isinstance(nodo, TerminalNode):
        return VoltioLexer.symbolicNames[nodo.getSymbol().type]
    return parser.ruleNames[nodo.getRuleIndex()]

def derivacion_izquierda(arbol, parser):
    forma = [arbol]
    pasos = [([simbolo(arbol, parser)], None)]
    while True:
        idx = next((i for i, x in enumerate(forma) if not isinstance(x, TerminalNode)), None)
        if idx is None:
            break
        nodo = forma[idx]
        hijos = list(nodo.getChildren()) if nodo.getChildCount() else []
        produccion = (simbolo(nodo, parser), [simbolo(h, parser) for h in hijos])
        forma = forma[:idx] + hijos + forma[idx + 1:]
        pasos.append(([simbolo(x, parser) for x in forma], produccion))
    return pasos

def main() -> int:
    prods = producciones()
    resultado, fallos = [], 0
    for c in CONSTRUCCIONES:
        entrada = {"id": c["id"], "nombre": c["nombre"], "simbolo": c["simbolo"], "derivaciones": []}
        aceptados = 0
        for i, ejemplo in enumerate(c["ejemplos"]):
            arbol, parser, vig, completo = analizar(ejemplo, c["regla_antlr"])
            if vig.errores or not completo or vig.ambiguedades:
                print(f"[FALLO] {c['id']}.{i + 1} {ejemplo}")
                fallos += 1
                continue
            aceptados += 1
            if i not in c["derivar"]:
                continue
            pasos = derivacion_izquierda(arbol, parser)
            for forma, prod in pasos[1:]:
                nt, cuerpo = prod
                if cuerpo not in prods[nt]:
                    print(f"[FALLO] Produccion no encontrada: {nt} -> {cuerpo}")
                    fallos += 1
            lexemas = [t.text for t in VoltioLexer(InputStream(ejemplo)).getAllTokens()]
            entrada["derivaciones"].append({
                "ejemplo": ejemplo,
                "tokens": pasos[-1][0],
                "lexemas": lexemas,
                "pasos": [forma for forma, _ in pasos],
                "producciones": [None] + [f"{nt} -> {' '.join(cu) if cu else 'epsilon'}" for _, (nt, cu) in pasos[1:]],
            })
        resultado.append(entrada)
        print(f"[{c['id']}] {aceptados}/5 ejemplos reconocidos sin ambiguedad ({len(entrada['derivaciones'])} derivaciones generadas)")

    docs = os.path.join(RAIZ, "docs")
    os.makedirs(docs, exist_ok=True)
    with open(os.path.join(docs, "derivaciones.json"), "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    titulos = {gid: t for gid, t, _ in GRUPOS}
    md = [
        "# Anexo A: Derivaciones Mas a la Izquierda (Hito 2)", "",
        "Generado automaticamente a partir de grammar/Voltio.g4 sin ambiguedades.",
        "Terminales en mayusculas, no terminales en minusculas.", ""
    ]
    for g in resultado:
        md += [f"## {g['id']}. {titulos[g['id']]}", ""]
        for n, d in enumerate(g["derivaciones"], 1):
            md += [f"### Ejemplo {g['id']}.{n}", "", "```voltio", d["ejemplo"], "```", "",
                   "Cadena de tokens: `" + " ".join(d["tokens"]) + "`", "", "```"]
            for k, paso in enumerate(d["pasos"]):
                linea = ("     " if k == 0 else "=>lm ") + " ".join(paso)
                md.append(linea)
            md += ["```", ""]
    with open(os.path.join(docs, "anexo_derivaciones.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    total = sum(len(g["derivaciones"]) for g in resultado)
    print(f"\n[OK] {total} derivaciones generadas exitosamente en docs/anexo_derivaciones.md")
    return 1 if fallos else 0

if __name__ == "__main__":
    sys.exit(main())
