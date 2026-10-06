# MarkovLang Compiler

**Curso:** Teoría de Compiladores (Ciclo 2026-2)  
**Docente:** Prof. José Luis Soncco Álvarez  
**Hito:** Hito 1 - Trabajo Parcial (Semana 7)  
**Especialidad:** Ciencias de la Computación (6to Ciclo)  

MarkovLang es un Lenguaje de Dominio Específico (DSL) para el modelado, verificación estática y compilación de **Cadenas de Markov de Tiempo Discreto (DTMC)**. El front-end del compilador ha sido construido en Python 3 utilizando **ANTLR4**, implementando la arquitectura modular de clases (Unidad 1, semanas 1 a 7). El compilador realiza comprobaciones semánticas estrictas (incluyendo la **propiedad estocástica**) y se simplifica compilando hacia **código de bajo nivel en C**.

---

## Estructura del Repositorio

```text
TP1/
├── MarkovLang.g4             # Gramática formal del lenguaje (ANTLR4)
├── Makefile                  # Compilación automatizada de la gramática a gen/
├── build.bat                 # Script de compilación rápida para Windows
├── compile_grammar.py        # Compilador multiplataforma de ANTLR4
├── main.py                   # Driver principal del compilador
├── codegen.py                # Generador de código de bajo nivel en C
├── gen/                      # Código generado por ANTLR4 (Lexer, Parser, Visitor)
├── semantic/                 # Módulo de análisis semántico
│   ├── errors.py             # Clase SemanticError con formato "[Error Semántico, línea X]"
│   ├── symbol_table.py       # Tabla de símbolos con pila de ámbitos estáticos
│   └── semantic_visitor.py   # SemanticVisitor con validaciones de tipos y estocásticas
├── tests/                    # Suite de casos de prueba
│   ├── entrada1_weather.txt  # Modelo climático clásico (Sunny, Rainy) + Simulación Monte Carlo
│   ├── entrada2_market.txt   # Modelo financiero de mercado (Bull, Bear, Stagnant)
│   ├── entrada3.txt          # Construcciones de control, expresiones e I/O
│   ├── error_sem1.txt        # Variable no declarada
│   ├── error_sem2.txt        # Variable ya declarada en el mismo ámbito
│   ├── error_sem3.txt        # Incompatibilidad de tipos en asignación
│   ├── error_sem4.txt        # Variable no inicializada (Guía Semana 6)
│   ├── error_sem5.txt        # División por cero con constante (Guía Semana 6)
│   ├── error_sem6.txt        # Violación de propiedad estocástica (probabilidades != 1.0)
│   ├── error_sem7.txt        # Estado no declarado en la cadena
│   ├── error_sin1.txt        # Error sintáctico (falta punto y coma)
│   └── warning1.txt          # Advertencia: variable declarada pero nunca usada
├── output/                   # Código de bajo nivel generado (*.c)
├── doc/                      # Documentación del Trabajo Parcial
│   ├── INFORME.md            # Informe técnico de 5 páginas para el Trabajo Parcial
│   ├── DERIVACIONES.md       # Derivaciones más a la izquierda paso a paso
│   ├── GUION_VIDEO.md        # Guion para el video demostrativo de 5 minutos
│   ├── DIAPOSITIVAS.md       # Estructura para la presentación en diapositivas (PDF)
│   └── BANCO_PREGUNTAS_DEFENSA.md # Preguntas teóricas clave para la sustentación
└── README.md
```

---

## Requisitos e Instalación

1. **Python 3.10+**:
   Instalar el runtime oficial de ANTLR4:
   ```bash
   pip install antlr4-python3-runtime==4.13.2
   ```

2. **Java Runtime (JDK 11+)**:
   Requerido para generar el código del parser desde el archivo `.g4`.

---

## Compilación de la Gramática

Para compilar `MarkovLang.g4` hacia la carpeta `gen/`:

* **En Linux / macOS / WSL:**
  ```bash
  make
  ```
* **En Windows (PowerShell / CMD):**
  ```cmd
  .\build.bat
  ```
* **Con Python:**
  ```bash
  python compile_grammar.py
  ```

---

## Ejecución del Compilador (`main.py`)

El driver analiza el archivo fuente, ejecuta el chequeo semántico, reporta errores o advertencias y genera el archivo de código en C de bajo nivel en `output/`:

```bash
python main.py <ruta_archivo.txt> [opciones]
```

### Opciones:
* `--tokens`: Imprime la lista de tokens reconocidos por el lexer.
* `--tree`: Muestra la representación textual del Parse Tree.

---

## Ejemplos de Prueba

### 1. Compilar modelo de clima y generar código C:
```bash
python main.py tests/entrada1_weather.txt
```
*Salida:*
```text
Análisis semántico: OK

[Compilación a Bajo Nivel] Código C generado en: output\entrada1_weather.c
```

### 2. Probar error semántico de dominio (Violación de propiedad estocástica):
```bash
python main.py tests/error_sem6.txt
```
*Salida:*
```text
=== ERRORES SEMÁNTICOS ===
  [Error Semántico, línea 4] Violación de propiedad estocástica en estado 'Sunny': las probabilidades salientes suman 1.3 (deben sumar exactamente 1.0)
```

### 3. Probar error semántico de estado no declarado:
```bash
python main.py tests/error_sem7.txt
```
*Salida:*
```text
=== ERRORES SEMÁNTICOS ===
  [Error Semántico, línea 8] Estado de destino 'Snowy' no declarado en la cadena 'Clima'
```

### 4. Probar detección de variable no inicializada (Guía Semana 6):
```bash
python main.py tests/error_sem4.txt
```

### 5. Probar detección de división por cero con constante (Guía Semana 6):
```bash
python main.py tests/error_sem5.txt
```

### 6. Probar advertencia de variable no usada:
```bash
python main.py tests/warning1.txt
```
