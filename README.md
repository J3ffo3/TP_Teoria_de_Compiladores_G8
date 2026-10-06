# MarkovLang

**Curso:** Teoría de Compiladores (Ciclo 2026-2)  
**Docente:** Prof. José Luis Soncco Álvarez  
**Grupo:** Grupo 8  
**Entrega:** Trabajo Parcial (Hito 1 - Semana 7)  

MarkovLang es un lenguaje de dominio específico (DSL) diseñado para el modelado, verificación estática y compilación de **Cadenas de Markov de Tiempo Discreto (DTMC)**. El compilador valida reglas semánticas y estocásticas en tiempo de compilación y traduce las cadenas a **código ejecutable en C de bajo nivel** (matrices de adyacencia estáticas, simulaciones de Monte Carlo y cálculo de distribuciones estacionarias).

---

## Estructura del Proyecto

```text
TP1/
├── MarkovLang.g4             # Gramática formal del lenguaje (ANTLR4)
├── Makefile                  # Automatización de generación de código ANTLR4
├── build.bat                 # Script de compilación para Windows
├── compile_grammar.py        # Script auxiliar de compilación ANTLR4
├── main.py                   # Driver principal del compilador
├── codegen.py                # Generador de código C
├── gen/                      # Archivos generados por ANTLR4 (Lexer, Parser, Visitor)
├── semantic/                 # Analizador semántico y tabla de símbolos
│   ├── errors.py             # Clase SemanticError
│   ├── symbol_table.py       # Tabla de símbolos con soporte de ámbitos
│   └── semantic_visitor.py   # Visitor semántico (tipos, variables, propiedad estocástica)
├── tests/                    # Casos de prueba
│   ├── entrada1_weather.txt  # Modelo climático + simulación Monte Carlo
│   ├── entrada2_market.txt   # Modelo de mercado financiero + distribución estacionaria
│   ├── entrada3.txt          # Estructuras de control y expresiones
│   ├── error_sem1.txt        # Variable no declarada
│   ├── error_sem2.txt        # Variable redeclarada en el mismo ámbito
│   ├── error_sem3.txt        # Incompatibilidad de tipos
│   ├── error_sem4.txt        # Variable usada sin inicializar
│   ├── error_sem5.txt        # División entre cero con constante
│   ├── error_sem6.txt        # Violación de propiedad estocástica (suma != 1.0)
│   ├── error_sem7.txt        # Estado no declarado en la cadena
│   ├── error_sin1.txt        # Error de sintaxis (falta ';')
│   └── warning1.txt          # Advertencia de variable no utilizada
├── output/                   # Archivos C generados
├── doc/                      # Documentación del trabajo
│   ├── INFORME.md            # Informe técnico del Trabajo Parcial
│   └── DERIVACIONES.md       # Derivaciones formales más a la izquierda
└── README.md
```

---

## Requisitos e Instalación

1. **Python 3.10+** con el runtime de ANTLR4:
   ```bash
   pip install antlr4-python3-runtime==4.13.2
   ```

2. **Java Runtime (JDK 11+)** para compilar la gramática `.g4`.

---

## Compilación de la Gramática

Para regenerar los archivos en `gen/` a partir de `MarkovLang.g4`:

* **Linux / macOS:**
  ```bash
  make
  ```
* **Windows (PowerShell / CMD):**
  ```cmd
  .\build.bat
  ```
* **Con Python:**
  ```bash
  python compile_grammar.py
  ```

---

## Uso del Compilador

El archivo `main.py` recibe el archivo de código fuente y opcionalmente flags de depuración:

```bash
python main.py <archivo.txt> [--tokens] [--tree]
```

### Opciones:
* `--tokens`: Muestra la lista de tokens generada por el analizador léxico.
* `--tree`: Muestra el árbol de análisis sintáctico (Parse Tree) en formato texto.

---

## Ejemplos de Ejecución

### 1. Compilación válida y generación de código C:
```bash
python main.py tests/entrada1_weather.txt
```
Salida:
```text
Análisis semántico: OK

[Compilación a Bajo Nivel] Código C generado en: output\entrada1_weather.c
```

Para compilar y ejecutar el C generado:
```bash
gcc output/entrada1_weather.c -o weather.exe
./weather.exe
```

### 2. Detección de error semántico (Propiedad estocástica):
```bash
python main.py tests/error_sem6.txt
```
Salida:
```text
=== ERRORES SEMÁNTICOS ===
  [Error Semántico, línea 4] Violación de propiedad estocástica en estado 'Sunny': las probabilidades salientes suman 1.3 (deben sumar exactamente 1.0)
```

### 3. Detección de variable no inicializada:
```bash
python main.py tests/error_sem4.txt
```
Salida:
```text
=== ERRORES SEMÁNTICOS ===
  [Error Semántico, línea 4] Variable 'a' utilizada sin haber sido inicializada
```

### 4. Advertencia de variable no usada:
```bash
python main.py tests/warning1.txt
```
Salida:
```text
Análisis semántico: OK

=== ADVERTENCIAS ===
  [Línea 2] Variable 'y' fue declarada pero nunca utilizada
```
