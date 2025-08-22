import os

usu = "juan"
directorio = "C:\\Users\\" + usu + "\\Desktop"
cont = 0


for i, archivo in enumerate(os.listdir(directorio), start=1):
    print(f"{archivo}")
    cont += 1

print("")
print(f"Hay un total de {cont} objetos en {directorio}")