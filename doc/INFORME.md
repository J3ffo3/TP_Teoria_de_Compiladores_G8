# Informe Técnico - Trabajo Parcial (Hito 1)
## MarkovLang: Lenguaje de Dominio Específico para Modelado, Validación y Compilación de Cadenas de Markov

---

### Datos del Proyecto
* **Curso:** Teoría de Compiladores (Ciclo 2026-2)
* **Docente:** Prof. José Luis Soncco Álvarez
* **Grupo:** Grupo 8
* **Hito de Entrega:** Hito 1 - Trabajo Parcial (Semana 7)
* **Carrera:** Ciencia de la Computación

---

## 1. Problemática y Motivación

Las Cadenas de Markov de Tiempo Discreto (DTMC) son un modelo matemático utilizado para describir procesos estocásticos donde la probabilidad de transición al siguiente estado depende exclusivamente del estado presente. Aunque su aplicación es frecuente en áreas como simulación de colas, análisis de confiabilidad, modelos meteorológicos y economía, **no existe en la actualidad un lenguaje de dominio específico (DSL) enfocado directamente en su definición y validación estática**.

### 1.1 Limitaciones del Flujo Tradicional
Cuando un programador implementa cadenas de Markov en lenguajes de propósito general o de bajo nivel como C o C++, el proceso resulta repetitivo y propenso a errores:
1. **Pérdida de abstracción semántica:** Los estados conceptuales del sistema (por ejemplo `Sunny`, `Rainy`, `Bull`, `Bear`) deben mapearse manualmente a números enteros (`0, 1, ...`) como índices de una matriz bidimensional, dificultando la lectura y mantenimiento del código.
2. **Ausencia de validación estocástica estática:** Los compiladores tradicionales no pueden validar que la suma de probabilidades salientes de cada fila sea estrictamente igual a $1.0$. Si el usuario comete un error tipográfico en un valor decimal o descuida una transición, el programa compila con éxito pero genera resultados matemáticamente inconsistentes en tiempo de ejecución.
3. **Reimplementación de algoritmos de simulación:** Tareas comunes como la simulación de Monte Carlo mediante la función de distribución acumulada (CDF) o el cálculo de la distribución estacionaria requieren escribir código repetitivo de manejo de matrices y generadores de números aleatorios.

### 1.2 Justificación de Compilación a Bajo Nivel (C)
Para resolver esta problemática, **MarkovLang** introduce una sintaxis declarativa concisa que permite al usuario definir estados y transiciones directamente por su nombre simbólico. El compilador se encarga de dos tareas fundamentales:
* **Verificación estática estricta:** Comprueba en tiempo de compilación tanto las reglas habituales del lenguaje (tipado, declaración e inicialización de variables) como los axiomas probabilísticos (propiedad estocástica).
* **Compilación a C:** Simplifica y traduce el modelo de alto nivel a un programa ejecutable en **C puro**, generando automáticamente tipos enumerados (`enum`), matrices estáticas de adyacencia (`float P[N][N]`), rutinas optimizadas de simulación Monte Carlo y algoritmos de potenciación matricial.

---

## 2. Objetivos

### 2.1 Objetivo General
Diseñar e implementar el analizador léxico, sintáctico, semántico y generador de código inicial del lenguaje **MarkovLang** utilizando **ANTLR4** y Python 3, aplicando los conceptos de gramáticas libres de contexto, tablas de símbolos y derivaciones formales desarrollados en la Unidad 1 del curso.

### 2.2 Objetivos Específicos
1. Formalizar la gramática libre de contexto de MarkovLang, resolviendo ambigüedades en expresiones aritméticas y estructuras de control mediante una jerarquía estratificada.
2. Construir la especificación léxica formal definiendo los tokens y expresiones regulares correspondientes.
3. Validar las producciones sintácticas mediante derivaciones más a la izquierda ($\Rightarrow_{lm}$) siguiendo la convención formal vista en clase.
4. Implementar un analizador semántico basado en el patrón *Visitor* con tabla de símbolos de ámbitos estáticos (`_scope_stack`), detectando errores de tipado, uso de variables no inicializadas, división entre cero con constantes y violación de la propiedad estocástica.
5. Diseñar el backend que traduzca el AST validado a código ejecutable en C.

---

## 3. Descripción de Construcciones del Lenguaje

El lenguaje incluye construcciones clásicas de programación estructurada junto con primitivas dedicadas al modelado probabilístico. A continuación se detallan 5 ejemplos de cada construcción:

### 3.1 Declaración de Variables
Sigue la sintaxis `var <identificador> : <tipo>;` utilizada en los ejemplos del curso.
* `var pasos : int;`
* `var umbral : float;`
* `var convergencia : bool;`
* `var etiqueta : string;`
* `var estado_actual : state;`

### 3.2 Sentencias de Asignación
Utiliza el operador de asignación destructiva `:=` y valida compatibilidad de tipos.
* `pasos := 50;`
* `umbral := 0.05;`
* `convergencia := true;`
* `etiqueta := "Modelo de Mercado";`
* `pasos := pasos + 10;`

### 3.3 Expresiones Aritméticas y Lógicas
Soportan operadores relacionales, sumas, restas, productos, divisiones (`/`, `DIV`, `MOD`) y agrupación por paréntesis respetando precedencia.
* `x + y * 2`
* `(pasos - 5) / (2 + 1)`
* `iteraciones < 100`
* `contador MOD 2 == 0`
* `probabilidad >= 0.0`

### 3.4 Sentencias Selectivas (`if-then-else`)
Permiten bifurcaciones condicionales basadas en expresiones booleanas.
* `if convergencia then { print("Simulacion completa"); }`
* `if pasos > 10 then { pasos := pasos - 1; } else { pasos := 0; }`
* `if contador MOD 2 == 0 then { print("Par"); } else { print("Impar"); }`
* `if umbral < 0.01 then { convergencia := true; }`
* `if activo then { contador := contador + 1; }`

### 3.5 Sentencias Iterativas (`while-do`)
Ejecutan un bloque de instrucciones de manera repetitiva mientras se cumpla la condición.
* `while contador < 5 do { contador := contador + 1; }`
* `while umbral > 0.001 do { umbral := umbral / 2.0; }`
* `while activo do { print("Ejecutando paso"); }`
* `while pasos > 0 do { pasos := pasos - 1; }`
* `while i < 10 do { print(i); i := i + 1; }`

### 3.6 Primitivas de Cadenas de Markov
Instrucciones específicas para declarar la cadena, definir sus estados y transiciones, e invocar operaciones de simulación o cálculo estacionario.
* `chain Clima do { state Soleado; state Lluvioso; }`
* `transition Soleado -> Lluvioso (0.3);`
* `transition Lluvioso -> Soleado (0.5);`
* `simulate(Clima, Soleado, 50);`
* `stationary(Clima);`

---

## 4. Analizador Léxico

La siguiente tabla resume los componentes léxicos implementados en ANTLR4:

| Token | Categoría | Lexemas / Expresión Regular |
| :--- | :--- | :--- |
| `VAR` | Palabra reservada | `'var'` |
| `SEED` | Configuración | `'seed'` |
| `CHAIN`, `STATE`, `TRANSITION` | Palabras de dominio | `'chain'`, `'state'`, `'transition'` |
| `SIMULATE`, `STATIONARY` | Operaciones de dominio | `'simulate'`, `'stationary'` |
| `IF`, `THEN`, `ELSE`, `WHILE`, `DO` | Control de flujo | `'if'`, `'then'`, `'else'`, `'while'`, `'do'` |
| `PRINT` | Salida estándar | `'print'` |
| `INT_TYPE`, `FLOAT_TYPE`, `BOOL_TYPE`, `STRING_TYPE`, `STATE_TYPE` | Tipos de datos | `'int'`, `'float'`, `'bool'`, `'string'`, `'state'` |
| `TRUE`, `FALSE` | Constantes booleanas | `'true'`, `'false'` |
| `RELOP` | Operadores relacionales | `'==' \| '!=' \| '<=' \| '>=' \| '<' \| '>'` |
| `ADDOP` | Operadores aditivos | `'+' \| '-'` |
| `MULOP` | Operadores multiplicativos | `'*' \| '/' \| 'MOD' \| 'DIV'` |
| `ASSIGN` | Asignación | `':='` |
| `ARROW` | Operador de transición | `'->'` |
| `COLON`, `SEMI`, `COMMA` | Signos de puntuación | `':'`, `';'`, `','` |
| `LPAREN`, `RPAREN`, `LBRACE`, `RBRACE` | Delimitadores | `'('`, `')'`, `'{'`, `'}'` |
| `FLOAT_LIT` | Constante flotante | `[0-9]+ '.' [0-9]+` |
| `INT_LIT` | Constante entera | `[0-9]+` |
| `STRING_LIT` | Cadena literal | `'"' ~["\r\n]* '"'` |
| `ID` | Identificador | `[a-zA-Z_][a-zA-Z0-9_]*` |
| `WS`, `LINE_COMMENT`, `BLOCK_COMMENT` | Espacios y comentarios | `-> skip` |

---

## 5. Analizador Sintáctico y Derivaciones

### 5.1 Gramática Libre de Contexto
A continuación se presenta la gramática formal en notación BNF simplificada:

```
program        ::= globalConfig* statement* EOF
globalConfig   ::= seedStmt
seedStmt       ::= SEED INT_LIT SEMI

statement      ::= varDecl | assignment | ifStmt | whileStmt | printStmt 
                 | chainDecl | simulateStmt | stationaryStmt | block
varDecl        ::= VAR ID COLON typeSpec SEMI
typeSpec       ::= INT_TYPE | FLOAT_TYPE | BOOL_TYPE | STRING_TYPE | STATE_TYPE
assignment     ::= ID ASSIGN expression SEMI
ifStmt         ::= IF expression THEN block (ELSE block)?
whileStmt      ::= WHILE expression DO block
block          ::= LBRACE statement* RBRACE
printStmt      ::= PRINT LPAREN expression RPAREN SEMI

chainDecl      ::= CHAIN ID DO LBRACE chainBody* RBRACE
chainBody      ::= stateDecl | transitionStmt
stateDecl      ::= STATE ID SEMI
transitionStmt ::= TRANSITION ID ARROW ID LPAREN expression RPAREN SEMI
simulateStmt   ::= SIMULATE LPAREN ID COMMA ID COMMA expression RPAREN SEMI
stationaryStmt ::= STATIONARY LPAREN ID RPAREN SEMI

expression     ::= relationalExpr
relationalExpr ::= relationalExpr RELOP additiveExpr | additiveExpr
additiveExpr   ::= additiveExpr ADDOP multiplicativeExpr | multiplicativeExpr
multiplicativeExpr ::= multiplicativeExpr MULOP factor | factor
factor         ::= INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | ID | LPAREN expression RPAREN
```

### 5.2 Derivaciones Más a la Izquierda Representativas
Siguiendo la convención formal explicada en clase (no-terminales en itálica, terminales en negrita y sustitución del no-terminal situado más a la izquierda):

#### Derivación 1: Declaración de variable (`var pasos : int;`)
$$\begin{aligned}
varDecl &\Rightarrow_{lm} \textbf{var} \; \textbf{id} \; \textbf{:} \; typeSpec \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{var} \; pasos \; \textbf{:} \; typeSpec \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{var} \; pasos \; \textbf{:} \; \textbf{int} \; \textbf{;}
\end{aligned}$$

#### Derivación 2: Asignación con expresión (`pasos := 20;`)
$$\begin{aligned}
assignment &\Rightarrow_{lm} \textbf{id} \; \textbf{:=} \; expression \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; expression \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; relationalExpr \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; additiveExpr \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; multiplicativeExpr \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; factor \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; 20 \; \textbf{;}
\end{aligned}$$

#### Derivación 3: Transición probabilística (`transition Sunny -> Rainy (0.2);`)
$$\begin{aligned}
transitionStmt &\Rightarrow_{lm} \textbf{transition} \; \textbf{id} \; \textbf{->} \; \textbf{id} \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; \textbf{id} \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; Rainy \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; Rainy \; \textbf{(} \; 0.2 \; \textbf{)} \; \textbf{;}
\end{aligned}$$

#### Derivación 4: Simulación estocástica (`simulate(Clima, Soleado, 10);`)
$$\begin{aligned}
simulateStmt &\Rightarrow_{lm} \textbf{simulate} \; \textbf{(} \; \textbf{id} \; \textbf{,} \; \textbf{id} \; \textbf{,} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{simulate} \; \textbf{(} \; Clima \; \textbf{,} \; \textbf{id} \; \textbf{,} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{simulate} \; \textbf{(} \; Clima \; \textbf{,} \; Soleado \; \textbf{,} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{simulate} \; \textbf{(} \; Clima \; \textbf{,} \; Soleado \; \textbf{,} \; 10 \; \textbf{)} \; \textbf{;}
\end{aligned}$$

*(Para la lista exhaustiva de 16 derivaciones formales, véase el anexo `doc/DERIVACIONES.md`)*.

---

## 6. Analizador Semántico y Manejo de Errores

El analizador semántico recorre el árbol de sintaxis mediante un `SemanticVisitor` y utiliza una tabla de símbolos con gestión de ámbitos anidados (`_scope_stack`). Se implementaron las siguientes verificaciones:

### 6.1 Errores Generales del Lenguaje
1. **Variable no declarada:** Ocurre al emplear un identificador que no fue registrado previamente en el ámbito actual o en los ámbitos padres.
2. **Variable redeclarada:** Se genera si se intenta declarar dos veces el mismo identificador dentro del mismo bloque.
3. **Incompatibilidad de tipos:** Ocurre cuando el tipo evaluado de una expresión no coincide ni es promocionable al tipo de la variable destino en una asignación.
4. **Variable no inicializada:** Se detecta cuando se lee una variable cuyo flag `initialized` se encuentra en falso.
5. **División entre cero:** Se evalúa en tiempo de compilación si el operando derecho de los operadores `/`, `DIV` o `MOD` es un literal numérico igual a $0$.

### 6.2 Errores Semánticos del Dominio (Cadenas de Markov)
6. **Violación de la propiedad estocástica:** Al concluir la definición de una cadena, el compilador suma las probabilidades salientes de cada estado $\sum_{j} P(s_i \to s_j)$. Si la suma difiere de $1.0$ (con tolerancia $\varepsilon = 10^{-4}$ para precisión en punto flotante), se emite un error indicando el estado exacto donde falló la condición.
7. **Estado no declarado:** Si una sentencia `transition` o `simulate` hace referencia a un estado que no fue definido mediante `state <nombre>;` dentro de la cadena, se emite un error de referencia inexistente.

---

## 7. Resultados de Pruebas

A continuación se muestra el resultado de evaluar los casos de prueba incluidos en la carpeta `tests/`:

| Archivo | Tipo de Caso | Comportamiento Esperado | Resultado |
| :--- | :--- | :--- | :--- |
| `tests/entrada1_weather.txt` | Válido (Clima) | Pasa análisis y genera archivo C | Exitoso (`output/entrada1_weather.c`) |
| `tests/entrada2_market.txt` | Válido (Mercado) | Pasa análisis y genera archivo C | Exitoso (`output/entrada2_market.c`) |
| `tests/entrada3.txt` | Válido (Control) | Pasa análisis sintáctico y semántico | Exitoso |
| `tests/error_sem1.txt` | Semántico | Detecta variable no declarada | Exitoso (`[Línea 2] Variable 'x' no declarada`) |
| `tests/error_sem2.txt` | Semántico | Detecta variable duplicada | Exitoso (`[Línea 3] Variable 'x' ya declarada`) |
| `tests/error_sem3.txt` | Semántico | Detecta incompatibilidad de tipos | Exitoso (`[Línea 3] No se puede asignar 'string' a 'int'`) |
| `tests/error_sem4.txt` | Semántico | Detecta variable no inicializada | Exitoso (`[Línea 4] Variable 'a' sin inicializar`) |
| `tests/error_sem5.txt` | Semántico | Detecta división por cero constante | Exitoso (`[Línea 3] División por cero constante`) |
| `tests/error_sem6.txt` | Semántico (Dominio) | Detecta suma de probabilidades != 1.0 | Exitoso (`[Línea 4] Probabilidades suman 1.3 != 1.0`) |
| `tests/error_sem7.txt` | Semántico (Dominio) | Detecta estado inexistente | Exitoso (`[Línea 8] Estado 'Snowy' no declarado`) |
| `tests/error_sin1.txt` | Sintáctico | Error de sintaxis por falta de ';' | Exitoso (`missing ';' at 'x'`) |
| `tests/warning1.txt` | Advertencia | Detecta variable declarada y no usada | Exitoso (`Advertencia: 'y' no utilizada`) |

---

## 8. Conclusiones

1. **MarkovLang** ofrece una alternativa práctica y formal para especificar Cadenas de Markov de manera declarativa, eliminando la necesidad de codificar manualmente índices matriciales.
2. La incorporación de la validación estática de la **propiedad estocástica** previene errores de modelado antes de la ejecución, garantizando consistencia probabilística.
3. El compilador cumple el requisito de **reducción a un lenguaje de menor nivel**, traduciendo las definiciones a C puro con arreglos bidimensionales estáticos y rutinas de simulación estocástica.
4. La estructura modular desarrollada sienta las bases para los siguientes hitos, permitiendo extender la generación de código hacia **LLVM IR** y soportar cadenas en tiempo continuo.
