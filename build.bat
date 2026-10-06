@echo off
echo ====================================================
echo  Compilando MarkovLang.g4 con ANTLR4 a gen/
echo ====================================================
python compile_grammar.py
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [OK] Compilacion completada con exito en gen/
) else (
    echo.
    echo [ERROR] Ocurrio un error al compilar la gramatica.
)
