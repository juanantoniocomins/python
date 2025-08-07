# Elimina la primera aparición del valor x en la lista.

lista = [123, 321, 456, 789, 900, True, 111, False, 9080, False]

lista.remove(False)

print(lista)

try:
    lista.remove(11)
    print(lista)
except ValueError:
    print("No se ha econtraddo el valor indicado")