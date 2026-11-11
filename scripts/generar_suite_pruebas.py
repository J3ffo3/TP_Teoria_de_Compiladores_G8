import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_TESTS = os.path.join(RAIZ, "tests")

os.makedirs(os.path.join(DIR_TESTS, "semantico", "validos"), exist_ok=True)
os.makedirs(os.path.join(DIR_TESTS, "semantico", "invalidos"), exist_ok=True)
os.makedirs(os.path.join(DIR_TESTS, "sintactico", "validos"), exist_ok=True)
os.makedirs(os.path.join(DIR_TESTS, "sintactico", "invalidos"), exist_ok=True)

# 1. Casos semanticos validos
with open(os.path.join(DIR_TESTS, "semantico", "validos", "01_ley_ohm.vo"), "w", encoding="utf-8") as f:
    f.write("""// espera: OK
const TENSION: voltaje<V> = 220 V;
const RESISTENCIA_CARGA: resistencia<OHM> = 44 OHM;
var corrienteLinea: corriente<A> = TENSION / RESISTENCIA_CARGA;
var potenciaConsumo: potencia<W> = TENSION * corrienteLinea;
mostrar("Corriente:", corrienteLinea, "Potencia:", potenciaConsumo);
""")

with open(os.path.join(DIR_TESTS, "semantico", "validos", "02_control_flujo.vo"), "w", encoding="utf-8") as f:
    f.write("""// espera: OK
var energiaAcumulada: energia<KWH> = 0 KWH;
para dia desde 1 hasta 7 {
    var consumoDiario: potencia<KW> = 5 KW;
    energiaAcumulada += consumoDiario * 24 H;
}
mientras (energiaAcumulada > 0 KWH) {
    energiaAcumulada -= 10 KWH;
}
""")

# 2. Casos semanticos invalidos (uno por cada error clave)
invalidos = [
    ("01_no_declarada.vo", """// espera: SEM-01@3
var v: voltaje<V> = 220 V;
var i: corriente<A> = v / resistenciaDesconocida;
"""),
    ("02_redeclaracion.vo", """// espera: SEM-02@3
var corrienteFase: corriente<A> = 10 A;
var corrienteFase: corriente<A> = 20 A;
"""),
    ("03_unidades_incompatibles.vo", """// espera: SEM-03@3
var v: voltaje<V> = 220 V;
var sumaInvalida: voltaje<V> = v + 15 A;
"""),
    ("04_tipos_incompatibles.vo", """// espera: SEM-04@2
var v: voltaje<V> = "Alta Tension";
"""),
    ("05_modificar_constante.vo", """// espera: SEM-05@3
const VOLTAJE_NOMINAL: voltaje<V> = 220 V;
VOLTAJE_NOMINAL = 230 V;
"""),
    ("06_condicion_no_booleana.vo", """// espera: SEM-06@2
si (220 V) {
    mostrar("Tension activa");
}
"""),
    ("07_retornar_fuera_regla.vo", """// espera: SEM-07@2
retornar 220 V;
"""),
    ("08_retorno_incompatible.vo", """// espera: SEM-08@2
regla medir(): voltaje<V> {
    retornar 15 A;
}
"""),
    ("09_aridad_incorrecta.vo", """// espera: SEM-09@4
regla potencia(v: voltaje<V>, i: corriente<A>): potencia<W> {
    retornar v * i;
}
var p: potencia<W> = potencia(220 V);
"""),
    ("10_division_cero.vo", """// espera: SEM-13@2
var i: corriente<A> = 220 V / 0 OHM;
"""),
]

for nombre, contenido in invalidos:
    with open(os.path.join(DIR_TESTS, "semantico", "invalidos", nombre), "w", encoding="utf-8") as f:
        f.write(contenido)

print("[OK] Casos de prueba semanticos generados exitosamente.")
