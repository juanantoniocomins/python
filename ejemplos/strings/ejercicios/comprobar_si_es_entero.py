cadena = input("Introduce algo: ")

if cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit()):
    print(f"{cadena} es un entero.")
else: 
    print(f"{cadena} NO es un entero.")