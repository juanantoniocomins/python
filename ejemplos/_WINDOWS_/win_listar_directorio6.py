import os

directorio = r"C:\Users\juan\Desktop"

for i, elemento in enumerate(os.listdir(directorio), start=1):
    ruta = os.path.join(directorio, elemento)  # construimos la ruta completa

    if os.path.isfile(ruta):
        print(f"{i}. {elemento} --> Fichero")
    elif os.path.isdir(ruta):
        print(f"{i}. {elemento} --> Directorio")
    else:
        print(f"{i}. {elemento} --> Desconocido")