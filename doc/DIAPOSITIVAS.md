# Contenido de Diapositivas para la Presentación (PDF)
**Curso:** Teoría de Compiladores (Ciclo 2026-2)  
**Profesor:** Prof. José Luis Soncco Álvarez  
**Hito:** Hito 1 - Trabajo Parcial (Semana 7)  
**Proyecto:** Compilador MarkovLang

---

### Diapositiva 1: Portada
* **Título:** MarkovLang: Compilador para Modelado y Validación de Cadenas de Markov
* **Curso:** Teoría de Compiladores
* **Integrantes:** [Nombres y Códigos de los estudiantes]
* **Carrera:** Ciencias de la Computación (6to Ciclo)

---

### Diapositiva 2: Problemática y Motivación
* Las Cadenas de Markov de Tiempo Discreto (DTMC) se implementan a mano en C/C++ usando matrices y arreglos planos.
* **Carencia de análisis estático:** Si una fila de probabilidad no suma 1.0 o un estado está mal conectado, el error solo se descubre en tiempo de ejecución.
* **MarkovLang:** Provee un lenguaje declarativo con comprobación estática de axiomas de probabilidad y se **compila a un lenguaje de bajo nivel (C / LLVM)**.

---

### Diapositiva 3: Arquitectura del Front-End (Estilo de Clase)
* Pipeline del compilador:
  `MarkovLang.g4 -> [ANTLR4 Tool] -> gen/ (Lexer & Parser) -> main.py -> semantic/ (SymbolTable & SemanticVisitor) -> codegen.py -> output/ (.c)`
* Estructura modular idéntica a la vista en clase (`gen/`, `semantic/`, `main.py`, `Makefile`).

---

### Diapositiva 4: Especificación Léxica y Sintáctica
* Sintaxis alineada a las convenciones de clase:
  * Declaración: `var <id> : <tipo>;`
  * Asignación: `<id> := <expr>;`
  * Control: `if <expr> then { } else { }`, `while <expr> do { }`
  * Dominio: `chain <id> do { }`, `state <id>;`, `transition <id> -> <id> (<prob>);`, `simulate(...)`, `stationary(...)`
* Expresiones estratificadas:
  `expression -> relationalExpr -> additiveExpr -> multiplicativeExpr -> factor` (eliminación de ambigüedad).

---

### Diapositiva 5: Análisis Semántico y Tabla de Símbolos
* **Tabla de Símbolos:**
  * Pila de ámbitos estáticos (`_scope_stack = ['global']`).
  * Símbolos con atributos de rastreo: `initialized` y `used`.
* **Reglas semánticas validadas:**
  1. Identificadores no declarados y redeclaraciones locales.
  2. Uso de variables no inicializadas (`initialized = False`).
  3. Validación de división por cero con constante.
  4. Incompatibilidad de tipos con `ARITH_COMPAT`.
  5. **Violación de la propiedad estocástica:** Comprobación estática de que las probabilidades salientes sumen exactamente 1.0 por estado.
  6. Estados origen/destino no declarados.
  7. Advertencias de variables no usadas (`unused_warnings`).

---

### Diapositiva 6: Compilación hacia Bajo Nivel (C)
* **Justificación de nuevo lenguaje:** Abstraer matrices y bucles de Monte Carlo a un DSL seguro.
* **Código C generado (`output/*.c`):**
  * Enumeración de estados tipados (`typedef enum`).
  * Matriz estática plana bidimensional `float P[N][N]`.
  * Funciones nativas de simulación Monte Carlo con números pseudoaleatorios y CDF.
  * Cálculo matricial para la distribución estacionaria.

---

### Diapositiva 7: Resultados Experimentales y Suite de Pruebas
* Suite de pruebas automatizadas en `tests/`:
  * Casos válidos: Modelo climático (`entrada1_weather.txt`) y Modelo de mercado (`entrada2_market.txt`).
  * Pruebas de errores: `error_sem1.txt` a `error_sem7.txt`, `error_sin1.txt`, `warning1.txt`.
  * Generación y validación del código C.

---

### Diapositiva 8: Conclusiones y Próximos Pasos (LLVM)
* Front-end completado y validado formalmente con los conceptos de las semanas 1 a 7.
* Cumplimiento del principio de simplificación hacia lenguajes de más bajo nivel.
* Para los Hitos 2 y 3, extenderemos el backend emitiendo **LLVM IR** directamente.
