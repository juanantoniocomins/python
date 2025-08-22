import os

usuario = "juan"
directorio = "C:\\Users\\" + usuario + "\\Desktop"

for i, archivo in enumerate(os.listdir(directorio), start=1):
    print(f"{archivo}")