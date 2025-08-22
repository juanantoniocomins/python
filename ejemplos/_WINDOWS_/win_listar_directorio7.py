import os
import re

directorio = r"C:\Users\juan\Desktop"
extension = "lnk"

# Patrón regex para archivos que terminen en .txt (insensible a mayúsculas/minúsculas)
patron = re.compile(r".*\." + extension + "$", re.IGNORECASE)

for i, elemento in enumerate(os.listdir(directorio), start=1):
    ruta = os.path.join(directorio, elemento)

    if os.path.isfile(ruta) and patron.match(elemento):
        print(f"{i}. {elemento}")