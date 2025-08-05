oficios = ['Arquitecto', 'Soldador', 'Montador', 'Arquitecto', 'Pintor', 'Albañil', 'Metal', 'Fontanero']
frutas = ["manzana", "pera", "uva"]

# acceso a los datos

print(f"{oficios[3]}")
print(f"{oficios[-1]}")
print(f"{oficios[:4]}")

# not y not in

print ("manzana" in frutas)
print ("manzana" not in frutas)

# metodo len

print(f"{len(oficios)} elementos.")

# metodo index

print(f"{oficios.index("Arquitecto")}") # la primera ocurrencia

# metoddo count

buscar = "Arquitecto"

print(f"{buscar} aparece {oficios.count(buscar)} veces.")

# consultar existencia: IF

if (buscar in oficios):
    print(f"{buscar} aparece en la lista")
else:
    print(f"{buscar} NO aparece en la lista")


if ("Alfredo" not in oficios):
    print("Alfredo, no aparece en la lista")
else:
    print("Si aparece en la lista")




