cadena = input("Introduce algo: ")

nueva_cadena = ""

for letra in cadena:
    if letra.isalpha():
        nueva_cadena += letra

print(nueva_cadena) 