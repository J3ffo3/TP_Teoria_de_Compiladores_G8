grammar MarkovLang;

// ==========================================
// REGLAS DEL PARSER
// ==========================================

// ---------- PUNTO DE ENTRADA
program : globalConfig* statement* EOF ;

// ---------- CONFIGURACIÓN GLOBAL
globalConfig : seedStmt ;
seedStmt     : SEED INT_LIT SEMI ;

// ---------- SENTENCIAS
statement
    : varDecl
    | assignment
    | ifStmt
    | whileStmt
    | printStmt
    | chainDecl
    | simulateStmt
    | stationaryStmt
    | block
    ;

// ---------- DECLARACIÓN DE VARIABLES (var x : int;)
varDecl : VAR ID COLON typeSpec SEMI ;

// ---------- TIPOS DE DATOS
typeSpec
    : INT_TYPE
    | FLOAT_TYPE
    | BOOL_TYPE
    | STRING_TYPE
    | STATE_TYPE
    ;

// ---------- ASIGNACIÓN (x := expresion;)
assignment : ID ASSIGN expression SEMI ;

// ---------- ESTRUCTURA IF-THEN-ELSE
ifStmt
    : IF expression THEN block
    | IF expression THEN block ELSE block
    ;

// ---------- ESTRUCTURA WHILE-DO
whileStmt : WHILE expression DO block ;

// ---------- IMPRESIÓN
printStmt : PRINT LPAREN expression RPAREN SEMI ;

// ---------- BLOQUE DE SENTENCIAS { stmt* }
block : LBRACE statement* RBRACE ;

// ---------- DOMINIO: CADENAS DE MARKOV
chainDecl      : CHAIN ID DO LBRACE chainBody* RBRACE ;
chainBody      : stateDecl | transitionStmt ;
stateDecl      : STATE ID SEMI ;
transitionStmt : TRANSITION ID ARROW ID LPAREN expression RPAREN SEMI ;

simulateStmt   : SIMULATE LPAREN ID COMMA ID COMMA expression RPAREN SEMI ;
stationaryStmt : STATIONARY LPAREN ID RPAREN SEMI ;

// ---------- EXPRESIONES
// Precedencia estratificada (diapositivas de clase Semana 5 y 6)
expression : relationalExpr ;

relationalExpr
    : relationalExpr RELOP additiveExpr
    | additiveExpr
    ;

additiveExpr
    : additiveExpr ADDOP multiplicativeExpr
    | multiplicativeExpr
    ;

multiplicativeExpr
    : multiplicativeExpr MULOP factor
    | factor
    ;

factor
    : INT_LIT
    | FLOAT_LIT
    | STRING_LIT
    | TRUE
    | FALSE
    | ID
    | LPAREN expression RPAREN
    ;

// ==========================================
// REGLAS DEL LEXER
// ==========================================

// ---------- PALABRAS CLAVE (antes que ID)
VAR        : 'var' ;
SEED       : 'seed' ;
CHAIN      : 'chain' ;
STATE      : 'state' ;
TRANSITION : 'transition' ;
SIMULATE   : 'simulate' ;
STATIONARY : 'stationary' ;
IF         : 'if' ;
THEN       : 'then' ;
ELSE       : 'else' ;
WHILE      : 'while' ;
DO         : 'do' ;
PRINT      : 'print' ;

// ---------- TIPOS DE DATOS
INT_TYPE    : 'int' ;
FLOAT_TYPE  : 'float' ;
BOOL_TYPE   : 'bool' ;
STRING_TYPE : 'string' ;
STATE_TYPE  : 'state' ;

// ---------- LITERALES BOOLEANOS
TRUE  : 'true' ;
FALSE : 'false' ;

// ---------- OPERADORES RELACIONALES
RELOP : '==' | '!=' | '<=' | '>=' | '<' | '>' ;

// ---------- OPERADORES ARITMÉTICOS
ADDOP : '+' | '-' ;
MULOP : '*' | '/' | 'MOD' | 'DIV' ;

// ---------- ASIGNACIÓN Y FLECHA
ASSIGN : ':=' ;
ARROW  : '->' ;

// ---------- DELIMITADORES
COLON  : ':' ;
SEMI   : ';' ;
COMMA  : ',' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;

// ---------- LITERALES NUMÉRICOS
FLOAT_LIT : [0-9]+ '.' [0-9]+ ;
INT_LIT   : [0-9]+ ;

// ---------- LITERAL DE CADENA
STRING_LIT : '"' ~["\r\n]* '"' ;

// ---------- IDENTIFICADORES
ID : [a-zA-Z_] [a-zA-Z0-9_]* ;

// ---------- IGNORADOS
WS            : [ \t\r\n]+ -> skip ;
LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
