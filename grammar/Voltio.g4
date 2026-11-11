// Voltio: Lenguaje de Dominio Específico para dimensionamiento eléctrico y circuitos.
// Teoría de Compiladores (1ACC0218) - Hito 2 (Forma estándar estricta L1 a L6).
grammar Voltio;

// ============================================================================
// ANALIZADOR SINTÁCTICO
// ============================================================================

// --- Estructura general -------------------------------------------------------
programa
    : listaSentencias EOF
    ;

listaSentencias
    : sentencia listaSentencias
    |
    ;

sentencia
    : declaracion
    | asignacion
    | seleccion
    | iteracion
    | regla
    | retorno
    | entradaSalida
    | llamadaSentencia
    | bloque
    ;

bloque
    : LLAVE_IZQ listaSentencias LLAVE_DER
    ;

// --- G1. Declaración de variables y constantes --------------------------------
declaracion
    : VAR ID DOS_PUNTOS tipo inicializacion PUNTO_COMA
    | CONST ID DOS_PUNTOS tipo ASIG expresion PUNTO_COMA
    ;

inicializacion
    : ASIG expresion
    |
    ;

tipo
    : ENTERO
    | DECIMAL
    | PORCENTAJE
    | BOOLEANO
    | TEXTO
    | VOLTAJE MENOR UNIDAD_VOLTAJE MAYOR
    | CORRIENTE MENOR UNIDAD_CORRIENTE MAYOR
    | POTENCIA MENOR UNIDAD_POTENCIA MAYOR
    | RESISTENCIA MENOR UNIDAD_RESISTENCIA MAYOR
    | ENERGIA MENOR UNIDAD_ENERGIA MAYOR
    | TIEMPO MENOR UNIDAD_TIEMPO MAYOR
    ;

// --- G2. Asignación -------------------------------------------------------------
asignacion
    : ID opAsignacion expresion PUNTO_COMA
    ;

opAsignacion
    : ASIG
    | MAS_ASIG
    | MENOS_ASIG
    ;

// --- G3. Expresiones (Precedencia por niveles) --------------------------------
expresion
    : expresion O conjuncion
    | conjuncion
    ;

conjuncion
    : conjuncion Y negacion
    | negacion
    ;

negacion
    : NO negacion
    | igualdad
    ;

igualdad
    : igualdad IGUAL relacional
    | igualdad DIFERENTE relacional
    | relacional
    ;

relacional
    : relacional MENOR aritmetica
    | relacional MENOR_IGUAL aritmetica
    | relacional MAYOR aritmetica
    | relacional MAYOR_IGUAL aritmetica
    | aritmetica
    ;

aritmetica
    : aritmetica SUMA termino
    | aritmetica RESTA termino
    | termino
    ;

termino
    : termino MULT unario
    | termino DIV unario
    | termino MOD unario
    | unario
    ;

unario
    : RESTA unario
    | primario
    ;

primario
    : PAR_IZQ expresion PAR_DER
    | llamada
    | literal
    | ID
    ;

literal
    : numero UNIDAD_VOLTAJE
    | numero UNIDAD_CORRIENTE
    | numero UNIDAD_POTENCIA
    | numero UNIDAD_RESISTENCIA
    | numero UNIDAD_ENERGIA
    | numero UNIDAD_TIEMPO
    | NUM_ENTERO
    | NUM_DECIMAL
    | LIT_PORCENTAJE
    | CADENA
    | VERDADERO
    | FALSO
    ;

numero
    : NUM_ENTERO
    | NUM_DECIMAL
    ;

llamada
    : ID PAR_IZQ argumentos PAR_DER
    ;

argumentos
    : expresion argumentosCola
    |
    ;

argumentosCola
    : COMA expresion argumentosCola
    |
    ;

// --- G4. Sentencias selectivas ------------------------------------------------
seleccion
    : SI PAR_IZQ expresion PAR_DER bloque parteSino
    ;

parteSino
    : SINO colaSino
    |
    ;

colaSino
    : seleccion
    | bloque
    ;

// --- G5. Sentencias iterativas --------------------------------------------------
iteracion
    : MIENTRAS PAR_IZQ expresion PAR_DER bloque
    | PARA ID DESDE expresion HASTA expresion pasoOpcional bloque
    ;

pasoOpcional
    : PASO expresion
    |
    ;

// --- G6. Reglas (funciones), retorno y llamadas -------------------------------
regla
    : REGLA ID PAR_IZQ parametros PAR_DER tipoRetorno bloque
    ;

parametros
    : parametro parametrosCola
    |
    ;

parametrosCola
    : COMA parametro parametrosCola
    |
    ;

parametro
    : ID DOS_PUNTOS tipo
    ;

tipoRetorno
    : DOS_PUNTOS tipo
    |
    ;

retorno
    : RETORNAR valorRetorno PUNTO_COMA
    ;

valorRetorno
    : expresion
    |
    ;

llamadaSentencia
    : llamada PUNTO_COMA
    ;

// --- G7. Entrada y salida --------------------------------------------------------
entradaSalida
    : MOSTRAR PAR_IZQ expresion argumentosCola PAR_DER PUNTO_COMA
    | LEER PAR_IZQ ID PAR_DER PUNTO_COMA
    ;

// ============================================================================
// ANALIZADOR LÉXICO
// ============================================================================

// --- Palabras reservadas (declaradas antes de ID para prioridad) ----------------
VAR              : 'var' ;
CONST            : 'const' ;
ENTERO           : 'entero' ;
DECIMAL          : 'decimal' ;
PORCENTAJE       : 'porcentaje' ;
BOOLEANO         : 'booleano' ;
TEXTO            : 'texto' ;

// Palabras de tipos de dominio
VOLTAJE          : 'voltaje' ;
CORRIENTE        : 'corriente' ;
POTENCIA         : 'potencia' ;
RESISTENCIA      : 'resistencia' ;
ENERGIA          : 'energia' ;
TIEMPO           : 'tiempo' ;

// Unidades del dominio
UNIDAD_VOLTAJE     : 'V' ;
UNIDAD_CORRIENTE   : 'A' ;
UNIDAD_POTENCIA    : 'W' | 'KW' ;
UNIDAD_RESISTENCIA : 'OHM' ;
UNIDAD_ENERGIA     : 'KWH' ;
UNIDAD_TIEMPO      : 'H' | 'S' ;

// Palabras de control y flujo
SI               : 'si' ;
SINO             : 'sino' ;
MIENTRAS         : 'mientras' ;
PARA             : 'para' ;
DESDE            : 'desde' ;
HASTA            : 'hasta' ;
PASO             : 'paso' ;
REGLA            : 'regla' ;
RETORNAR         : 'retornar' ;
MOSTRAR          : 'mostrar' ;
LEER             : 'leer' ;
Y                : 'y' ;
O                : 'o' ;
NO               : 'no' ;
VERDADERO        : 'verdadero' ;
FALSO            : 'falso' ;
MOD              : 'mod' ;

// --- Operadores ---
MAS_ASIG         : '+=' ;
MENOS_ASIG       : '-=' ;
IGUAL            : '==' ;
DIFERENTE        : '!=' ;
MENOR_IGUAL      : '<=' ;
MAYOR_IGUAL      : '>=' ;
MENOR            : '<' ;
MAYOR            : '>' ;
ASIG             : '=' ;
SUMA             : '+' ;
RESTA            : '-' ;
MULT             : '*' ;
DIV              : '/' ;

// --- Delimitadores ---
PAR_IZQ          : '(' ;
PAR_DER          : ')' ;
LLAVE_IZQ        : '{' ;
LLAVE_DER        : '}' ;
PUNTO_COMA       : ';' ;
COMA             : ',' ;
DOS_PUNTOS       : ':' ;

// --- Literales ---
LIT_PORCENTAJE
    : DIGITOS '%'
    | DIGITOS '.' DIGITOS '%'
    ;
NUM_DECIMAL      : DIGITOS '.' DIGITOS ;
NUM_ENTERO       : DIGITOS ;
CADENA           : '"' CADENA_COLA '"' ;

// --- Identificadores ---
ID               : LETRA ID_COLA ;

// --- Elementos ignorados ---
COMENTARIO       : '//' COMENTARIO_COLA -> skip ;
ESPACIO          : BLANCO ESPACIO_COLA -> skip ;

// --- Fragments recursivos (Sin usar * ni + para cumplir L3) --------------------
fragment DIGITOS
    : DIGITO DIGITOS_COLA
    ;
fragment DIGITOS_COLA
    : DIGITO DIGITOS_COLA
    |
    ;
fragment ID_COLA
    : LETRA ID_COLA
    | DIGITO ID_COLA
    |
    ;
fragment CADENA_COLA
    : CARACTER_CADENA CADENA_COLA
    |
    ;
fragment CARACTER_CADENA
    : ~["\\\r\n]
    | '\\' ~[\r\n]
    ;
fragment COMENTARIO_COLA
    : ~[\r\n] COMENTARIO_COLA
    |
    ;
fragment ESPACIO_COLA
    : BLANCO ESPACIO_COLA
    |
    ;
fragment BLANCO : [ \t\r\n] ;
fragment DIGITO : [0-9] ;
fragment LETRA  : [a-zA-Z_áéíóúÁÉÍÓÚñÑ] ;
