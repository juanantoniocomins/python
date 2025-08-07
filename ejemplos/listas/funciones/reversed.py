# Devuelve un iterador con los elementos al revés.

lista = [1, 2, 3, 4, 5]

for elemento in reversed(lista):
    print(elemento)


# -------------------------------------------------- Convertir el resultado de reversed() en una nueva lista (lista invertida)

lista2 = ['a', 'b', 'c', 'd']
lista_invertida = list(reversed(lista2))
print(lista_invertida)