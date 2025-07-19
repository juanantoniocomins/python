import os
import time

ancho = 20

for i in range(ancho +1):
    porcentaje = int(i / ancho * 100)
    os.system("clear") # cls si windows
    barra = "#" * i + "-" * (ancho-i)
    print(f"{barra}{porcentaje}%")
    time.sleep(0.1)