numeros = [[1, 2], [3, 4], [5, 6]]

# acceso

print(numeros)
print(numeros[1])
print(numeros[0][1]) 

# modificacion

numeros[1][0] = 99
print(numeros)

# iterar

for fila in numeros:
    for numero in fila:
        print(numero)

# añadir sublistas

colores = []
colores.append(["rojo", "verde"])
colores.append(["azul", "amarillo"])
print(colores)