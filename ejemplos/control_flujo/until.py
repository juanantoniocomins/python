# En Python no existe directamente una sentencia until como en otros lenguajes (por ejemplo, Bash o Ruby). Sin embargo, puedes simular el comportamiento de until con un bucle while utilizando una negación de la condición.

# until condicion:
#     instrucciones

# Se traduce a:

# while not condicion:
#    instrucciones

contador = 0

while not contador == 5:
    print(f"Contador actual: {contador}")
    contador += 1