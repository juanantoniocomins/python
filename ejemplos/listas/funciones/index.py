# buscar la posición (índice) de la primera aparición del elemento x en la lista.


lista1 = ['a', 'b', 'c', 'b', 'd']
lista2 = [1, 2, 3, 2, 4]

buscar = 'b'

print(f"La {buscar} esta en la posición {lista1.index(buscar)}")

buscar2 = "z"

try:
    print(f"La {buscar2} esta en la posición {lista1.index(buscar2)}")
except:
    print(f"{buscar2}, no esta en: {lista1}")