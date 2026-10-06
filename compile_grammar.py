import os
import sys
import subprocess
import glob

def find_java():
    home_dir = os.path.expanduser("~")
    jdk_dirs = glob.glob(os.path.join(home_dir, ".jdk", "*", "bin", "java.exe"))
    if jdk_dirs:
        return jdk_dirs[0]

    java_home = os.environ.get("JAVA_HOME")
    if java_home:
        java_bin = os.path.join(java_home, "bin", "java.exe" if os.name == 'nt' else "java")
        if os.path.exists(java_bin):
            return java_bin

    return "java"

def compile_grammars():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    jar_path = os.path.join(base_dir, "antlr-4.13.2-complete.jar")
    out_dir = os.path.join(base_dir, "gen")
    g4_path = os.path.join(base_dir, "MarkovLang.g4")

    os.makedirs(out_dir, exist_ok=True)
    
    init_file = os.path.join(out_dir, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, "w") as f:
            f.write("# Generated ANTLR package\n")

    java_cmd = find_java()
    print(f"[*] Usando Java: {java_cmd}")
    print(f"[*] Generando código Python3 desde MarkovLang.g4 en {out_dir}...")

    cmd = [
        java_cmd,
        "-jar", jar_path,
        "-Dlanguage=Python3",
        "-visitor",
        "-o", out_dir,
        g4_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("[ERROR] Falló la compilación de la gramática con ANTLR:")
        print(result.stderr)
        sys.exit(result.returncode)
    else:
        print("[OK] Gramática MarkovLang.g4 compilada exitosamente en:", out_dir)
        if result.stdout.strip():
            print(result.stdout)

if __name__ == "__main__":
    compile_grammars()
