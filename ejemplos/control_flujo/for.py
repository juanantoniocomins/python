# for variable in iterable:
    # Código que se repite

# variable: toma el valor de cada elemento del iterable.
# iterable: puede ser una lista, una cadena, un rango, etc.

# uso de un rango

for i in range(5):
    print("Valor de i:", i)

for i in range(0, 11, 2):
    print(i)

# uso de iterable: lista

nombres = ["Ana", "Luis", "Pedro", "Marta"]

for nombre in nombres:
    print("Hola", nombre)

# uso de iterable: tupla

coordenadas = (10, 20, 30)

for valor in coordenadas:
    print("Valor:", valor)

# uso de iterable: diccionario

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Valencia"}

for clave, valor in persona.items():
    print(clave, "->", valor)

# recorrer una cadena

mensaje = "Hola"

for letra in mensaje:
    print(letra)



