import os
import sys
import unittest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))
sys.path.insert(0, os.path.join(RAIZ, "tests"))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))

from antlr4 import CommonTokenStream, InputStream, Token
from construcciones import CONSTRUCCIONES
from errores import RecolectorErrores
from generated.VoltioLexer import VoltioLexer
from generated.VoltioParser import VoltioParser
from voltio import compilar

DIR_PRUEBAS = os.path.join(RAIZ, "tests")

def esperado(ruta: str) -> list[str]:
    with open(ruta, encoding="utf-8") as f:
        cabecera = f.readline().strip()
    if not cabecera.startswith("// espera:"):
        return []
    val = cabecera.split(":", 1)[1].split()
    return [] if val == ["OK"] else val

def obtenido(res) -> list[str]:
    return [f"{e.codigo}@{e.linea}" for e in res.errores]

class TestGramatica(unittest.TestCase):
    def test_lineamientos_estandar(self):
        from verificar_gramatica import verificar
        ruta_g4 = os.path.join(RAIZ, "grammar", "Voltio.g4")
        errores = verificar(ruta_g4)
        self.assertEqual(errores, [], f"Inconsistencias en gramatica: {errores}")

    def test_reconocimiento_construcciones(self):
        for c in CONSTRUCCIONES:
            for ejemplo in c["ejemplos"]:
                with self.subTest(construccion=c["id"], ejemplo=ejemplo):
                    lexer = VoltioLexer(InputStream(ejemplo))
                    parser = VoltioParser(CommonTokenStream(lexer))
                    err = RecolectorErrores("SIN")
                    parser.removeErrorListeners()
                    parser.addErrorListener(err)
                    getattr(parser, c["regla_antlr"])()
                    self.assertEqual(err.errores, [])
                    self.assertEqual(parser.getCurrentToken().type, Token.EOF)

class TestSemantico(unittest.TestCase):
    def test_programas_validos(self):
        dir_validos = os.path.join(DIR_PRUEBAS, "semantico", "validos")
        for arch in sorted(os.listdir(dir_validos)):
            if arch.endswith(".vo"):
                ruta = os.path.join(dir_validos, arch)
                with self.subTest(archivo=arch):
                    res = compilar(ruta=ruta)
                    self.assertEqual(obtenido(res), [], [str(e) for e in res.errores])

    def test_programas_invalidos(self):
        dir_invalidos = os.path.join(DIR_PRUEBAS, "semantico", "invalidos")
        for arch in sorted(os.listdir(dir_invalidos)):
            if arch.endswith(".vo"):
                ruta = os.path.join(dir_invalidos, arch)
                with self.subTest(archivo=arch):
                    res = compilar(ruta=ruta)
                    self.assertEqual(obtenido(res), esperado(ruta), [str(e) for e in res.errores])

if __name__ == "__main__":
    unittest.main(verbosity=2)
