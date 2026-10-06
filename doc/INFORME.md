# Informe Técnico - Trabajo Parcial (Hito 1)
## MarkovLang: Lenguaje de Dominio Específico para Modelado, Validación y Compilación de Cadenas de Markov

---

### Datos del Proyecto
* **Curso:** Teoría de Compiladores (Ciclo 2026-2)
* **Docente:** Prof. José Luis Soncco Álvarez
* **Hito:** Hito 1 - Trabajo Parcial (Semana 7)
* **Carrera:** Ciencias de la Computación (6to Ciclo)
* **Competencias Evaluadas:** ABET 3 (Comunicación Efectiva) y Pensamiento Crítico

---

## 1. Problemática y Motivación

En ciencias de la computación, física estadística, bioinformática e inteligencia artificial, las **Cadenas de Markov de Tiempo Discreto (DTMC)** son el modelo formal estándar para estudiar sistemas estocásticos basados en la propiedad de Markov (la probabilidad del estado futuro depende exclusivamente del estado presente).

### ¿Por qué es importante? ¿Existe y es un proceso largo?
Actualmente **no existe un lenguaje de programación de dominio específico (DSL) dedicado a Cadenas de Markov**. Para desarrollar modelos de Markov en lenguajes de propósito general o de bajo nivel como C, C++ o Java, el ingeniero o investigador se enfrenta a un proceso largo, manual y propenso a errores:
1. **Mapeo manual de abstracciones a bajo nivel:** Es necesario asociar identificadores conceptuales (como `Sunny`, `Rainy`, `Bear`, `Bull`) a índices numéricos de matriz (`0, 1, 2...`), perdiendo semántica.
2. **Carencia de análisis semántico estático:** Los lenguajes tradicionales no validan en tiempo de compilación que las probabilidades salientes de un estado sumen exactamente $1.0$ (propiedad estocástica). Si el programador comete un error aritmético o se olvida de una transición, el programa compilará sin advertencias y fallará silenciosamente durante la simulación o cálculo de probabilidades.
3. **Complejidad de implementación repetitiva:** Programar manualmente simulaciones de Monte Carlo (generación de números pseudoaleatorios y búsqueda en la función de distribución acumulada CDF) o la potenciación matricial para la distribución estacionaria $\pi = \pi P$ es repetitivo y verboso.

### Justificación de Compilación hacia un Lenguaje de Bajo Nivel
La razón de ser de **MarkovLang** es proveer un lenguaje de alto nivel declarativo con **verificación estática de tipos y de axiomas de probabilidad**, que al compilarse se **simplifique y traduzca a código de bajo nivel en C**. El compilador automatiza la construcción de enumeraciones, matrices estáticas planas (`float P[N][N]`) y algoritmos optimizados de simulación estocástica en C puro.

---

## 2. Objetivos

### Objetivo General
Diseñar e implementar el front-end y backend inicial del compilador **MarkovLang** en Python 3 utilizando la herramienta **ANTLR4**, siguiendo la metodología y buenas prácticas de ingeniería de compiladores vistas en las Semanas 1 a 7 del curso.

### Objetivos Específicos
1. Formalizar la gramática libre de contexto `MarkovLang.g4` eliminando ambigüedades mediante estratificación de reglas (Semana 5 y 6).
2. Construir una tabla léxica formal de tokens y expresiones regulares.
3. Demostrar la corrección de las reglas mediante derivaciones más a la izquierda ($\Rightarrow_{lm}$) siguiendo la notación formal del curso.
4. Implementar un analizador semántico basado en el patrón *Visitor* con tabla de símbolos de ámbitos estáticos (`_scope_stack`), detectando variables no declaradas, no inicializadas, división por cero con constantes y la **violación de la propiedad estocástica**.
5. Traducir el código validado a un programa ejecutable en **C de bajo nivel**.

---

## 3. Descripción de Construcciones del Lenguaje

A continuación se describen las construcciones del lenguaje con **5 ejemplos por cada una**:

### 3.1 Declaración de Variables
Utiliza la convención `var <id> : <tipo>;` vista en clase.
* **Ejemplo 1:** `var pasos : int;`
* **Ejemplo 2:** `var umbral : float;`
* **Ejemplo 3:** `var convergencia : bool;`
* **Ejemplo 4:** `var modelo : string;`
* **Ejemplo 5:** `var estado_actual : state;`

### 3.2 Sentencias de Asignación
Asignación destructiva fuertemente tipada con el operador `:=`.
* **Ejemplo 1:** `pasos := 20;`
* **Ejemplo 2:** `umbral := 0.001;`
* **Ejemplo 3:** `convergencia := true;`
* **Ejemplo 4:** `modelo := "Modelo Climatico";`
* **Ejemplo 5:** `pasos := pasos + 5;`

### 3.3 Expresiones Aritméticas y Lógicas
Estratificadas según precedencia formal (relacional, aditiva, multiplicativa y factores).
* **Ejemplo 1:** `x + y * 2`
* **Ejemplo 2:** `(iteraciones - 10) / (4 - 1)`
* **Ejemplo 3:** `contador < 10`
* **Ejemplo 4:** `contador MOD 2 == 0`
* **Ejemplo 5:** `prob >= 0.0 and prob <= 1.0`

### 3.4 Sentencias Selectivas (`if-then-else`)
Bifurcaciones condicionadas a expresiones booleanas.
* **Ejemplo 1:** `if convergencia then { print("Convergencia alcanzada"); }`
* **Ejemplo 2:** `if contador MOD 2 == 0 then { print("Par"); } else { print("Impar"); }`
* **Ejemplo 3:** `if pasos > 100 then { print("Simulacion larga"); }`
* **Ejemplo 4:** `if umbral < 0.01 then { convergencia := true; }`
* **Ejemplo 5:** `if contador == 0 then { print("Inicio"); }`

### 3.5 Sentencias Iterativas (`while-do`)
Bucles convencionales de evaluación condicional.
* **Ejemplo 1:** `while contador < 5 do { contador := contador + 1; }`
* **Ejemplo 2:** `while umbral > 0.0001 do { umbral := umbral / 2.0; }`
* **Ejemplo 3:** `while activo do { print("Ejecutando..."); }`
* **Ejemplo 4:** `while pasos > 0 do { pasos := pasos - 1; }`
* **Ejemplo 5:** `while contador < 10 do { print(contador); contador := contador + 1; }`

### 3.6 Construcciones del Dominio de Cadenas de Markov
Primitivas para declarar cadenas, estados, transiciones y simulaciones.
* **Ejemplo 1:** `chain Weather do { state Sunny; state Rainy; }`
* **Ejemplo 2:** `transition Sunny -> Rainy (0.2);`
* **Ejemplo 3:** `transition Rainy -> Sunny (0.4);`
* **Ejemplo 4:** `simulate(Weather, Sunny, 20);`
* **Ejemplo 5:** `stationary(Weather);`

---

## 4. Analizador Léxico

Especificación de componentes léxicos en formato `Token : Patrón / Lista de Lexemas`:

| Token | Categoría | Lexemas / Expresión Regular |
| :--- | :--- | :--- |
| `VAR` | Palabra Clave | `'var'` |
| `SEED` | Configuración Global | `'seed'` |
| `CHAIN`, `STATE`, `TRANSITION` | Dominio Markov | `'chain'`, `'state'`, `'transition'` |
| `SIMULATE`, `STATIONARY` | Operaciones de Dominio | `'simulate'`, `'stationary'` |
| `IF`, `THEN`, `ELSE`, `WHILE`, `DO` | Control de Flujo | `'if'`, `'then'`, `'else'`, `'while'`, `'do'` |
| `PRINT` | Entrada/Salida | `'print'` |
| `INT_TYPE`, `FLOAT_TYPE`, `BOOL_TYPE`, `STRING_TYPE`, `STATE_TYPE` | Tipos de Datos | `'int'`, `'float'`, `'bool'`, `'string'`, `'state'` |
| `TRUE`, `FALSE` | Booleanos | `'true'`, `'false'` |
| `RELOP` | Operadores Relacionales | `'==' \| '!=' \| '<=' \| '>=' \| '<' \| '>'` |
| `ADDOP` | Operadores Aditivos | `'+' \| '-'` |
| `MULOP` | Operadores Multiplicativos | `'*' \| '/' \| 'MOD' \| 'DIV'` |
| `ASSIGN` | Operador Asignación | `':='` |
| `ARROW` | Operador de Transición | `'->'` |
| `COLON`, `SEMI`, `COMMA` | Delimitadores | `':'`, `';'`, `','` |
| `LPAREN`, `RPAREN`, `LBRACE`, `RBRACE` | Agrupación | `'('`, `')'`, `'{'`, `'}'` |
| `FLOAT_LIT` | Literal Decimal | `[0-9]+ '.' [0-9]+` |
| `INT_LIT` | Literal Entero | `[0-9]+` |
| `STRING_LIT` | Cadena | `'"' ~["\r\n]* '"'` |
| `ID` | Identificador | `[a-zA-Z_][a-zA-Z0-9_]*` |
| `WS`, `LINE_COMMENT`, `BLOCK_COMMENT` | Ignorados | `-> skip` |

---

## 5. Analizador Sintáctico y Derivaciones

### 5.1 Gramática Libre de Contexto Formal
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

### 5.2 Derivación Más a la Izquierda Representativa
Para la transición probabilística: `transition Sunny -> Rainy (0.2);`
$$\begin{aligned}
chainBody &\Rightarrow_{lm} transitionStmt \\
&\Rightarrow_{lm} \textbf{transition} \; \textbf{id} \; \textbf{->} \; \textbf{id} \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; \textbf{id} \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; Rainy \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; Rainy \; \textbf{(} \; 0.2 \; \textbf{)} \; \textbf{;}
\end{aligned}$$
*(El compendio completo de 16 derivaciones detalladas se encuentra en el anexo formal `doc/DERIVACIONES.md`)*.

---

## 6. Tratamiento Formal de Errores (Tarea 4 de Clase)

Siguiendo la Diapositiva 12 de la Unidad II:

### 6.1 Errores Léxicos (5 ejemplos)
1. Carácter inválido no perteneciente al alfabeto: `@` o `$`.
2. Identificador iniciado con dígito: `9cadena`.
3. Cadena no delimitada antes del fin de línea: `"modelo sin comillas`.
4. Operador de flecha mal formado: `-->` o `=>`.
5. Literal flotante mal formado: `0..5`.

### 6.2 Errores Sintácticos (5 ejemplos)
1. Omisión de punto y coma en sentencia (`var x : int`).
2. Llaves desbalanceadas en el bloque de la cadena (`chain Weather do { state Sunny;`).
3. Estructura condicional sin palabra clave `then` (`if x == 0 { }`).
4. Estructura iterativa sin palabra clave `do` (`while x < 5 { }`).
5. Paréntesis no balanceados en llamada a simulación (`simulate(Weather, Sunny, 10;`).

### 6.3 Errores Semánticos Formalizados (7 errores implementados)
1. **Variable no declarada:** Uso de una variable en asignación o expresión sin previo `var`.
2. **Variable ya declarada en el mismo ámbito:** Declaración duplicada capturada por `SymbolTable.declare()`.
3. **Incompatibilidad de tipos en asignación:** Intentar asignar tipos incompatibles (ej. `string` a `int`).
4. **Uso de variable no inicializada:** Validación de la Guía de Semana 6 (`initialized == False`).
5. **División por cero con constante:** Operador `/`, `DIV` o `MOD` con operando derecho literal igual a $0$.
6. **Violación de la propiedad estocástica:** La suma de probabilidades de salida de un estado difiere de $1.0$ ($\sum_{j} P(s \to j) \neq 1.0$).
7. **Estado no declarado en la cadena:** Transición que referencia un estado inexistente (`transition Sunny -> Snowy` donde `Snowy` no fue declarado).

---

## 7. Resultados de Validación Experimental

| Archivo de Prueba | Categoría | Resultado Esperado | Resultado Obtenido |
| :--- | :--- | :--- | :--- |
| `tests/entrada1_weather.txt` | Válido (Clima) | Compilación exitosa y código C generado | **Pasa** (OK, C generado en `output/`) |
| `tests/entrada2_market.txt` | Válido (Mercado) | Compilación exitosa y código C generado | **Pasa** (OK, C generado en `output/`) |
| `tests/entrada3.txt` | Válido (Control) | Compilación exitosa | **Pasa** (OK) |
| `tests/error_sem1.txt` | Error Semántico | Variable no declarada | **Pasa** (`[Línea 2] Variable 'x' no declarada`) |
| `tests/error_sem2.txt` | Error Semántico | Variable ya declarada en ámbito | **Pasa** (`[Línea 3] Variable 'x' ya declarada`) |
| `tests/error_sem3.txt` | Error Semántico | Incompatibilidad de tipos | **Pasa** (`[Línea 3] No se puede asignar 'string' a 'int'`) |
| `tests/error_sem4.txt` | Error Semántico | Variable no inicializada | **Pasa** (`[Línea 4] Variable 'a' usada sin inicializar`) |
| `tests/error_sem5.txt` | Error Semántico | División por cero constante | **Pasa** (`[Línea 3] División por cero con constante`) |
| `tests/error_sem6.txt` | Error Semántico | Violación de propiedad estocástica | **Pasa** (`[Línea 4] Probabilidades suman 1.3 != 1.0`) |
| `tests/error_sem7.txt` | Error Semántico | Estado no declarado | **Pasa** (`[Línea 8] Estado 'Snowy' no declarado`) |
| `tests/error_sin1.txt` | Error Sintáctico | Falta punto y coma | **Pasa** (`line 3:0 missing ';' at 'x'. Abortando.`) |
| `tests/warning1.txt` | Advertencia | Variable nunca usada | **Pasa** (`ADVERTENCIA: 'y' declarada nunca fue usada.`) |

---

## 8. Conclusiones
1. **MarkovLang** resuelve una carencia real en el modelado estocástico: provee una sintaxis declarativa limpia y realiza verificación estática de la propiedad estocástica en tiempo de compilación.
2. Cumple con la exigencia fundamental de compiladores al **simplificarse y traducirse a un lenguaje de más bajo nivel (C)**, generando matrices estáticas y bucles eficientes de Monte Carlo.
3. El analizador semántico sigue estrictamente las pautas pedagógicas del curso, implementando la tabla de símbolos con ámbitos estáticos y los ejercicios de la Semana 6.
4. El compilador queda formalmente preparado para los Hitos 2 y 3, donde la generación de C evolucionará hacia **LLVM IR**.
