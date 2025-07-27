cadena = input("Introduce una frase: ")
suma_caracteres = 0
suma_espacios = 0

for caracter in cadena:
    if caracter != " ":
        suma_caracteres = suma_caracteres + 1
    else:
        suma_espacios = suma_espacios + 1

print(f"{cadena}, tiene {suma_caracteres} carácteres y {suma_espacios} espacios en blanco.)")