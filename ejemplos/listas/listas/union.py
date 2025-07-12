# " ".join(lista) une cada palabra con un espacio entre ellas.
# ¡Ojo! Todos los elementos deben ser strings

lista = ["Hola", "Juanan", "¿cómo", "estás?"]
resultado = " ".join(lista)

print(resultado)

# Con coma

nombres = ["Ana", "Luis", "Carlos"]
print(", ".join(nombres))

# Con guiones

print("-".join(nombres))


# Sin ningún separador

print("".join(nombres))

# unir lineas de texto

lineas = ["Primera línea", "Segunda línea", "Tercera línea"]
texto = "\n".join(lineas)
print(texto)

# caracteres

print("".join(['P', 'y', 't', 'h', 'o', 'n']))

