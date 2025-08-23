import os

hosts = ["8.8.8.8", "1.1.1.1", "www.google.com"]

for host in hosts:
    respuesta = os.system(f"ping {host} -n 1 >nul")
    if respuesta == 0:
        print(f"✅ Conectado a {host}")
    else:
        print(f"❌ No responde {host}")        