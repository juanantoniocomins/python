oficios = ['Arquitecto', 'Soldador', 'Montador', 'Arquitecto', 'Pintor', 'Albañil', 'Metal', 'Fontanero']
nombres = ["Ana", "Carlos", "Beatriz", "David", "Elena", "Fernando", "Gloria", "Héctor", "Irene", "Javier"]


# slicing

lista = oficios[0:4] # inicio a final -1

print(lista)

# metodo copy

nueva = oficios.copy()

print(nueva)

# meotodo list

nueva_lista = list(nueva)

print(nueva_lista)

# metodo zip

union = zip(oficios, nombres)

print(list(union))