# OJO: En Python el for no acepta condiciones combinadas en su cabecera. Usar COMPRESION


#  range

for i in range(10)
for i in range(1, 10)
for i in range(1, 10, 2)
for i in range(10, 0, -1)

# listas

for nombre in ["Ana", "Luis", "Pepe"]
for numero in [1, 2, 3, 4, 5]
for palabra in ["hola", "mundo"]

# multiplles listas

for a, b in zip(lista1, lista2)

# diccionarios

for clave in diccionario
for valor in diccionario.values()
for clave, valor in diccionario.items()

# enumerate

for i, valor in enumerate(lista)
for i, letra in enumerate("hola")

# set

for elemento in {"rojo", "verde", "azul"}

# cadenas de texto

for letra in "python"

# booleanos y operadores

for nombre, completada in tareas:
for user in usuarios:
for nombre, lectura, escritura in archivos:

# comprensión de listas

[x for x in lista if x > 0]
[nombre for nombre in nombres if len(nombre) > 4]
[num for num in range(20) if num % 2 == 0]
[palabra for palabra in palabras if "a" in palabra]
[x**2 for x in range(100) if x**2 < 100]
[alumno for alumno in alumnos if alumno["nota"] >= 5]
[f for f in archivos if f.endswith(".txt")]
[palabra for palabra in lista if palabra != ""]
[fruta for fruta in frutas if fruta != "manzana"]
[x for x in lista if lista.count(x) == 1]