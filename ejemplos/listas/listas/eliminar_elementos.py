
oficios = ['Arquitecto', 'Soldador', 'Montador', 'Arquitecto', 'Pintor', 'Albañil', 'Metal', 'Fontanero']

# metodo remove, elimina la primera ocurrencia

oficios.remove("Arquitecto")
print(oficios)

# metodo pop

oficios.pop(-1) # ultimo
print(oficios)

# del elimina un elemento

del oficios[0]
print(oficios)

del oficios[0:3] # elimina dee inicio a fin -1
print(oficios)

# metodo clear

oficios.clear() # vaciamos la lista
print(oficios)