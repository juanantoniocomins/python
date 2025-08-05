alumnos = ["Juan", "Eli", "Angel", "Sergio", "Raquel"]

# metodo append

alumnos.append("Vicente") # agregar un elemento, se agrega al final
print(alumnos)

oficios = [] # podemos crear una lista vacia e ir añadiendo
oficios.append("Soldador")
oficios.append("Montador")
oficios.append("Pintor")
print(oficios)

# metodo extend

nuevos_oficios = ("Albañil", "Metal", "Fontanero")
oficios.extend(nuevos_oficios)
print(oficios)

# metodo insert

oficios.insert(0, "Arquitecto")
print(oficios)
