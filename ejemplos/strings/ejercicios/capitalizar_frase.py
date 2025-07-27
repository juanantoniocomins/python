cadena = input("Introduce algo: ")
cadena = cadena.lower()  # Todo en minúscula
resultado = ""

capitalizar = True  # Capitalizar el primer carácter

for letra in cadena:
    if capitalizar and letra.isalpha():
        resultado += letra.upper()
        capitalizar = False
    else:
        resultado += letra
        if letra == " ":
            capitalizar = True

print(resultado)

# se podria hacer directamente con: str.title()

        