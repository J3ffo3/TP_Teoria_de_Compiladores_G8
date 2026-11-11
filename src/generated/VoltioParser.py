# Generated from grammar/Voltio.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,63,404,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,82,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,93,8,2,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,114,8,4,1,5,1,5,1,5,3,5,119,8,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,150,8,6,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,165,8,9,10,9,12,9,168,9,9,1,10,1,
        10,1,10,1,10,1,10,1,10,5,10,176,8,10,10,10,12,10,179,9,10,1,11,1,
        11,1,11,3,11,184,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,5,12,195,8,12,10,12,12,12,198,9,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,215,8,13,10,
        13,12,13,218,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,
        14,229,8,14,10,14,12,14,232,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,5,15,246,8,15,10,15,12,15,249,9,15,1,
        16,1,16,1,16,3,16,254,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,
        17,263,8,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,3,18,289,8,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,
        21,1,21,3,21,302,8,21,1,22,1,22,1,22,1,22,1,22,3,22,309,8,22,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,3,24,321,8,24,1,25,
        1,25,3,25,325,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,3,26,342,8,26,1,27,1,27,1,27,3,27,
        347,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,
        1,29,3,29,361,8,29,1,30,1,30,1,30,1,30,1,30,3,30,368,8,30,1,31,1,
        31,1,31,1,31,1,32,1,32,1,32,3,32,377,8,32,1,33,1,33,1,33,1,33,1,
        34,1,34,3,34,385,8,34,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,402,8,36,1,36,0,6,18,20,24,
        26,28,30,37,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,0,2,2,0,37,
        38,45,45,1,0,58,59,427,0,74,1,0,0,0,2,81,1,0,0,0,4,92,1,0,0,0,6,
        94,1,0,0,0,8,113,1,0,0,0,10,118,1,0,0,0,12,149,1,0,0,0,14,151,1,
        0,0,0,16,156,1,0,0,0,18,158,1,0,0,0,20,169,1,0,0,0,22,183,1,0,0,
        0,24,185,1,0,0,0,26,199,1,0,0,0,28,219,1,0,0,0,30,233,1,0,0,0,32,
        253,1,0,0,0,34,262,1,0,0,0,36,288,1,0,0,0,38,290,1,0,0,0,40,292,
        1,0,0,0,42,301,1,0,0,0,44,308,1,0,0,0,46,310,1,0,0,0,48,320,1,0,
        0,0,50,324,1,0,0,0,52,341,1,0,0,0,54,346,1,0,0,0,56,348,1,0,0,0,
        58,360,1,0,0,0,60,367,1,0,0,0,62,369,1,0,0,0,64,376,1,0,0,0,66,378,
        1,0,0,0,68,384,1,0,0,0,70,386,1,0,0,0,72,401,1,0,0,0,74,75,3,2,1,
        0,75,76,5,0,0,1,76,1,1,0,0,0,77,78,3,4,2,0,78,79,3,2,1,0,79,82,1,
        0,0,0,80,82,1,0,0,0,81,77,1,0,0,0,81,80,1,0,0,0,82,3,1,0,0,0,83,
        93,3,8,4,0,84,93,3,14,7,0,85,93,3,46,23,0,86,93,3,52,26,0,87,93,
        3,56,28,0,88,93,3,66,33,0,89,93,3,72,36,0,90,93,3,70,35,0,91,93,
        3,6,3,0,92,83,1,0,0,0,92,84,1,0,0,0,92,85,1,0,0,0,92,86,1,0,0,0,
        92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,0,92,91,1,
        0,0,0,93,5,1,0,0,0,94,95,5,52,0,0,95,96,3,2,1,0,96,97,5,53,0,0,97,
        7,1,0,0,0,98,99,5,1,0,0,99,100,5,61,0,0,100,101,5,56,0,0,101,102,
        3,12,6,0,102,103,3,10,5,0,103,104,5,54,0,0,104,114,1,0,0,0,105,106,
        5,2,0,0,106,107,5,61,0,0,107,108,5,56,0,0,108,109,3,12,6,0,109,110,
        5,45,0,0,110,111,3,18,9,0,111,112,5,54,0,0,112,114,1,0,0,0,113,98,
        1,0,0,0,113,105,1,0,0,0,114,9,1,0,0,0,115,116,5,45,0,0,116,119,3,
        18,9,0,117,119,1,0,0,0,118,115,1,0,0,0,118,117,1,0,0,0,119,11,1,
        0,0,0,120,150,5,3,0,0,121,150,5,4,0,0,122,150,5,5,0,0,123,150,5,
        6,0,0,124,150,5,7,0,0,125,126,5,8,0,0,126,127,5,43,0,0,127,128,5,
        14,0,0,128,150,5,44,0,0,129,130,5,9,0,0,130,131,5,43,0,0,131,132,
        5,15,0,0,132,150,5,44,0,0,133,134,5,10,0,0,134,135,5,43,0,0,135,
        136,5,16,0,0,136,150,5,44,0,0,137,138,5,11,0,0,138,139,5,43,0,0,
        139,140,5,17,0,0,140,150,5,44,0,0,141,142,5,12,0,0,142,143,5,43,
        0,0,143,144,5,18,0,0,144,150,5,44,0,0,145,146,5,13,0,0,146,147,5,
        43,0,0,147,148,5,19,0,0,148,150,5,44,0,0,149,120,1,0,0,0,149,121,
        1,0,0,0,149,122,1,0,0,0,149,123,1,0,0,0,149,124,1,0,0,0,149,125,
        1,0,0,0,149,129,1,0,0,0,149,133,1,0,0,0,149,137,1,0,0,0,149,141,
        1,0,0,0,149,145,1,0,0,0,150,13,1,0,0,0,151,152,5,61,0,0,152,153,
        3,16,8,0,153,154,3,18,9,0,154,155,5,54,0,0,155,15,1,0,0,0,156,157,
        7,0,0,0,157,17,1,0,0,0,158,159,6,9,-1,0,159,160,3,20,10,0,160,166,
        1,0,0,0,161,162,10,2,0,0,162,163,5,32,0,0,163,165,3,20,10,0,164,
        161,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,
        19,1,0,0,0,168,166,1,0,0,0,169,170,6,10,-1,0,170,171,3,22,11,0,171,
        177,1,0,0,0,172,173,10,2,0,0,173,174,5,31,0,0,174,176,3,22,11,0,
        175,172,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,
        178,21,1,0,0,0,179,177,1,0,0,0,180,181,5,33,0,0,181,184,3,22,11,
        0,182,184,3,24,12,0,183,180,1,0,0,0,183,182,1,0,0,0,184,23,1,0,0,
        0,185,186,6,12,-1,0,186,187,3,26,13,0,187,196,1,0,0,0,188,189,10,
        3,0,0,189,190,5,39,0,0,190,195,3,26,13,0,191,192,10,2,0,0,192,193,
        5,40,0,0,193,195,3,26,13,0,194,188,1,0,0,0,194,191,1,0,0,0,195,198,
        1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,25,1,0,0,0,198,196,1,
        0,0,0,199,200,6,13,-1,0,200,201,3,28,14,0,201,216,1,0,0,0,202,203,
        10,5,0,0,203,204,5,43,0,0,204,215,3,28,14,0,205,206,10,4,0,0,206,
        207,5,41,0,0,207,215,3,28,14,0,208,209,10,3,0,0,209,210,5,44,0,0,
        210,215,3,28,14,0,211,212,10,2,0,0,212,213,5,42,0,0,213,215,3,28,
        14,0,214,202,1,0,0,0,214,205,1,0,0,0,214,208,1,0,0,0,214,211,1,0,
        0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,27,1,0,0,
        0,218,216,1,0,0,0,219,220,6,14,-1,0,220,221,3,30,15,0,221,230,1,
        0,0,0,222,223,10,3,0,0,223,224,5,46,0,0,224,229,3,30,15,0,225,226,
        10,2,0,0,226,227,5,47,0,0,227,229,3,30,15,0,228,222,1,0,0,0,228,
        225,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,
        29,1,0,0,0,232,230,1,0,0,0,233,234,6,15,-1,0,234,235,3,32,16,0,235,
        247,1,0,0,0,236,237,10,4,0,0,237,238,5,48,0,0,238,246,3,32,16,0,
        239,240,10,3,0,0,240,241,5,49,0,0,241,246,3,32,16,0,242,243,10,2,
        0,0,243,244,5,36,0,0,244,246,3,32,16,0,245,236,1,0,0,0,245,239,1,
        0,0,0,245,242,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,248,1,
        0,0,0,248,31,1,0,0,0,249,247,1,0,0,0,250,251,5,47,0,0,251,254,3,
        32,16,0,252,254,3,34,17,0,253,250,1,0,0,0,253,252,1,0,0,0,254,33,
        1,0,0,0,255,256,5,50,0,0,256,257,3,18,9,0,257,258,5,51,0,0,258,263,
        1,0,0,0,259,263,3,40,20,0,260,263,3,36,18,0,261,263,5,61,0,0,262,
        255,1,0,0,0,262,259,1,0,0,0,262,260,1,0,0,0,262,261,1,0,0,0,263,
        35,1,0,0,0,264,265,3,38,19,0,265,266,5,14,0,0,266,289,1,0,0,0,267,
        268,3,38,19,0,268,269,5,15,0,0,269,289,1,0,0,0,270,271,3,38,19,0,
        271,272,5,16,0,0,272,289,1,0,0,0,273,274,3,38,19,0,274,275,5,17,
        0,0,275,289,1,0,0,0,276,277,3,38,19,0,277,278,5,18,0,0,278,289,1,
        0,0,0,279,280,3,38,19,0,280,281,5,19,0,0,281,289,1,0,0,0,282,289,
        5,59,0,0,283,289,5,58,0,0,284,289,5,57,0,0,285,289,5,60,0,0,286,
        289,5,34,0,0,287,289,5,35,0,0,288,264,1,0,0,0,288,267,1,0,0,0,288,
        270,1,0,0,0,288,273,1,0,0,0,288,276,1,0,0,0,288,279,1,0,0,0,288,
        282,1,0,0,0,288,283,1,0,0,0,288,284,1,0,0,0,288,285,1,0,0,0,288,
        286,1,0,0,0,288,287,1,0,0,0,289,37,1,0,0,0,290,291,7,1,0,0,291,39,
        1,0,0,0,292,293,5,61,0,0,293,294,5,50,0,0,294,295,3,42,21,0,295,
        296,5,51,0,0,296,41,1,0,0,0,297,298,3,18,9,0,298,299,3,44,22,0,299,
        302,1,0,0,0,300,302,1,0,0,0,301,297,1,0,0,0,301,300,1,0,0,0,302,
        43,1,0,0,0,303,304,5,55,0,0,304,305,3,18,9,0,305,306,3,44,22,0,306,
        309,1,0,0,0,307,309,1,0,0,0,308,303,1,0,0,0,308,307,1,0,0,0,309,
        45,1,0,0,0,310,311,5,20,0,0,311,312,5,50,0,0,312,313,3,18,9,0,313,
        314,5,51,0,0,314,315,3,6,3,0,315,316,3,48,24,0,316,47,1,0,0,0,317,
        318,5,21,0,0,318,321,3,50,25,0,319,321,1,0,0,0,320,317,1,0,0,0,320,
        319,1,0,0,0,321,49,1,0,0,0,322,325,3,46,23,0,323,325,3,6,3,0,324,
        322,1,0,0,0,324,323,1,0,0,0,325,51,1,0,0,0,326,327,5,22,0,0,327,
        328,5,50,0,0,328,329,3,18,9,0,329,330,5,51,0,0,330,331,3,6,3,0,331,
        342,1,0,0,0,332,333,5,23,0,0,333,334,5,61,0,0,334,335,5,24,0,0,335,
        336,3,18,9,0,336,337,5,25,0,0,337,338,3,18,9,0,338,339,3,54,27,0,
        339,340,3,6,3,0,340,342,1,0,0,0,341,326,1,0,0,0,341,332,1,0,0,0,
        342,53,1,0,0,0,343,344,5,26,0,0,344,347,3,18,9,0,345,347,1,0,0,0,
        346,343,1,0,0,0,346,345,1,0,0,0,347,55,1,0,0,0,348,349,5,27,0,0,
        349,350,5,61,0,0,350,351,5,50,0,0,351,352,3,58,29,0,352,353,5,51,
        0,0,353,354,3,64,32,0,354,355,3,6,3,0,355,57,1,0,0,0,356,357,3,62,
        31,0,357,358,3,60,30,0,358,361,1,0,0,0,359,361,1,0,0,0,360,356,1,
        0,0,0,360,359,1,0,0,0,361,59,1,0,0,0,362,363,5,55,0,0,363,364,3,
        62,31,0,364,365,3,60,30,0,365,368,1,0,0,0,366,368,1,0,0,0,367,362,
        1,0,0,0,367,366,1,0,0,0,368,61,1,0,0,0,369,370,5,61,0,0,370,371,
        5,56,0,0,371,372,3,12,6,0,372,63,1,0,0,0,373,374,5,56,0,0,374,377,
        3,12,6,0,375,377,1,0,0,0,376,373,1,0,0,0,376,375,1,0,0,0,377,65,
        1,0,0,0,378,379,5,28,0,0,379,380,3,68,34,0,380,381,5,54,0,0,381,
        67,1,0,0,0,382,385,3,18,9,0,383,385,1,0,0,0,384,382,1,0,0,0,384,
        383,1,0,0,0,385,69,1,0,0,0,386,387,3,40,20,0,387,388,5,54,0,0,388,
        71,1,0,0,0,389,390,5,29,0,0,390,391,5,50,0,0,391,392,3,18,9,0,392,
        393,3,44,22,0,393,394,5,51,0,0,394,395,5,54,0,0,395,402,1,0,0,0,
        396,397,5,30,0,0,397,398,5,50,0,0,398,399,5,61,0,0,399,400,5,51,
        0,0,400,402,5,54,0,0,401,389,1,0,0,0,401,396,1,0,0,0,402,73,1,0,
        0,0,30,81,92,113,118,149,166,177,183,194,196,214,216,228,230,245,
        247,253,262,288,301,308,320,324,341,346,360,367,376,384,401
    ]

class VoltioParser ( Parser ):

    grammarFileName = "Voltio.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'const'", "'entero'", "'decimal'", 
                     "'porcentaje'", "'booleano'", "'texto'", "'voltaje'", 
                     "'corriente'", "'potencia'", "'resistencia'", "'energia'", 
                     "'tiempo'", "'V'", "'A'", "<INVALID>", "'OHM'", "'KWH'", 
                     "<INVALID>", "'si'", "'sino'", "'mientras'", "'para'", 
                     "'desde'", "'hasta'", "'paso'", "'regla'", "'retornar'", 
                     "'mostrar'", "'leer'", "'y'", "'o'", "'no'", "'verdadero'", 
                     "'falso'", "'mod'", "'+='", "'-='", "'=='", "'!='", 
                     "'<='", "'>='", "'<'", "'>'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "'{'", "'}'", "';'", "','", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "VAR", "CONST", "ENTERO", "DECIMAL", 
                      "PORCENTAJE", "BOOLEANO", "TEXTO", "VOLTAJE", "CORRIENTE", 
                      "POTENCIA", "RESISTENCIA", "ENERGIA", "TIEMPO", "UNIDAD_VOLTAJE", 
                      "UNIDAD_CORRIENTE", "UNIDAD_POTENCIA", "UNIDAD_RESISTENCIA", 
                      "UNIDAD_ENERGIA", "UNIDAD_TIEMPO", "SI", "SINO", "MIENTRAS", 
                      "PARA", "DESDE", "HASTA", "PASO", "REGLA", "RETORNAR", 
                      "MOSTRAR", "LEER", "Y", "O", "NO", "VERDADERO", "FALSO", 
                      "MOD", "MAS_ASIG", "MENOS_ASIG", "IGUAL", "DIFERENTE", 
                      "MENOR_IGUAL", "MAYOR_IGUAL", "MENOR", "MAYOR", "ASIG", 
                      "SUMA", "RESTA", "MULT", "DIV", "PAR_IZQ", "PAR_DER", 
                      "LLAVE_IZQ", "LLAVE_DER", "PUNTO_COMA", "COMA", "DOS_PUNTOS", 
                      "LIT_PORCENTAJE", "NUM_DECIMAL", "NUM_ENTERO", "CADENA", 
                      "ID", "COMENTARIO", "ESPACIO" ]

    RULE_programa = 0
    RULE_listaSentencias = 1
    RULE_sentencia = 2
    RULE_bloque = 3
    RULE_declaracion = 4
    RULE_inicializacion = 5
    RULE_tipo = 6
    RULE_asignacion = 7
    RULE_opAsignacion = 8
    RULE_expresion = 9
    RULE_conjuncion = 10
    RULE_negacion = 11
    RULE_igualdad = 12
    RULE_relacional = 13
    RULE_aritmetica = 14
    RULE_termino = 15
    RULE_unario = 16
    RULE_primario = 17
    RULE_literal = 18
    RULE_numero = 19
    RULE_llamada = 20
    RULE_argumentos = 21
    RULE_argumentosCola = 22
    RULE_seleccion = 23
    RULE_parteSino = 24
    RULE_colaSino = 25
    RULE_iteracion = 26
    RULE_pasoOpcional = 27
    RULE_regla = 28
    RULE_parametros = 29
    RULE_parametrosCola = 30
    RULE_parametro = 31
    RULE_tipoRetorno = 32
    RULE_retorno = 33
    RULE_valorRetorno = 34
    RULE_llamadaSentencia = 35
    RULE_entradaSalida = 36

    ruleNames =  [ "programa", "listaSentencias", "sentencia", "bloque", 
                   "declaracion", "inicializacion", "tipo", "asignacion", 
                   "opAsignacion", "expresion", "conjuncion", "negacion", 
                   "igualdad", "relacional", "aritmetica", "termino", "unario", 
                   "primario", "literal", "numero", "llamada", "argumentos", 
                   "argumentosCola", "seleccion", "parteSino", "colaSino", 
                   "iteracion", "pasoOpcional", "regla", "parametros", "parametrosCola", 
                   "parametro", "tipoRetorno", "retorno", "valorRetorno", 
                   "llamadaSentencia", "entradaSalida" ]

    EOF = Token.EOF
    VAR=1
    CONST=2
    ENTERO=3
    DECIMAL=4
    PORCENTAJE=5
    BOOLEANO=6
    TEXTO=7
    VOLTAJE=8
    CORRIENTE=9
    POTENCIA=10
    RESISTENCIA=11
    ENERGIA=12
    TIEMPO=13
    UNIDAD_VOLTAJE=14
    UNIDAD_CORRIENTE=15
    UNIDAD_POTENCIA=16
    UNIDAD_RESISTENCIA=17
    UNIDAD_ENERGIA=18
    UNIDAD_TIEMPO=19
    SI=20
    SINO=21
    MIENTRAS=22
    PARA=23
    DESDE=24
    HASTA=25
    PASO=26
    REGLA=27
    RETORNAR=28
    MOSTRAR=29
    LEER=30
    Y=31
    O=32
    NO=33
    VERDADERO=34
    FALSO=35
    MOD=36
    MAS_ASIG=37
    MENOS_ASIG=38
    IGUAL=39
    DIFERENTE=40
    MENOR_IGUAL=41
    MAYOR_IGUAL=42
    MENOR=43
    MAYOR=44
    ASIG=45
    SUMA=46
    RESTA=47
    MULT=48
    DIV=49
    PAR_IZQ=50
    PAR_DER=51
    LLAVE_IZQ=52
    LLAVE_DER=53
    PUNTO_COMA=54
    COMA=55
    DOS_PUNTOS=56
    LIT_PORCENTAJE=57
    NUM_DECIMAL=58
    NUM_ENTERO=59
    CADENA=60
    ID=61
    COMENTARIO=62
    ESPACIO=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaSentencias(self):
            return self.getTypedRuleContext(VoltioParser.ListaSentenciasContext,0)


        def EOF(self):
            return self.getToken(VoltioParser.EOF, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = VoltioParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.listaSentencias()
            self.state = 75
            self.match(VoltioParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaSentenciasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self):
            return self.getTypedRuleContext(VoltioParser.SentenciaContext,0)


        def listaSentencias(self):
            return self.getTypedRuleContext(VoltioParser.ListaSentenciasContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_listaSentencias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaSentencias" ):
                listener.enterListaSentencias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaSentencias" ):
                listener.exitListaSentencias(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaSentencias" ):
                return visitor.visitListaSentencias(self)
            else:
                return visitor.visitChildren(self)




    def listaSentencias(self):

        localctx = VoltioParser.ListaSentenciasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_listaSentencias)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 22, 23, 27, 28, 29, 30, 52, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.sentencia()
                self.state = 78
                self.listaSentencias()
                pass
            elif token in [-1, 53]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(VoltioParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(VoltioParser.AsignacionContext,0)


        def seleccion(self):
            return self.getTypedRuleContext(VoltioParser.SeleccionContext,0)


        def iteracion(self):
            return self.getTypedRuleContext(VoltioParser.IteracionContext,0)


        def regla(self):
            return self.getTypedRuleContext(VoltioParser.ReglaContext,0)


        def retorno(self):
            return self.getTypedRuleContext(VoltioParser.RetornoContext,0)


        def entradaSalida(self):
            return self.getTypedRuleContext(VoltioParser.EntradaSalidaContext,0)


        def llamadaSentencia(self):
            return self.getTypedRuleContext(VoltioParser.LlamadaSentenciaContext,0)


        def bloque(self):
            return self.getTypedRuleContext(VoltioParser.BloqueContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = VoltioParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentencia)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.seleccion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.iteracion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.regla()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
                self.retorno()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 89
                self.entradaSalida()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 90
                self.llamadaSentencia()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 91
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE_IZQ(self):
            return self.getToken(VoltioParser.LLAVE_IZQ, 0)

        def listaSentencias(self):
            return self.getTypedRuleContext(VoltioParser.ListaSentenciasContext,0)


        def LLAVE_DER(self):
            return self.getToken(VoltioParser.LLAVE_DER, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = VoltioParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(VoltioParser.LLAVE_IZQ)
            self.state = 95
            self.listaSentencias()
            self.state = 96
            self.match(VoltioParser.LLAVE_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(VoltioParser.VAR, 0)

        def ID(self):
            return self.getToken(VoltioParser.ID, 0)

        def DOS_PUNTOS(self):
            return self.getToken(VoltioParser.DOS_PUNTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(VoltioParser.TipoContext,0)


        def inicializacion(self):
            return self.getTypedRuleContext(VoltioParser.InicializacionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(VoltioParser.PUNTO_COMA, 0)

        def CONST(self):
            return self.getToken(VoltioParser.CONST, 0)

        def ASIG(self):
            return self.getToken(VoltioParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = VoltioParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracion)
        try:
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(VoltioParser.VAR)
                self.state = 99
                self.match(VoltioParser.ID)
                self.state = 100
                self.match(VoltioParser.DOS_PUNTOS)
                self.state = 101
                self.tipo()
                self.state = 102
                self.inicializacion()
                self.state = 103
                self.match(VoltioParser.PUNTO_COMA)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(VoltioParser.CONST)
                self.state = 106
                self.match(VoltioParser.ID)
                self.state = 107
                self.match(VoltioParser.DOS_PUNTOS)
                self.state = 108
                self.tipo()
                self.state = 109
                self.match(VoltioParser.ASIG)
                self.state = 110
                self.expresion(0)
                self.state = 111
                self.match(VoltioParser.PUNTO_COMA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(VoltioParser.ASIG, 0)

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacion" ):
                listener.enterInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacion" ):
                listener.exitInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = VoltioParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inicializacion)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.match(VoltioParser.ASIG)
                self.state = 116
                self.expresion(0)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(VoltioParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(VoltioParser.DECIMAL, 0)

        def PORCENTAJE(self):
            return self.getToken(VoltioParser.PORCENTAJE, 0)

        def BOOLEANO(self):
            return self.getToken(VoltioParser.BOOLEANO, 0)

        def TEXTO(self):
            return self.getToken(VoltioParser.TEXTO, 0)

        def VOLTAJE(self):
            return self.getToken(VoltioParser.VOLTAJE, 0)

        def MENOR(self):
            return self.getToken(VoltioParser.MENOR, 0)

        def UNIDAD_VOLTAJE(self):
            return self.getToken(VoltioParser.UNIDAD_VOLTAJE, 0)

        def MAYOR(self):
            return self.getToken(VoltioParser.MAYOR, 0)

        def CORRIENTE(self):
            return self.getToken(VoltioParser.CORRIENTE, 0)

        def UNIDAD_CORRIENTE(self):
            return self.getToken(VoltioParser.UNIDAD_CORRIENTE, 0)

        def POTENCIA(self):
            return self.getToken(VoltioParser.POTENCIA, 0)

        def UNIDAD_POTENCIA(self):
            return self.getToken(VoltioParser.UNIDAD_POTENCIA, 0)

        def RESISTENCIA(self):
            return self.getToken(VoltioParser.RESISTENCIA, 0)

        def UNIDAD_RESISTENCIA(self):
            return self.getToken(VoltioParser.UNIDAD_RESISTENCIA, 0)

        def ENERGIA(self):
            return self.getToken(VoltioParser.ENERGIA, 0)

        def UNIDAD_ENERGIA(self):
            return self.getToken(VoltioParser.UNIDAD_ENERGIA, 0)

        def TIEMPO(self):
            return self.getToken(VoltioParser.TIEMPO, 0)

        def UNIDAD_TIEMPO(self):
            return self.getToken(VoltioParser.UNIDAD_TIEMPO, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = VoltioParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipo)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(VoltioParser.ENTERO)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(VoltioParser.DECIMAL)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(VoltioParser.PORCENTAJE)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(VoltioParser.BOOLEANO)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.match(VoltioParser.TEXTO)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.match(VoltioParser.VOLTAJE)
                self.state = 126
                self.match(VoltioParser.MENOR)
                self.state = 127
                self.match(VoltioParser.UNIDAD_VOLTAJE)
                self.state = 128
                self.match(VoltioParser.MAYOR)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 7)
                self.state = 129
                self.match(VoltioParser.CORRIENTE)
                self.state = 130
                self.match(VoltioParser.MENOR)
                self.state = 131
                self.match(VoltioParser.UNIDAD_CORRIENTE)
                self.state = 132
                self.match(VoltioParser.MAYOR)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 8)
                self.state = 133
                self.match(VoltioParser.POTENCIA)
                self.state = 134
                self.match(VoltioParser.MENOR)
                self.state = 135
                self.match(VoltioParser.UNIDAD_POTENCIA)
                self.state = 136
                self.match(VoltioParser.MAYOR)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 9)
                self.state = 137
                self.match(VoltioParser.RESISTENCIA)
                self.state = 138
                self.match(VoltioParser.MENOR)
                self.state = 139
                self.match(VoltioParser.UNIDAD_RESISTENCIA)
                self.state = 140
                self.match(VoltioParser.MAYOR)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 10)
                self.state = 141
                self.match(VoltioParser.ENERGIA)
                self.state = 142
                self.match(VoltioParser.MENOR)
                self.state = 143
                self.match(VoltioParser.UNIDAD_ENERGIA)
                self.state = 144
                self.match(VoltioParser.MAYOR)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 11)
                self.state = 145
                self.match(VoltioParser.TIEMPO)
                self.state = 146
                self.match(VoltioParser.MENOR)
                self.state = 147
                self.match(VoltioParser.UNIDAD_TIEMPO)
                self.state = 148
                self.match(VoltioParser.MAYOR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VoltioParser.ID, 0)

        def opAsignacion(self):
            return self.getTypedRuleContext(VoltioParser.OpAsignacionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def PUNTO_COMA(self):
            return self.getToken(VoltioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = VoltioParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(VoltioParser.ID)
            self.state = 152
            self.opAsignacion()
            self.state = 153
            self.expresion(0)
            self.state = 154
            self.match(VoltioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpAsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(VoltioParser.ASIG, 0)

        def MAS_ASIG(self):
            return self.getToken(VoltioParser.MAS_ASIG, 0)

        def MENOS_ASIG(self):
            return self.getToken(VoltioParser.MENOS_ASIG, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_opAsignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpAsignacion" ):
                listener.enterOpAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpAsignacion" ):
                listener.exitOpAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpAsignacion" ):
                return visitor.visitOpAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def opAsignacion(self):

        localctx = VoltioParser.OpAsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_opAsignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35596688949248) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conjuncion(self):
            return self.getTypedRuleContext(VoltioParser.ConjuncionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def O(self):
            return self.getToken(VoltioParser.O, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VoltioParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.conjuncion(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VoltioParser.ExpresionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 161
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 162
                    self.match(VoltioParser.O)
                    self.state = 163
                    self.conjuncion(0) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConjuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negacion(self):
            return self.getTypedRuleContext(VoltioParser.NegacionContext,0)


        def conjuncion(self):
            return self.getTypedRuleContext(VoltioParser.ConjuncionContext,0)


        def Y(self):
            return self.getToken(VoltioParser.Y, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_conjuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjuncion" ):
                listener.enterConjuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjuncion" ):
                listener.exitConjuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjuncion" ):
                return visitor.visitConjuncion(self)
            else:
                return visitor.visitChildren(self)



    def conjuncion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VoltioParser.ConjuncionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_conjuncion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.negacion()
            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VoltioParser.ConjuncionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_conjuncion)
                    self.state = 172
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 173
                    self.match(VoltioParser.Y)
                    self.state = 174
                    self.negacion() 
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NegacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NO(self):
            return self.getToken(VoltioParser.NO, 0)

        def negacion(self):
            return self.getTypedRuleContext(VoltioParser.NegacionContext,0)


        def igualdad(self):
            return self.getTypedRuleContext(VoltioParser.IgualdadContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_negacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegacion" ):
                listener.enterNegacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegacion" ):
                listener.exitNegacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegacion" ):
                return visitor.visitNegacion(self)
            else:
                return visitor.visitChildren(self)




    def negacion(self):

        localctx = VoltioParser.NegacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_negacion)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(VoltioParser.NO)
                self.state = 181
                self.negacion()
                pass
            elif token in [34, 35, 47, 50, 57, 58, 59, 60, 61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.igualdad(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgualdadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacional(self):
            return self.getTypedRuleContext(VoltioParser.RelacionalContext,0)


        def igualdad(self):
            return self.getTypedRuleContext(VoltioParser.IgualdadContext,0)


        def IGUAL(self):
            return self.getToken(VoltioParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(VoltioParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_igualdad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgualdad" ):
                listener.enterIgualdad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgualdad" ):
                listener.exitIgualdad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgualdad" ):
                return visitor.visitIgualdad(self)
            else:
                return visitor.visitChildren(self)



    def igualdad(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VoltioParser.IgualdadContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_igualdad, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.relacional(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 194
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = VoltioParser.IgualdadContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_igualdad)
                        self.state = 188
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 189
                        self.match(VoltioParser.IGUAL)
                        self.state = 190
                        self.relacional(0)
                        pass

                    elif la_ == 2:
                        localctx = VoltioParser.IgualdadContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_igualdad)
                        self.state = 191
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 192
                        self.match(VoltioParser.DIFERENTE)
                        self.state = 193
                        self.relacional(0)
                        pass

             
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aritmetica(self):
            return self.getTypedRuleContext(VoltioParser.AritmeticaContext,0)


        def relacional(self):
            return self.getTypedRuleContext(VoltioParser.RelacionalContext,0)


        def MENOR(self):
            return self.getToken(VoltioParser.MENOR, 0)

        def MENOR_IGUAL(self):
            return self.getToken(VoltioParser.MENOR_IGUAL, 0)

        def MAYOR(self):
            return self.getToken(VoltioParser.MAYOR, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(VoltioParser.MAYOR_IGUAL, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)



    def relacional(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VoltioParser.RelacionalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_relacional, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.aritmetica(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 214
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = VoltioParser.RelacionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                        self.state = 202
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 203
                        self.match(VoltioParser.MENOR)
                        self.state = 204
                        self.aritmetica(0)
                        pass

                    elif la_ == 2:
                        localctx = VoltioParser.RelacionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                        self.state = 205
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 206
                        self.match(VoltioParser.MENOR_IGUAL)
                        self.state = 207
                        self.aritmetica(0)
                        pass

                    elif la_ == 3:
                        localctx = VoltioParser.RelacionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                        self.state = 208
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 209
                        self.match(VoltioParser.MAYOR)
                        self.state = 210
                        self.aritmetica(0)
                        pass

                    elif la_ == 4:
                        localctx = VoltioParser.RelacionalContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_relacional)
                        self.state = 211
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 212
                        self.match(VoltioParser.MAYOR_IGUAL)
                        self.state = 213
                        self.aritmetica(0)
                        pass

             
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(VoltioParser.TerminoContext,0)


        def aritmetica(self):
            return self.getTypedRuleContext(VoltioParser.AritmeticaContext,0)


        def SUMA(self):
            return self.getToken(VoltioParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(VoltioParser.RESTA, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_aritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAritmetica" ):
                listener.enterAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAritmetica" ):
                listener.exitAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAritmetica" ):
                return visitor.visitAritmetica(self)
            else:
                return visitor.visitChildren(self)



    def aritmetica(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VoltioParser.AritmeticaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_aritmetica, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 228
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = VoltioParser.AritmeticaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_aritmetica)
                        self.state = 222
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 223
                        self.match(VoltioParser.SUMA)
                        self.state = 224
                        self.termino(0)
                        pass

                    elif la_ == 2:
                        localctx = VoltioParser.AritmeticaContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_aritmetica)
                        self.state = 225
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 226
                        self.match(VoltioParser.RESTA)
                        self.state = 227
                        self.termino(0)
                        pass

             
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unario(self):
            return self.getTypedRuleContext(VoltioParser.UnarioContext,0)


        def termino(self):
            return self.getTypedRuleContext(VoltioParser.TerminoContext,0)


        def MULT(self):
            return self.getToken(VoltioParser.MULT, 0)

        def DIV(self):
            return self.getToken(VoltioParser.DIV, 0)

        def MOD(self):
            return self.getToken(VoltioParser.MOD, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VoltioParser.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.unario()
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 245
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = VoltioParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 236
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 237
                        self.match(VoltioParser.MULT)
                        self.state = 238
                        self.unario()
                        pass

                    elif la_ == 2:
                        localctx = VoltioParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 239
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 240
                        self.match(VoltioParser.DIV)
                        self.state = 241
                        self.unario()
                        pass

                    elif la_ == 3:
                        localctx = VoltioParser.TerminoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 242
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 243
                        self.match(VoltioParser.MOD)
                        self.state = 244
                        self.unario()
                        pass

             
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RESTA(self):
            return self.getToken(VoltioParser.RESTA, 0)

        def unario(self):
            return self.getTypedRuleContext(VoltioParser.UnarioContext,0)


        def primario(self):
            return self.getTypedRuleContext(VoltioParser.PrimarioContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_unario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnario" ):
                listener.enterUnario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnario" ):
                listener.exitUnario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnario" ):
                return visitor.visitUnario(self)
            else:
                return visitor.visitChildren(self)




    def unario(self):

        localctx = VoltioParser.UnarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unario)
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(VoltioParser.RESTA)
                self.state = 251
                self.unario()
                pass
            elif token in [34, 35, 50, 57, 58, 59, 60, 61]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.primario()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAR_IZQ(self):
            return self.getToken(VoltioParser.PAR_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def PAR_DER(self):
            return self.getToken(VoltioParser.PAR_DER, 0)

        def llamada(self):
            return self.getTypedRuleContext(VoltioParser.LlamadaContext,0)


        def literal(self):
            return self.getTypedRuleContext(VoltioParser.LiteralContext,0)


        def ID(self):
            return self.getToken(VoltioParser.ID, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_primario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimario" ):
                listener.enterPrimario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimario" ):
                listener.exitPrimario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimario" ):
                return visitor.visitPrimario(self)
            else:
                return visitor.visitChildren(self)




    def primario(self):

        localctx = VoltioParser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primario)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.match(VoltioParser.PAR_IZQ)
                self.state = 256
                self.expresion(0)
                self.state = 257
                self.match(VoltioParser.PAR_DER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.llamada()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
                self.match(VoltioParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numero(self):
            return self.getTypedRuleContext(VoltioParser.NumeroContext,0)


        def UNIDAD_VOLTAJE(self):
            return self.getToken(VoltioParser.UNIDAD_VOLTAJE, 0)

        def UNIDAD_CORRIENTE(self):
            return self.getToken(VoltioParser.UNIDAD_CORRIENTE, 0)

        def UNIDAD_POTENCIA(self):
            return self.getToken(VoltioParser.UNIDAD_POTENCIA, 0)

        def UNIDAD_RESISTENCIA(self):
            return self.getToken(VoltioParser.UNIDAD_RESISTENCIA, 0)

        def UNIDAD_ENERGIA(self):
            return self.getToken(VoltioParser.UNIDAD_ENERGIA, 0)

        def UNIDAD_TIEMPO(self):
            return self.getToken(VoltioParser.UNIDAD_TIEMPO, 0)

        def NUM_ENTERO(self):
            return self.getToken(VoltioParser.NUM_ENTERO, 0)

        def NUM_DECIMAL(self):
            return self.getToken(VoltioParser.NUM_DECIMAL, 0)

        def LIT_PORCENTAJE(self):
            return self.getToken(VoltioParser.LIT_PORCENTAJE, 0)

        def CADENA(self):
            return self.getToken(VoltioParser.CADENA, 0)

        def VERDADERO(self):
            return self.getToken(VoltioParser.VERDADERO, 0)

        def FALSO(self):
            return self.getToken(VoltioParser.FALSO, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = VoltioParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literal)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.numero()
                self.state = 265
                self.match(VoltioParser.UNIDAD_VOLTAJE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.numero()
                self.state = 268
                self.match(VoltioParser.UNIDAD_CORRIENTE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.numero()
                self.state = 271
                self.match(VoltioParser.UNIDAD_POTENCIA)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 273
                self.numero()
                self.state = 274
                self.match(VoltioParser.UNIDAD_RESISTENCIA)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 276
                self.numero()
                self.state = 277
                self.match(VoltioParser.UNIDAD_ENERGIA)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 279
                self.numero()
                self.state = 280
                self.match(VoltioParser.UNIDAD_TIEMPO)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 282
                self.match(VoltioParser.NUM_ENTERO)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 283
                self.match(VoltioParser.NUM_DECIMAL)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 284
                self.match(VoltioParser.LIT_PORCENTAJE)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 285
                self.match(VoltioParser.CADENA)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 286
                self.match(VoltioParser.VERDADERO)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 287
                self.match(VoltioParser.FALSO)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumeroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_ENTERO(self):
            return self.getToken(VoltioParser.NUM_ENTERO, 0)

        def NUM_DECIMAL(self):
            return self.getToken(VoltioParser.NUM_DECIMAL, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_numero

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)




    def numero(self):

        localctx = VoltioParser.NumeroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_numero)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            _la = self._input.LA(1)
            if not(_la==58 or _la==59):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VoltioParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(VoltioParser.PAR_IZQ, 0)

        def argumentos(self):
            return self.getTypedRuleContext(VoltioParser.ArgumentosContext,0)


        def PAR_DER(self):
            return self.getToken(VoltioParser.PAR_DER, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = VoltioParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(VoltioParser.ID)
            self.state = 293
            self.match(VoltioParser.PAR_IZQ)
            self.state = 294
            self.argumentos()
            self.state = 295
            self.match(VoltioParser.PAR_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def argumentosCola(self):
            return self.getTypedRuleContext(VoltioParser.ArgumentosColaContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = VoltioParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_argumentos)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 35, 47, 50, 57, 58, 59, 60, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.expresion(0)
                self.state = 298
                self.argumentosCola()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosColaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(VoltioParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def argumentosCola(self):
            return self.getTypedRuleContext(VoltioParser.ArgumentosColaContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_argumentosCola

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentosCola" ):
                listener.enterArgumentosCola(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentosCola" ):
                listener.exitArgumentosCola(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentosCola" ):
                return visitor.visitArgumentosCola(self)
            else:
                return visitor.visitChildren(self)




    def argumentosCola(self):

        localctx = VoltioParser.ArgumentosColaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_argumentosCola)
        try:
            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(VoltioParser.COMA)
                self.state = 304
                self.expresion(0)
                self.state = 305
                self.argumentosCola()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeleccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(VoltioParser.SI, 0)

        def PAR_IZQ(self):
            return self.getToken(VoltioParser.PAR_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def PAR_DER(self):
            return self.getToken(VoltioParser.PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(VoltioParser.BloqueContext,0)


        def parteSino(self):
            return self.getTypedRuleContext(VoltioParser.ParteSinoContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_seleccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeleccion" ):
                listener.enterSeleccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeleccion" ):
                listener.exitSeleccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeleccion" ):
                return visitor.visitSeleccion(self)
            else:
                return visitor.visitChildren(self)




    def seleccion(self):

        localctx = VoltioParser.SeleccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_seleccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(VoltioParser.SI)
            self.state = 311
            self.match(VoltioParser.PAR_IZQ)
            self.state = 312
            self.expresion(0)
            self.state = 313
            self.match(VoltioParser.PAR_DER)
            self.state = 314
            self.bloque()
            self.state = 315
            self.parteSino()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParteSinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(VoltioParser.SINO, 0)

        def colaSino(self):
            return self.getTypedRuleContext(VoltioParser.ColaSinoContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_parteSino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParteSino" ):
                listener.enterParteSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParteSino" ):
                listener.exitParteSino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParteSino" ):
                return visitor.visitParteSino(self)
            else:
                return visitor.visitChildren(self)




    def parteSino(self):

        localctx = VoltioParser.ParteSinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parteSino)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(VoltioParser.SINO)
                self.state = 318
                self.colaSino()
                pass
            elif token in [-1, 1, 2, 20, 22, 23, 27, 28, 29, 30, 52, 53, 61]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColaSinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seleccion(self):
            return self.getTypedRuleContext(VoltioParser.SeleccionContext,0)


        def bloque(self):
            return self.getTypedRuleContext(VoltioParser.BloqueContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_colaSino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColaSino" ):
                listener.enterColaSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColaSino" ):
                listener.exitColaSino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColaSino" ):
                return visitor.visitColaSino(self)
            else:
                return visitor.visitChildren(self)




    def colaSino(self):

        localctx = VoltioParser.ColaSinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_colaSino)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.seleccion()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.bloque()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IteracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(VoltioParser.MIENTRAS, 0)

        def PAR_IZQ(self):
            return self.getToken(VoltioParser.PAR_IZQ, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VoltioParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(VoltioParser.ExpresionContext,i)


        def PAR_DER(self):
            return self.getToken(VoltioParser.PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(VoltioParser.BloqueContext,0)


        def PARA(self):
            return self.getToken(VoltioParser.PARA, 0)

        def ID(self):
            return self.getToken(VoltioParser.ID, 0)

        def DESDE(self):
            return self.getToken(VoltioParser.DESDE, 0)

        def HASTA(self):
            return self.getToken(VoltioParser.HASTA, 0)

        def pasoOpcional(self):
            return self.getTypedRuleContext(VoltioParser.PasoOpcionalContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_iteracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIteracion" ):
                listener.enterIteracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIteracion" ):
                listener.exitIteracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIteracion" ):
                return visitor.visitIteracion(self)
            else:
                return visitor.visitChildren(self)




    def iteracion(self):

        localctx = VoltioParser.IteracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_iteracion)
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(VoltioParser.MIENTRAS)
                self.state = 327
                self.match(VoltioParser.PAR_IZQ)
                self.state = 328
                self.expresion(0)
                self.state = 329
                self.match(VoltioParser.PAR_DER)
                self.state = 330
                self.bloque()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(VoltioParser.PARA)
                self.state = 333
                self.match(VoltioParser.ID)
                self.state = 334
                self.match(VoltioParser.DESDE)
                self.state = 335
                self.expresion(0)
                self.state = 336
                self.match(VoltioParser.HASTA)
                self.state = 337
                self.expresion(0)
                self.state = 338
                self.pasoOpcional()
                self.state = 339
                self.bloque()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PasoOpcionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASO(self):
            return self.getToken(VoltioParser.PASO, 0)

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_pasoOpcional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPasoOpcional" ):
                listener.enterPasoOpcional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPasoOpcional" ):
                listener.exitPasoOpcional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPasoOpcional" ):
                return visitor.visitPasoOpcional(self)
            else:
                return visitor.visitChildren(self)




    def pasoOpcional(self):

        localctx = VoltioParser.PasoOpcionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_pasoOpcional)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(VoltioParser.PASO)
                self.state = 344
                self.expresion(0)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReglaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGLA(self):
            return self.getToken(VoltioParser.REGLA, 0)

        def ID(self):
            return self.getToken(VoltioParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(VoltioParser.PAR_IZQ, 0)

        def parametros(self):
            return self.getTypedRuleContext(VoltioParser.ParametrosContext,0)


        def PAR_DER(self):
            return self.getToken(VoltioParser.PAR_DER, 0)

        def tipoRetorno(self):
            return self.getTypedRuleContext(VoltioParser.TipoRetornoContext,0)


        def bloque(self):
            return self.getTypedRuleContext(VoltioParser.BloqueContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_regla

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegla" ):
                listener.enterRegla(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegla" ):
                listener.exitRegla(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegla" ):
                return visitor.visitRegla(self)
            else:
                return visitor.visitChildren(self)




    def regla(self):

        localctx = VoltioParser.ReglaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_regla)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(VoltioParser.REGLA)
            self.state = 349
            self.match(VoltioParser.ID)
            self.state = 350
            self.match(VoltioParser.PAR_IZQ)
            self.state = 351
            self.parametros()
            self.state = 352
            self.match(VoltioParser.PAR_DER)
            self.state = 353
            self.tipoRetorno()
            self.state = 354
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self):
            return self.getTypedRuleContext(VoltioParser.ParametroContext,0)


        def parametrosCola(self):
            return self.getTypedRuleContext(VoltioParser.ParametrosColaContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = VoltioParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_parametros)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.parametro()
                self.state = 357
                self.parametrosCola()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosColaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(VoltioParser.COMA, 0)

        def parametro(self):
            return self.getTypedRuleContext(VoltioParser.ParametroContext,0)


        def parametrosCola(self):
            return self.getTypedRuleContext(VoltioParser.ParametrosColaContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_parametrosCola

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosCola" ):
                listener.enterParametrosCola(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosCola" ):
                listener.exitParametrosCola(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametrosCola" ):
                return visitor.visitParametrosCola(self)
            else:
                return visitor.visitChildren(self)




    def parametrosCola(self):

        localctx = VoltioParser.ParametrosColaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parametrosCola)
        try:
            self.state = 367
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(VoltioParser.COMA)
                self.state = 363
                self.parametro()
                self.state = 364
                self.parametrosCola()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(VoltioParser.ID, 0)

        def DOS_PUNTOS(self):
            return self.getToken(VoltioParser.DOS_PUNTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(VoltioParser.TipoContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = VoltioParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(VoltioParser.ID)
            self.state = 370
            self.match(VoltioParser.DOS_PUNTOS)
            self.state = 371
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoRetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOS_PUNTOS(self):
            return self.getToken(VoltioParser.DOS_PUNTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(VoltioParser.TipoContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_tipoRetorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoRetorno" ):
                listener.enterTipoRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoRetorno" ):
                listener.exitTipoRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoRetorno" ):
                return visitor.visitTipoRetorno(self)
            else:
                return visitor.visitChildren(self)




    def tipoRetorno(self):

        localctx = VoltioParser.TipoRetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_tipoRetorno)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [56]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(VoltioParser.DOS_PUNTOS)
                self.state = 374
                self.tipo()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(VoltioParser.RETORNAR, 0)

        def valorRetorno(self):
            return self.getTypedRuleContext(VoltioParser.ValorRetornoContext,0)


        def PUNTO_COMA(self):
            return self.getToken(VoltioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = VoltioParser.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(VoltioParser.RETORNAR)
            self.state = 379
            self.valorRetorno()
            self.state = 380
            self.match(VoltioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorRetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def getRuleIndex(self):
            return VoltioParser.RULE_valorRetorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValorRetorno" ):
                listener.enterValorRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValorRetorno" ):
                listener.exitValorRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValorRetorno" ):
                return visitor.visitValorRetorno(self)
            else:
                return visitor.visitChildren(self)




    def valorRetorno(self):

        localctx = VoltioParser.ValorRetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_valorRetorno)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34, 35, 47, 50, 57, 58, 59, 60, 61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.expresion(0)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaSentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def llamada(self):
            return self.getTypedRuleContext(VoltioParser.LlamadaContext,0)


        def PUNTO_COMA(self):
            return self.getToken(VoltioParser.PUNTO_COMA, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_llamadaSentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaSentencia" ):
                listener.enterLlamadaSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaSentencia" ):
                listener.exitLlamadaSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaSentencia" ):
                return visitor.visitLlamadaSentencia(self)
            else:
                return visitor.visitChildren(self)




    def llamadaSentencia(self):

        localctx = VoltioParser.LlamadaSentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_llamadaSentencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.llamada()
            self.state = 387
            self.match(VoltioParser.PUNTO_COMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaSalidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(VoltioParser.MOSTRAR, 0)

        def PAR_IZQ(self):
            return self.getToken(VoltioParser.PAR_IZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(VoltioParser.ExpresionContext,0)


        def argumentosCola(self):
            return self.getTypedRuleContext(VoltioParser.ArgumentosColaContext,0)


        def PAR_DER(self):
            return self.getToken(VoltioParser.PAR_DER, 0)

        def PUNTO_COMA(self):
            return self.getToken(VoltioParser.PUNTO_COMA, 0)

        def LEER(self):
            return self.getToken(VoltioParser.LEER, 0)

        def ID(self):
            return self.getToken(VoltioParser.ID, 0)

        def getRuleIndex(self):
            return VoltioParser.RULE_entradaSalida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntradaSalida" ):
                listener.enterEntradaSalida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntradaSalida" ):
                listener.exitEntradaSalida(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntradaSalida" ):
                return visitor.visitEntradaSalida(self)
            else:
                return visitor.visitChildren(self)




    def entradaSalida(self):

        localctx = VoltioParser.EntradaSalidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_entradaSalida)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(VoltioParser.MOSTRAR)
                self.state = 390
                self.match(VoltioParser.PAR_IZQ)
                self.state = 391
                self.expresion(0)
                self.state = 392
                self.argumentosCola()
                self.state = 393
                self.match(VoltioParser.PAR_DER)
                self.state = 394
                self.match(VoltioParser.PUNTO_COMA)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.match(VoltioParser.LEER)
                self.state = 397
                self.match(VoltioParser.PAR_IZQ)
                self.state = 398
                self.match(VoltioParser.ID)
                self.state = 399
                self.match(VoltioParser.PAR_DER)
                self.state = 400
                self.match(VoltioParser.PUNTO_COMA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expresion_sempred
        self._predicates[10] = self.conjuncion_sempred
        self._predicates[12] = self.igualdad_sempred
        self._predicates[13] = self.relacional_sempred
        self._predicates[14] = self.aritmetica_sempred
        self._predicates[15] = self.termino_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def conjuncion_sempred(self, localctx:ConjuncionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def igualdad_sempred(self, localctx:IgualdadContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def relacional_sempred(self, localctx:RelacionalContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def aritmetica_sempred(self, localctx:AritmeticaContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def termino_sempred(self, localctx:TerminoContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         




