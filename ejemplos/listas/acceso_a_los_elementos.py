alumnos = ["Juan", "Eli", "Angel", "Sergio", "Raquel", "Nerea", "Rafael"]
numeros = [12, 23, 45, 67, 101, 1]

# acceso individual

print (f"El primer alumno es {alumnos[0]}")
print (f"El último alumno es {alumnos[-1]}") # al reves con el signo -

# acceso mediante rango

print (f"{alumnos[1:4]}") # desde el 1 al 3, es decir, el 4 no lo tiene en cuenta

# metodo enumerate

print(list(enumerate(alumnos))) # indice + valor

# valor maximo

print(f"{max(alumnos)}")

# valor minimo

print(f"{min(alumnos)}")

# suma valores

print(f"{sum(numeros)}")