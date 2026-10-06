# Gramáticas Libres de Contexto y Derivaciones Más a la Izquierda
**Curso:** Teoría de Compiladores (Ciclo 2026-2)  
**Profesor:** Prof. José Luis Soncco Álvarez  
**Lenguaje:** MarkovLang (DSL para Cadenas de Markov y Procesos Estocásticos)  
**Documento de Soporte Formal para el Informe (Hito 1 - Trabajo Parcial)**

---

## 1. Convención Notacional de Clase
De acuerdo con las diapositivas de la Unidad II (Prof. José Luis Soncco Álvarez, diapositivas 22-25 y 31-32):
* **Símbolos terminales:** Cadenas en negrita: $\textbf{var}$, $\textbf{:=}$, $\textbf{chain}$, $\textbf{state}$, $\textbf{transition}$, $\textbf{simulate}$, $\textbf{->}$, $\textbf{;}$, etc.
* **Símbolos no-terminales:** Nombres en itálica: *statement*, *expression*, *chainDecl*, *relationalExpr*, *additiveExpr*, etc.
* **Derivación más a la izquierda ($\Rightarrow_{lm}$):** En cada paso de sustitución se reemplaza el no-terminal ubicado más a la izquierda en la forma sentencial.

---

## 2. Construcción 1: Declaración y Asignación de Variables

### Reglas de Producción Formales ($G_1$)
$$\begin{aligned}
varDecl &\to \textbf{var} \; \textbf{id} \; \textbf{:} \; typeSpec \; \textbf{;} \\
assignment &\to \textbf{id} \; \textbf{:=} \; expression \; \textbf{;} \\
typeSpec &\to \textbf{int} \mid \textbf{float} \mid \textbf{bool} \mid \textbf{string} \mid \textbf{state} \\
expression &\to \textbf{id} \mid \textbf{int\_lit} \mid \textbf{float\_lit} \mid \textbf{string\_lit}
\end{aligned}$$

### Derivaciones Más a la Izquierda ($\Rightarrow_{lm}$)

#### Ejemplo 1.1: `var pasos : int;`
$$\begin{aligned}
varDecl &\Rightarrow_{lm} \textbf{var} \; \textbf{id} \; \textbf{:} \; typeSpec \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{var} \; pasos \; \textbf{:} \; typeSpec \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{var} \; pasos \; \textbf{:} \; \textbf{int} \; \textbf{;}
\end{aligned}$$

#### Ejemplo 1.2: `var umbral : float;`
$$\begin{aligned}
varDecl &\Rightarrow_{lm} \textbf{var} \; \textbf{id} \; \textbf{:} \; typeSpec \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{var} \; umbral \; \textbf{:} \; typeSpec \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{var} \; umbral \; \textbf{:} \; \textbf{float} \; \textbf{;}
\end{aligned}$$

#### Ejemplo 1.3: `var convergencia : bool;`
$$\begin{aligned}
varDecl &\Rightarrow_{lm} \textbf{var} \; \textbf{id} \; \textbf{:} \; typeSpec \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{var} \; convergencia \; \textbf{:} \; typeSpec \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{var} \; convergencia \; \textbf{:} \; \textbf{bool} \; \textbf{;}
\end{aligned}$$

#### Ejemplo 1.4: `pasos := 20;`
$$\begin{aligned}
assignment &\Rightarrow_{lm} \textbf{id} \; \textbf{:=} \; expression \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; expression \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; \textbf{int\_lit} \; \textbf{;} \\
&\Rightarrow_{lm} pasos \; \textbf{:=} \; 20 \; \textbf{;}
\end{aligned}$$

---

## 3. Construcción 2: Expresiones Aritméticas y Lógicas

### Reglas de Producción Formales ($G_2$ - Estructura Estratificada de Clase)
$$\begin{aligned}
expression &\to relationalExpr \\
relationalExpr &\to relationalExpr \; \textbf{relop} \; additiveExpr \mid additiveExpr \\
additiveExpr &\to additiveExpr \; \textbf{addop} \; multiplicativeExpr \mid multiplicativeExpr \\
multiplicativeExpr &\to multiplicativeExpr \; \textbf{mulop} \; factor \mid factor \\
factor &\to \textbf{id} \mid \textbf{int\_lit} \mid \textbf{float\_lit} \mid \textbf{true} \mid \textbf{false} \mid \textbf{(} \; expression \; \textbf{)}
\end{aligned}$$

### Derivaciones Más a la Izquierda ($\Rightarrow_{lm}$)

#### Ejemplo 2.1: `x + y * 2`
$$\begin{aligned}
expression &\Rightarrow_{lm} relationalExpr \Rightarrow_{lm} additiveExpr \\
&\Rightarrow_{lm} additiveExpr \; \textbf{addop} \; multiplicativeExpr \\
&\Rightarrow_{lm} multiplicativeExpr \; \textbf{+} \; multiplicativeExpr \\
&\Rightarrow_{lm} factor \; \textbf{+} \; multiplicativeExpr \\
&\Rightarrow_{lm} \textbf{id} \; \textbf{+} \; multiplicativeExpr \\
&\Rightarrow_{lm} x \; \textbf{+} \; multiplicativeExpr \\
&\Rightarrow_{lm} x \; \textbf{+} \; multiplicativeExpr \; \textbf{mulop} \; factor \\
&\Rightarrow_{lm} x \; \textbf{+} \; factor \; \textbf{*} \; factor \\
&\Rightarrow_{lm} x \; \textbf{+} \; y \; \textbf{*} \; 2
\end{aligned}$$

#### Ejemplo 2.2: `contador < 10`
$$\begin{aligned}
expression &\Rightarrow_{lm} relationalExpr \\
&\Rightarrow_{lm} relationalExpr \; \textbf{relop} \; additiveExpr \\
&\Rightarrow_{lm} additiveExpr \; \textbf{<} \; additiveExpr \\
&\Rightarrow_{lm} multiplicativeExpr \; \textbf{<} \; multiplicativeExpr \\
&\Rightarrow_{lm} factor \; \textbf{<} \; factor \\
&\Rightarrow_{lm} contador \; \textbf{<} \; 10
\end{aligned}$$

#### Ejemplo 2.3: `contador MOD 2 == 0`
$$\begin{aligned}
expression &\Rightarrow_{lm} relationalExpr \\
&\Rightarrow_{lm} relationalExpr \; \textbf{relop} \; additiveExpr \\
&\Rightarrow_{lm} additiveExpr \; \textbf{==} \; additiveExpr \\
&\Rightarrow_{lm} multiplicativeExpr \; \textbf{==} \; additiveExpr \\
&\Rightarrow_{lm} multiplicativeExpr \; \textbf{MOD} \; factor \; \textbf{==} \; factor \\
&\Rightarrow_{lm} contador \; \textbf{MOD} \; 2 \; \textbf{==} \; 0
\end{aligned}$$

#### Ejemplo 2.4: `(a + b) * c`
$$\begin{aligned}
expression &\Rightarrow_{lm} additiveExpr \Rightarrow_{lm} multiplicativeExpr \\
&\Rightarrow_{lm} multiplicativeExpr \; \textbf{mulop} \; factor \\
&\Rightarrow_{lm} factor \; \textbf{*} \; factor \\
&\Rightarrow_{lm} \textbf{(} \; expression \; \textbf{)} \; \textbf{*} \; factor \\
&\Rightarrow_{lm} \textbf{(} \; additiveExpr \; \textbf{)} \; \textbf{*} \; factor \\
&\Rightarrow_{lm} \textbf{(} \; a \; \textbf{+} \; b \; \textbf{)} \; \textbf{*} \; c
\end{aligned}$$

---

## 4. Construcción 3: Sentencias de Control Selectivas e Iterativas

### Reglas de Producción Formales ($G_3$)
$$\begin{aligned}
statement &\to ifStmt \mid whileStmt \\
ifStmt &\to \textbf{if} \; expression \; \textbf{then} \; block \mid \textbf{if} \; expression \; \textbf{then} \; block \; \textbf{else} \; block \\
whileStmt &\to \textbf{while} \; expression \; \textbf{do} \; block \\
block &\to \textbf{\{} \; statement^* \; \textbf{\}}
\end{aligned}$$

### Derivaciones Más a la Izquierda ($\Rightarrow_{lm}$)

#### Ejemplo 3.1: `if convergencia then { }`
$$\begin{aligned}
statement &\Rightarrow_{lm} ifStmt \\
&\Rightarrow_{lm} \textbf{if} \; expression \; \textbf{then} \; block \\
&\Rightarrow_{lm} \textbf{if} \; convergencia \; \textbf{then} \; \textbf{\{} \; \textbf{\}}
\end{aligned}$$

#### Ejemplo 3.2: `if cond then { } else { }`
$$\begin{aligned}
statement &\Rightarrow_{lm} ifStmt \\
&\Rightarrow_{lm} \textbf{if} \; expression \; \textbf{then} \; block \; \textbf{else} \; block \\
&\Rightarrow_{lm} \textbf{if} \; cond \; \textbf{then} \; \textbf{\{} \; \textbf{\}} \; \textbf{else} \; \textbf{\{} \; \textbf{\}}
\end{aligned}$$

#### Ejemplo 3.3: `while contador < 5 do { }`
$$\begin{aligned}
statement &\Rightarrow_{lm} whileStmt \\
&\Rightarrow_{lm} \textbf{while} \; expression \; \textbf{do} \; block \\
&\Rightarrow_{lm} \textbf{while} \; contador < 5 \; \textbf{do} \; \textbf{\{} \; \textbf{\}}
\end{aligned}$$

#### Ejemplo 3.4: `while activo do { print(x); }`
$$\begin{aligned}
statement &\Rightarrow_{lm} whileStmt \\
&\Rightarrow_{lm} \textbf{while} \; expression \; \textbf{do} \; block \\
&\Rightarrow_{lm} \textbf{while} \; activo \; \textbf{do} \; \textbf{\{} \; statement \; \textbf{\}} \\
&\Rightarrow_{lm} \textbf{while} \; activo \; \textbf{do} \; \textbf{\{} \; printStmt \; \textbf{\}} \\
&\Rightarrow_{lm} \textbf{while} \; activo \; \textbf{do} \; \textbf{\{} \; \textbf{print} \; \textbf{(} \; x \; \textbf{)} \; \textbf{;} \; \textbf{\}}
\end{aligned}$$

---

## 5. Construcción 4: Dominio de Cadenas de Markov

### Reglas de Producción Formales ($G_4$)
$$\begin{aligned}
chainDecl &\to \textbf{chain} \; \textbf{id} \; \textbf{do} \; \textbf{\{} \; chainBody^* \; \textbf{\}} \\
chainBody &\to stateDecl \mid transitionStmt \\
stateDecl &\to \textbf{state} \; \textbf{id} \; \textbf{;} \\
transitionStmt &\to \textbf{transition} \; \textbf{id} \; \textbf{->} \; \textbf{id} \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
simulateStmt &\to \textbf{simulate} \; \textbf{(} \; \textbf{id} \; \textbf{,} \; \textbf{id} \; \textbf{,} \; expression \; \textbf{)} \; \textbf{;}
\end{aligned}$$

### Derivaciones Más a la Izquierda ($\Rightarrow_{lm}$)

#### Ejemplo 4.1: `state Sunny;`
$$\begin{aligned}
chainBody &\Rightarrow_{lm} stateDecl \\
&\Rightarrow_{lm} \textbf{state} \; \textbf{id} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{state} \; Sunny \; \textbf{;}
\end{aligned}$$

#### Ejemplo 4.2: `transition Sunny -> Rainy (0.2);`
$$\begin{aligned}
chainBody &\Rightarrow_{lm} transitionStmt \\
&\Rightarrow_{lm} \textbf{transition} \; \textbf{id} \; \textbf{->} \; \textbf{id} \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; \textbf{id} \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; Rainy \; \textbf{(} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{transition} \; Sunny \; \textbf{->} \; Rainy \; \textbf{(} \; 0.2 \; \textbf{)} \; \textbf{;}
\end{aligned}$$

#### Ejemplo 4.3: `simulate(Weather, Sunny, 20);`
$$\begin{aligned}
statement &\Rightarrow_{lm} simulateStmt \\
&\Rightarrow_{lm} \textbf{simulate} \; \textbf{(} \; \textbf{id} \; \textbf{,} \; \textbf{id} \; \textbf{,} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{simulate} \; \textbf{(} \; Weather \; \textbf{,} \; \textbf{id} \; \textbf{,} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{simulate} \; \textbf{(} \; Weather \; \textbf{,} \; Sunny \; \textbf{,} \; expression \; \textbf{)} \; \textbf{;} \\
&\Rightarrow_{lm} \textbf{simulate} \; \textbf{(} \; Weather \; \textbf{,} \; Sunny \; \textbf{,} \; 20 \; \textbf{)} \; \textbf{;}
\end{aligned}$$

#### Ejemplo 4.4: `chain Weather do { state Sunny; transition Sunny -> Sunny (0.8); }`
$$\begin{aligned}
chainDecl &\Rightarrow_{lm} \textbf{chain} \; \textbf{id} \; \textbf{do} \; \textbf{\{} \; chainBody \; chainBody \; \textbf{\}} \\
&\Rightarrow_{lm} \textbf{chain} \; Weather \; \textbf{do} \; \textbf{\{} \; chainBody \; chainBody \; \textbf{\}} \\
&\Rightarrow_{lm} \textbf{chain} \; Weather \; \textbf{do} \; \textbf{\{} \; stateDecl \; chainBody \; \textbf{\}} \\
&\Rightarrow_{lm} \textbf{chain} \; Weather \; \textbf{do} \; \textbf{\{} \; \textbf{state} \; Sunny \; \textbf{;} \; chainBody \; \textbf{\}} \\
&\Rightarrow_{lm} \textbf{chain} \; Weather \; \textbf{do} \; \textbf{\{} \; \textbf{state} \; Sunny \; \textbf{;} \; transitionStmt \; \textbf{\}} \\
&\Rightarrow_{lm} \textbf{chain} \; Weather \; \textbf{do} \; \textbf{\{} \; \textbf{state} \; Sunny \; \textbf{;} \; \textbf{transition} \; Sunny \; \textbf{->} \; Sunny \; \textbf{(} \; 0.8 \; \textbf{)} \; \textbf{;} \; \textbf{\}}
\end{aligned}$$
