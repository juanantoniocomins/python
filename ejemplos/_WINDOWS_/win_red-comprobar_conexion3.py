import subprocess

host = "8.8.8.8"
try:
    resultado = subprocess.check_output(["ping", host, "-n", "1"], text=True)
    print("✅ Conectado. Detalles:")
    print(resultado)
except subprocess.CalledProcessError:
    print("❌ Error de conexión")
