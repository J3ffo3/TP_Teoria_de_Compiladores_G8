# Voltio - Lenguaje de Dominio Especifico para Circuitos Electricos

Voltio es un DSL disenado para el calculo, verificacion y dimensionamiento de circuitos electricos e instalaciones energeticas. Posee tipos nativos con magnitudes fisicas (voltaje, corriente, potencia, resistencia, energia, tiempo) que permiten al compilador verificar la coherencia dimensional en tiempo de compilacion (Ley de Ohm y Ley de Potencia).

Proyecto del curso Teoria de Compiladores (1ACC0218), UPC, ciclo 2026-2.

## Estado del Proyecto (Hito 2)
- Gramatica en forma estandar BNF pura (sin ?, *, + ni subreglas).
- Analizador lexico y sintactico en ANTLR4.
- 28 derivaciones mas a la izquierda verificadas sin ambiguedad.
- Analizador semantico completo con tabla de simbolos por ambitos y 13 errores formales (SEM-01 a SEM-13).
- Generacion de codigo intermedio LLVM IR (avance Hito 2).
- Suite de pruebas automatizadas con unittest (100% aprobadas).

## Requisitos
- Python 3.10+
- antlr4-python3-runtime==4.13.1
- llvmlite

## Comandos Principales
- Verificar gramatica: python3 scripts/verificar_gramatica.py
- Generar derivaciones: python3 scripts/derivaciones.py
- Ejecutar pruebas: python3 -m unittest discover -s tests -v
- Compilar a LLVM IR: python3 src/voltio.py ejemplos/dimensionamiento.vo --llvm
