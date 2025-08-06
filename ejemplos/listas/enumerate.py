# Devuelve un iterable con tuplas (índice, valor). Muy útil en bucles.

# --------------------------------------- Recorrer una lista con índice y valor

frutas = ['manzana', 'banana', 'cereza']

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}") 

# --------------------------------------- Empezar la numeración desde 1 en vez de 0

for indice, fruta in enumerate(frutas, start=1):
    print(f"{indice}: {fruta}")

# --------------------------------------- Crear una lista de tuplas (índice, valor) a partir de una cadena

texto = "hola"
lista = list(enumerate(texto))
print(lista)

# --------------------------------------- Usar enumerate() con listas modificables para actualizar valores con índice

numeros = [10, 20, 30, 40]

for i, valor in enumerate(numeros):
    numeros[i] = valor + 5

print(numeros)
