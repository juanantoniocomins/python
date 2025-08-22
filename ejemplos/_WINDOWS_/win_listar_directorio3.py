import os
import re

usuario = "juan"
directorio = "C:\\Users\\" + usuario + "\\Desktop"
contador_fich = 0
contador_dir = 0

for i, archivo in enumerate(os.listdir(directorio), start=1):
    patron = re.compile(r".*\.\w+$", re.IGNORECASE)  # << extensión de 1 o más caracteres
    
    if patron.match(archivo):
        contador_fich += 1
    else: 
        contador_dir += 1

print("")
print(f"Hay {contador_fich} ficheros y {contador_dir} directorios en {directorio}")
