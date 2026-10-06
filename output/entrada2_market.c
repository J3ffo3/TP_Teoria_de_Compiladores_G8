// ==============================================================
// Código generado automáticamente por el Compilador MarkovLang
// Lenguaje destino: C (Bajo nivel / Código Intermedio)
// ==============================================================
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// --- Cadena de Markov: Market ---
#define MARKET_NUM_STATES 3
typedef enum {
    STATE_MARKET_Bull = 0,
    STATE_MARKET_Bear = 1,
    STATE_MARKET_Stagnant = 2,
} Market_State;

const char* Market_names[] = {
    "Bull",
    "Bear",
    "Stagnant",
};

float Market_P[3][3] = {
    { 0.9000f, 0.0750f, 0.0250f },
    { 0.1500f, 0.8000f, 0.0500f },
    { 0.2500f, 0.2500f, 0.5000f },
};

void simulate_Market(int start_state, int steps) {
    printf("[C Simulación Monte Carlo] Cadena 'Market' por %d pasos:\n", steps);
    int current = start_state;
    printf("  Paso 0: %s\n", Market_names[current]);
    for (int t = 1; t <= steps; t++) {
        float r = (float)rand() / (float)RAND_MAX;
        float cumulative = 0.0f;
        int next_state = current;
        for (int j = 0; j < 3; j++) {
            cumulative += Market_P[current][j];
            if (r <= cumulative) {
                next_state = j;
                break;
            }
        }
        current = next_state;
        if (t <= 10 || t == steps) {
            printf("  Paso %d: %s\n", t, Market_names[current]);
        } else if (t == 11) {
            printf("  ...\n");
        }
    }
}

void stationary_Market() {
    printf("[C Distribución Estacionaria] Cadena 'Market':\n");
    // Aproximación por potencias P^k
    float M[3][3];
    for(int i=0; i<3; i++) for(int j=0; j<3; j++) M[i][j] = Market_P[i][j];
    for (int iter = 0; iter < 50; iter++) {
        float Temp[3][3] = {0};
        for(int i=0; i<3; i++)
            for(int j=0; j<3; j++)
                for(int k=0; k<3; k++)
                    Temp[i][j] += M[i][k] * M[k][j];
        for(int i=0; i<3; i++) for(int j=0; j<3; j++) M[i][j] = Temp[i][j];
    }
    for (int j = 0; j < 3; j++) {
        printf("  pi(%s) = %.4f\n", Market_names[j], M[0][j]);
    }
}

int main() {
    srand(1234);
    printf("=== Ejecutando Codigo Compilado de MarkovLang ===\n\n");
    simulate_Market(STATE_MARKET_Bull, 50);
    printf("\n");
    stationary_Market();
    printf("\n");
    return 0;
}
