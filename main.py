import sys
import os
from antlr4 import CommonTokenStream, FileStream
from gen.MarkovLangLexer import MarkovLangLexer
from gen.MarkovLangParser import MarkovLangParser
from semantic.semantic_visitor import SemanticVisitor
from codegen import generate_c_code

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo.txt> [--tokens] [--tree]")
        return

    archivo = sys.argv[1]
    tokens_flag = "--tokens" in sys.argv
    tree_flag = "--tree" in sys.argv

    input_stream = FileStream(archivo, encoding='utf-8')
    lexer = MarkovLangLexer(input_stream)
    stream = CommonTokenStream(lexer)

    if tokens_flag:
        stream.fill()
        print("\n=== TOKENS RECONOCIDOS ===")
        for token in stream.tokens:
            token_name = lexer.symbolicNames[token.type] if token.type >= 0 else "EOF"
            print(f"[{token.line}:{token.column}] {token_name:<16} -> {repr(token.text)}")

    parser = MarkovLangParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print('Errores sintácticos encontrados. Abortando.')
        sys.exit(1)

    if tree_flag:
        print("\n=== ÁRBOL SINTÁCTICO (PARSE TREE) ===")
        print(tree.toStringTree(recog=parser))

    visitor = SemanticVisitor()
    visitor.visit(tree)

    if visitor.errors:
        print('\n=== ERRORES SEMÁNTICOS ===')
        for e in visitor.errors:
            print(' ', e)
        sys.exit(1)
    else:
        print('Análisis semántico: OK')

    warns = visitor.symtab.unused_warnings()
    if warns:
        print('\n=== ADVERTENCIAS ===')
        for w in warns:
            print(' ', w)

    # Generación de código de bajo nivel (C)
    if visitor.symtab.chains:
        base_name = os.path.splitext(os.path.basename(archivo))[0]
        output_c = os.path.join("output", f"{base_name}.c")
        generate_c_code(visitor.symtab.chains, visitor.simulations, visitor.seed, output_c)
        print(f"\n[Compilación a Bajo Nivel] Código C generado en: {output_c}")

if __name__ == "__main__":
    main()
