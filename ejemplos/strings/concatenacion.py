# los string pueden ir entre comillas simples o dobles

nom = "Juan"
ape = "Perez"

print(f"{nom} {ape}")

# podemos concatenar con el signo +

usu = nom + " " + ape
usuario = "Pedro Alonso"

print(f"{usu}")
print ("Me llamo " + usuario)

# solo se pueden concatenar cadenas con + si es con numeros tendremos que usar: 

edad = 22

print("Tengo " + str(edad) + " años.")

# se puede declarar un string on n lineas, usando tres conillas simples o dobles

cadena = """En un lugar de la Mancha,
de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo
de los de lanza en astillero,
adarga antigua, rocín flaco y galgo corredor."""

print(cadena)
