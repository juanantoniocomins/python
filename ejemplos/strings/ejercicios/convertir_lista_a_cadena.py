# capitalizar cada palabra

cadena2 = "hola mundo"
palabras = cadena2.split()

print(palabras )

for i in range(len(palabras)):
    palabras[i] = palabras[i].capitalize()  # Cambia la palabra actual

cadena_final = " ".join(palabras)# Unir de nuevo la lista en una sola cadena
print(f"Resultado final: {cadena_final}")