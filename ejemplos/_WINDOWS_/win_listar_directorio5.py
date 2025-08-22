import os
import re

usuario = "juan"
directorio = "C:\\Users\\" + usuario + "\\Desktop"

try:
    contador_fich = 0
    contador_dir = 0

    for i, archivo in enumerate(os.listdir(directorio), start=1):
        patron = re.compile(r".*\.\w+$", re.IGNORECASE)

        if patron.match(archivo):
            contador_fich += 1
        else:
            contador_dir += 1

    print(f"Hay {contador_fich} ficheros y {contador_dir} directorios en {directorio}")

except FileNotFoundError:
    print(f"❌ Error: el directorio {directorio} no existe.")