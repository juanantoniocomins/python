# Une elementos de dos o más listas en tuplas.
# OJO: Cuando usas zip() con listas (o iterables) de distinto tamaño, zip se detiene cuando la lista más corta se acaba, es decir, solo combina elementos hasta donde todas las listas tienen datos.

# -------------------------------------------------------- Unir dos listas en tuplas

nombres = ['Ana', 'Luis', 'Carlos']
edades = [25, 30, 22]
ciudades = ['Madrid', 'Barcelona', 'Valencia']

combinado = list(zip(nombres, edades))
print(combinado)

# -------------------------------------------------------- Iterar con zip() en un bucle for


for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# -------------------------------------------------------- Unir tres listas

combinado = list(zip(nombres, edades, ciudades))
print(combinado)

# -------------------------------------------------------- 




# -------------------------------------------------------- 