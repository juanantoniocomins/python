import os

respuesta = os.system("ping 8.8.8.8 -n 1")
if respuesta == 0:
    print("✅ Conectado a Internet")
else:
    print("❌ Sin conexión")