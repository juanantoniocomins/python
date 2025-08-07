# Convierte un iterable (como una cadena o un conjunto) en una lista.

# -------- texto: 

texto = "hola"
lista = list(texto)
print(lista)

# --------  convertir un conjunto (set) en una lista:

conjunto = {10, 20, 30}
lista1 = list(conjunto)
print(lista1)

# -------- convertir una tupla en una lista:

tupla = (1, 2, 3, 4)
lista2 = list(tupla)
print(lista2)

# -------- convertir un range en una lista

rango = range(5)
lista3 = list(rango)
print(lista3)

# -------- convertir un diccionario en una lista (de sus claves)

diccionario = {'a': 1, 'b': 2, 'c': 3}
lista4 = list(diccionario)
print(lista4)

# -------- convertir un diccionario en una lista de pares (tuplas clave-valor)

diccionario2 = {'a': 1, 'b': 2, 'c': 3}
lista5 = list(diccionario2.items())
print(lista5)

# -------- convertir un generador en una lista

generador = (x*x for x in range(5))
lista6 = list(generador)
print(lista6)

# -------- convertir un map en una lista

numeros = [1, 2, 3]
resultado = map(lambda x: x + 10, numeros)
lista7 = list(resultado)
print(lista7)

# -------- convertir un filter en una lista

numeros2 = [1, 2, 3, 4, 5]
resultado2 = filter(lambda x: x % 2 == 0, numeros2)
lista8 = list(resultado2)
print(lista8)