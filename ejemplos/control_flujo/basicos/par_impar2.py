numero = int(input("Introduce un número: "))

if numero == 0:
    print("Has introducido un cero.")
else:
    if numero % 2 == 0:
        print("Es par.")
    else:
        print("Es impar.")