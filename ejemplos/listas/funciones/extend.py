# Agrega todos los elementos de un iterable (como otra lista, una cadena, una tupla…) al final de la lista original.

lista_original = ["Juan", "Pedro", "Ángel"]
segunda_lista = [45, 56, 78]
tupla = ("Ana", True, 10.15)
diccionario = {"Raiz": "Arbol", "Manzano": "Manzana"}

lista_original.extend(segunda_lista)

print(lista_original)

lista_original.extend(tupla)

print(lista_original)

lista_original.extend(diccionario)

print(lista_original)