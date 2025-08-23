import time, os

while True:
    respuesta = os.system("ping 8.8.8.8 -n 1 >nul")
    if respuesta == 0:
        print("✅ Conectado a Internet")
    else:
        print("❌ Sin conexión")
    time.sleep(5)  # espera 5 segundos antes de volver a probar
