# Guion Técnico para el Video Demostrativo (Máximo 5 Minutos)
**Curso:** Teoría de Compiladores  
**Profesor:** Prof. José Luis Soncco Álvarez  
**Proyecto:** Compilador MarkovLang  
**Hito:** Hito 1 - Trabajo Parcial

---

## Cronograma del Video (Duración Total: 4:30 a 5:00 min)

### [0:00 - 0:45] Bloque 1: Introducción, Problemática y Motivación
* **Pantalla:** Diapositiva de carátula o VS Code mostrando el proyecto.
* **Guion:**
  > "Buenas tardes profesor. Somos el Grupo [X] y hoy presentamos el compilador de **MarkovLang**, un Lenguaje de Dominio Específico para el modelado, validación y compilación de Cadenas de Markov de Tiempo Discreto.
  > La motivación nace de que actualmente no existe un lenguaje especializado para cadenas de Markov. En lenguajes como C o C++, el programador tiene que construir matrices a mano, mapear estados a índices enteros e implementar bucles de simulación Monte Carlo sin ninguna verificación estática. Si las probabilidades de un estado no suman 1.0, el programa falla en silencio. MarkovLang valida la propiedad estocástica en tiempo de compilación y se compila directamente a código C de bajo nivel."

---

### [0:45 - 1:45] Bloque 2: Arquitectura del Front-End y Gramática ANTLR4
* **Pantalla:** Mostrar el archivo `MarkovLang.g4` y la estructura de carpetas (`gen/`, `semantic/`, `tests/`).
* **Guion:**
  > "Nuestra arquitectura modular sigue los lineamientos del curso:
  > - La gramática `MarkovLang.g4` define declaraciones con `var x : tipo;`, asignaciones con `x := expr;`, estructuras `if-then-else`, `while-do` y primitivas de dominio como `chain ... do { }`, `state` y `transition`.
  > - Para las expresiones aritméticas y relacionales usamos la estratificación de reglas vista en las semanas 5 y 6 (`relationalExpr`, `additiveExpr`, `multiplicativeExpr`, `factor`), resolviendo la precedencia sin ambigüedades."

---

### [1:45 - 2:45] Bloque 3: Análisis Semántico y Tabla de Símbolos
* **Pantalla:** Mostrar `semantic/symbol_table.py` y `semantic/semantic_visitor.py`.
* **Guion:**
  > "El análisis semántico utiliza el patrón Visitor y una tabla de símbolos con pila de ámbitos estáticos (`_scope_stack = ['global']`), tal como se desarrolló en la Semana 6.
  > Implementamos:
  > 1. Detección de variables no declaradas y redeclaraciones en el mismo ámbito.
  > 2. Detección de variables no inicializadas (`initialized = False`) y división por cero con constantes.
  > 3. Y la regla matemática reina de nuestro dominio: **Violación de la Propiedad Estocástica**. El compilador comprueba estáticamente que la suma de probabilidades que salen de cada estado sume exactamente 1.0, además de verificar que los estados origen y destino existan en la cadena."

---

### [2:45 - 4:10] Bloque 4: Demostración en la Terminal
* **Pantalla:** Terminal de comandos (PowerShell / Bash).

#### Paso 1: Mostrar captura de errores semánticos de dominio
```bash
python main.py tests/error_sem6.txt
```
* **Explicar:** "Aquí vemos cómo el compilador detecta inmediatamente que las probabilidades del estado 'Sunny' suman 1.3 y lanza el error semántico con la línea exacta."

```bash
python main.py tests/error_sem7.txt
```
* **Explicar:** "En este caso detecta que el estado 'Snowy' no fue declarado previamente en la cadena."

#### Paso 2: Mostrar caso válido y compilación a lenguaje de bajo nivel (C)
```bash
python main.py tests/entrada1_weather.txt
```
* **Explicar:**
  > "Compilamos el archivo `entrada1_weather.txt`, que define el modelo de clima con estados Sunny y Rainy y una simulación de 20 pasos.
  > El análisis léxico, sintáctico y semántico pasa con 0 errores.
  > Y aquí vemos el cumplimiento clave del compilador: genera automáticamente el archivo de bajo nivel `output/entrada1_weather.c`."

#### Paso 3: Mostrar el código C generado
* **Abrir en pantalla:** `output/entrada1_weather.c`
* **Explicar:**
  > "Observen cómo las abstracciones de alto nivel de MarkovLang se simplificaron a bajo nivel:
  > - Se generaron las enumeraciones `Weather_State`.
  > - La matriz plana bidimensional estática `float Weather_P[2][2]`.
  > - Y la función de simulación Monte Carlo en C puro con números pseudoaleatorios y acumulador de probabilidad, además del algoritmo para calcular la distribución estacionaria."

---

### [4:10 - 4:45] Bloque 5: Conclusiones y Proyección a LLVM
* **Guion:**
  > "Para el Hito 1 tenemos el front-end 100% operativo, con comprobaciones semánticas formales y generación de código de bajo nivel.
  > Para los Hitos 2 y 3, continuaremos extendiendo este backend hacia la generación de **LLVM IR**. Muchas gracias por su atención."
