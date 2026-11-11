import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
from verificar_gramatica import reglas

RUTA_G4 = os.path.join(RAIZ, "grammar", "Voltio.g4")

GRUPOS = [
    ("G0", "Estructura general del programa", ["programa", "listaSentencias", "sentencia", "bloque"]),
    ("G1", "Declaracion de variables y constantes", ["declaracion", "inicializacion", "tipo"]),
    ("G2", "Asignacion", ["asignacion", "opAsignacion"]),
    ("G3", "Expresiones", ["expresion", "conjuncion", "negacion", "igualdad", "relacional", "aritmetica",
                           "termino", "unario", "primario", "literal", "numero", "llamada", "argumentos",
                           "argumentosCola"]),
    ("G4", "Sentencias selectivas", ["seleccion", "parteSino", "colaSino"]),
    ("G5", "Sentencias iterativas", ["iteracion", "pasoOpcional"]),
    ("G6", "Reglas (funciones), retorno y llamadas", ["regla", "parametros", "parametrosCola", "parametro",
                                                      "tipoRetorno", "retorno", "valorRetorno", "llamadaSentencia"]),
    ("G7", "Entrada y salida", ["entradaSalida"]),
]

def producciones() -> dict:
    with open(RUTA_G4, encoding="utf-8") as f:
        texto = f.read()
    salida = {}
    for nombre, es_fragment, cuerpo in reglas(texto):
        if not nombre[0].islower():
            continue
        cadena = "".join(v for _, v in cuerpo)
        alternativas = [alt.split() for alt in cadena.split("|")]
        salida[nombre] = alternativas
    return salida
