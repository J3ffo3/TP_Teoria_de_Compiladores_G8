"""
Generador de Código de Bajo Nivel (C) para MarkovLang
Traduce las abstracciones de alto nivel (estados, transiciones probabilísticas)
a estructuras de datos estáticas en C (matrices planas, enums, simulación Monte Carlo).
"""

import os

def generate_c_code(chains, simulations, seed, output_c_path):
    os.makedirs(os.path.dirname(os.path.abspath(output_c_path)), exist_ok=True)

    lines = [
        "// ==============================================================",
        "// Código generado automáticamente por el Compilador MarkovLang",
        "// Lenguaje destino: C (Bajo nivel / Código Intermedio)",
        "// ==============================================================",
        "#include <stdio.h>",
        "#include <stdlib.h>",
        "#include <time.h>",
        "",
    ]

    # Para cada cadena, generar enums, matriz de transición y funciones en C
    for chain_name, chain in chains.items():
        n = len(chain.states)
        lines.append(f"// --- Cadena de Markov: {chain_name} ---")
        lines.append(f"#define {chain_name.upper()}_NUM_STATES {n}")
        
        # Enum de estados
        lines.append(f"typedef enum {{")
        for i, s in enumerate(chain.states):
            lines.append(f"    STATE_{chain_name.upper()}_{s} = {i},")
        lines.append(f"}} {chain_name}_State;")
        lines.append("")

        # Nombres de estados como strings
        lines.append(f"const char* {chain_name}_names[] = {{")
        for s in chain.states:
            lines.append(f'    "{s}",')
        lines.append("};")
        lines.append("")

        # Matriz de transición plana en C
        lines.append(f"float {chain_name}_P[{n}][{n}] = {{")
        for s_from in chain.states:
            row_vals = []
            for s_to in chain.states:
                prob = chain.transitions.get((s_from, s_to), 0.0)
                row_vals.append(f"{prob:.4f}f")
            lines.append("    { " + ", ".join(row_vals) + " },")
        lines.append("};")
        lines.append("")

        # Función de simulación Monte Carlo de bajo nivel
        lines.append(f"void simulate_{chain_name}(int start_state, int steps) {{")
        lines.append(f'    printf("[C Simulación Monte Carlo] Cadena \'{chain_name}\' por %d pasos:\\n", steps);')
        lines.append(f"    int current = start_state;")
        lines.append(f'    printf("  Paso 0: %s\\n", {chain_name}_names[current]);')
        lines.append(f"    for (int t = 1; t <= steps; t++) {{")
        lines.append(f"        float r = (float)rand() / (float)RAND_MAX;")
        lines.append(f"        float cumulative = 0.0f;")
        lines.append(f"        int next_state = current;")
        lines.append(f"        for (int j = 0; j < {n}; j++) {{")
        lines.append(f"            cumulative += {chain_name}_P[current][j];")
        lines.append(f"            if (r <= cumulative) {{")
        lines.append(f"                next_state = j;")
        lines.append(f"                break;")
        lines.append(f"            }}")
        lines.append(f"        }}")
        lines.append(f"        current = next_state;")
        lines.append(f'        if (t <= 10 || t == steps) {{')
        lines.append(f'            printf("  Paso %d: %s\\n", t, {chain_name}_names[current]);')
        lines.append(f'        }} else if (t == 11) {{')
        lines.append(f'            printf("  ...\\n");')
        lines.append(f'        }}')
        lines.append(f"    }}")
        lines.append(f"}}\n")

        # Función para calcular distribución estacionaria (Potenciación de Matriz)
        lines.append(f"void stationary_{chain_name}() {{")
        lines.append(f'    printf("[C Distribución Estacionaria] Cadena \'{chain_name}\':\\n");')
        lines.append(f"    // Aproximación por potencias P^k")
        lines.append(f"    float M[{n}][{n}];")
        lines.append(f"    for(int i=0; i<{n}; i++) for(int j=0; j<{n}; j++) M[i][j] = {chain_name}_P[i][j];")
        lines.append(f"    for (int iter = 0; iter < 50; iter++) {{")
        lines.append(f"        float Temp[{n}][{n}] = {{0}};")
        lines.append(f"        for(int i=0; i<{n}; i++)")
        lines.append(f"            for(int j=0; j<{n}; j++)")
        lines.append(f"                for(int k=0; k<{n}; k++)")
        lines.append(f"                    Temp[i][j] += M[i][k] * M[k][j];")
        lines.append(f"        for(int i=0; i<{n}; i++) for(int j=0; j<{n}; j++) M[i][j] = Temp[i][j];")
        lines.append(f"    }}")
        lines.append(f"    for (int j = 0; j < {n}; j++) {{")
        lines.append(f'        printf("  pi(%s) = %.4f\\n", {chain_name}_names[j], M[0][j]);')
        lines.append(f"    }}")
        lines.append(f"}}\n")

    # Función main en C
    lines.append("int main() {")
    if seed is not None:
        lines.append(f"    srand({seed});")
    else:
        lines.append("    srand((unsigned int)time(NULL));")
    lines.append('    printf("=== Ejecutando Codigo Compilado de MarkovLang ===\\n\\n");')

    for sim in simulations:
        c_name = sim['chain'].name
        if sim['type'] == 'simulate':
            start_s = sim['start_state']
            steps = sim['steps']
            lines.append(f"    simulate_{c_name}(STATE_{c_name.upper()}_{start_s}, {steps});")
            lines.append('    printf("\\n");')
        elif sim['type'] == 'stationary':
            lines.append(f"    stationary_{c_name}();")
            lines.append('    printf("\\n");')

    lines.append("    return 0;")
    lines.append("}")

    with open(output_c_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    return True
