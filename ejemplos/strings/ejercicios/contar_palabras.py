cadena = input("Introduce algo: ")

# .split() separa por espacios y devuelve una lista de palabras
palabras = cadena.split()

# Contamos el número de elementos en la lista
total = len(palabras)

print(f"El total de palabras = {total}")