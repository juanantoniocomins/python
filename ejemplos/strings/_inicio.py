# --------------------------------------------------------------crear cadenas

print("--------------------------------------------------------imprimir")

cad1 = "Esto es una cadena con comillas dobles"
cad2 = 'Esto es una cadena con comillas simples'
a = "Hola"
b = "Mundo"

print(f"{cad1} \n{cad2}")

# cadenas multilinea

opcion1 = '''Este es un
string
multilínea'''

opcion2 = """También
este es un
string multilínea"""

print(f"\n-------------\n{opcion1} \n-------------\n{opcion2}")

# --------------------------------------------------------------repetir

print("--------------------------------------------------------repetir")

print(f"{a * 3}")

# --------------------------------------------------------------indexacion

print("--------------------------------------------------------indexacion")

# Indexación
print(f"primero = {a[0]}")
print(f"ultimo {b[-1]}")

# --------------------------------------------------------------slicing

print("--------------------------------------------------------slicing")

print(f"{b[1:4]}")

# --------------------------------------------------------------comprobar inclusión

print("--------------------------------------------------------comprobar inclusión")

existe = 'a' in a
existe2 = 'X' in a

print(f"{existe}")
print(f"{existe2}")

