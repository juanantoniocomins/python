cadena = input("Introduce una frase: ")
palabras = cadena.split()

acronimo = ""

for palabra in palabras:
    acronimo = acronimo + palabra[0].upper()

print(f"Acrónimo: {acronimo}")