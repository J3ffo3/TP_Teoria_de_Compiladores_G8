// ==============================================================
// Código generado automáticamente por el Compilador MarkovLang
// Lenguaje destino: C (Bajo nivel / Código Intermedio)
// ==============================================================
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// --- Cadena de Markov: Weather ---
#define WEATHER_NUM_STATES 2
typedef enum {
    STATE_WEATHER_Sunny = 0,
    STATE_WEATHER_Rainy = 1,
} Weather_State;

const char* Weather_names[] = {
    "Sunny",
    "Rainy",
};

float Weather_P[2][2] = {
    { 0.8000f, 0.2000f },
    { 0.4000f, 0.6000f },
};

void simulate_Weather(int start_state, int steps) {
    printf("[C Simulación Monte Carlo] Cadena 'Weather' por %d pasos:\n", steps);
    int current = start_state;
    printf("  Paso 0: %s\n", Weather_names[current]);
    for (int t = 1; t <= steps; t++) {
        float r = (float)rand() / (float)RAND_MAX;
        float cumulative = 0.0f;
        int next_state = current;
        for (int j = 0; j < 2; j++) {
            cumulative += Weather_P[current][j];
            if (r <= cumulative) {
                next_state = j;
                break;
            }
        }
        current = next_state;
        if (t <= 10 || t == steps) {
            printf("  Paso %d: %s\n", t, Weather_names[current]);
        } else if (t == 11) {
            printf("  ...\n");
        }
    }
}

void stationary_Weather() {
    printf("[C Distribución Estacionaria] Cadena 'Weather':\n");
    // Aproximación por potencias P^k
    float M[2][2];
    for(int i=0; i<2; i++) for(int j=0; j<2; j++) M[i][j] = Weather_P[i][j];
    for (int iter = 0; iter < 50; iter++) {
        float Temp[2][2] = {0};
        for(int i=0; i<2; i++)
            for(int j=0; j<2; j++)
                for(int k=0; k<2; k++)
                    Temp[i][j] += M[i][k] * M[k][j];
        for(int i=0; i<2; i++) for(int j=0; j<2; j++) M[i][j] = Temp[i][j];
    }
    for (int j = 0; j < 2; j++) {
        printf("  pi(%s) = %.4f\n", Weather_names[j], M[0][j]);
    }
}

int main() {
    srand(42);
    printf("=== Ejecutando Codigo Compilado de MarkovLang ===\n\n");
    simulate_Weather(STATE_WEATHER_Sunny, 10);
    printf("\n");
    stationary_Weather();
    printf("\n");
    return 0;
}
