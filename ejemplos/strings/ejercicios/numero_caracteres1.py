cadena = input("Introduce una frase: ")
suma = 0

for caracter in cadena:
    if caracter != " ":
        suma = suma + 1

print(f"{cadena}, tiene {suma} carácteres (sin contar espacios en blanco.)")