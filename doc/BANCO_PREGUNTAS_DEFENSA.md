# Banco de Preguntas y Respuestas para la Sustentación Oral
**Curso:** Teoría de Compiladores  
**Docente:** Prof. José Luis Soncco Álvarez  
**Proyecto:** Compilador MarkovLang  
**Ponderación en Rúbrica:** **6 a 8 puntos**

---

### 1. ¿Cuál es la justificación de crear un nuevo lenguaje para Cadenas de Markov?
* **Respuesta del estudiante:**  
  *"Actualmente, modelar una Cadena de Markov en lenguajes como C, C++ o Java requiere manipular matrices numéricas crudas, asociar identificadores de estados a índices enteros arbitrarios y verificar manualmente que las probabilidades sumen 1.0. Esto carece de comprobación estática: cualquier error en las probabilidades o estados genera cálculos incorrectos en tiempo de ejecución sin ninguna advertencia del compilador. MarkovLang introduce las entidades de estados y transiciones a nivel de lenguaje y permite realizar análisis estático formal antes de generar código."*

---

### 2. ¿A qué lenguaje de bajo nivel compila y cómo se simplifican las construcciones?
* **Respuesta del estudiante:**  
  *"MarkovLang compila hacia **código en C de bajo nivel** (con miras a **LLVM IR** en los Hitos 2 y 3). El compilador realiza una simplificación y descenso de abstracción (*lowering*):
  1. Las declaraciones simbólicas `state Sunny; state Rainy;` se traducen a tipos enumerados en C (`typedef enum { STATE_Sunny = 0, ... }`).
  2. Las sentencias declarativas de transición se mapean a una **matriz estática plana** bidimensional en memoria (`float P[N][N]`).
  3. Las instrucciones `simulate` y `stationary` se traducen a bucles `for` en C de simulación Monte Carlo con generadores de números pseudoaleatorios y búsqueda en la función de distribución acumulada (CDF), y potenciación de matrices para la distribución estacionaria. De esta forma, el programador escribe un modelo declarativo y obtiene código C nativo y optimizado."*

---

### 3. ¿Cómo comprueba el analizador semántico la Propiedad Estocástica?
* **Respuesta del estudiante:**  
  *"Una matriz de transición es estocásticamente válida si y solo si para cada estado $i$, la suma de las probabilidades hacia todos los estados destino $j$ es exactamente igual a 1.0:*
  $$\sum_{j=1}^{N} P(i \to j) = 1.0 \quad \text{y} \quad 0 \le P(i \to j) \le 1.0$$
  *En nuestro `SemanticVisitor`, al visitar el bloque de la cadena, agrupamos todas las transiciones por estado de origen. Si para algún estado la sumatoria difiere de 1.0 (considerando una tolerancia de coma flotante de $10^{-4}$), el compilador emite un `SemanticError` indicando el estado infractor y el valor acumulado, abortando la compilación antes de generar código."*

---

### 4. ¿Por qué utilizaron una gramática estratificada para las expresiones en lugar de ambigüedad con prioridades?
* **Respuesta del estudiante:**  
  *"Siguiendo las diapositivas de las Semanas 5 y 6, organizamos la gramática en niveles jerárquicos: `expression -> relationalExpr -> additiveExpr -> multiplicativeExpr -> factor`. Esta técnica estratificada refleja formalmente la precedencia de operadores (multiplicación antes que suma, y suma antes que comparaciones relacionales) y garantiza que el árbol de derivación sea único, eliminando la ambigüedad inherente y facilitando el análisis LL(1) o top-down."*

---

### 5. ¿Por qué eligieron el patrón Visitor sobre el patrón Listener para el análisis semántico?
* **Respuesta del estudiante:**  
  *"El patrón Listener realiza un recorrido pasivo en profundidad controlado por ANTLR (`enterRule` y `exitRule`). El patrón Visitor nos otorga control explícito sobre el recorrido: podemos condicionar qué ramas visitar (por ejemplo, evaluar sentencias `if-then-else` o ciclos `while`), y fundamentalmente, los métodos de visita pueden **retornar valores directamente** (`return expr_type`). Esto es indispensable para la inferencia de tipos y para las comprobaciones en `ARITH_COMPAT`."*

---

### 6. ¿Cómo se proyecta el compilador para los Hitos 2 y 3 con LLVM?
* **Respuesta del estudiante:**  
  *"Actualmente el compilador ya genera una representación intermedia y emite código de bajo nivel en C. Para el Hito 2 (50% final) y Hito 3 (entrega final), sustituiremos la emisión de texto en C por la generación directa de **LLVM IR** utilizando la librería `llvmlite` o la API de LLVM. Las matrices y bucles de Monte Carlo se generarán con instrucciones LLVM como `alloca`, `load`, `store`, `fadd`, `fcmp` y `br`, permitiendo compilar directamente a binarios nativos optimizados con `clang` o `llc`."*
