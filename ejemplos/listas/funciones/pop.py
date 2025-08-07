# Elimina y devuelve el elemento en la posición i de la lista.
# Si no se indica i, quita el último elemento.

numeros = [10, 20, 30, 50, 100]

elemento_eliminada = numeros.pop(0)

print(f"Hs eliminado el {elemento_eliminada}")

numeros.pop()

print(numeros)
