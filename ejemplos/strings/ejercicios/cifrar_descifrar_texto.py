texto_original = ""
texto_cifrado = ""
desplazamiento = 3  # Puedes cambiarlo si quieres

while True:
    print("\nMenú:")
    print("1 - Introducir texto")
    print("2 - Cifrar")
    print("3 - Descifrar")
    print("4 - Mostrar texto cifrado")
    print("0 - Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        texto_original = input("Introduce el texto: ")
        texto_cifrado = ""  # Reiniciar cifrado si el texto cambia
        print("Texto guardado.")

    elif opcion == "2":
        if texto_original == "":
            print("Primero debes introducir un texto.")
        else:
            texto_cifrado = ""
            for c in texto_original:
                if c.isalpha():
                    base = ord('A') if c.isupper() else ord('a')
                    nuevo = chr((ord(c) - base + desplazamiento) % 26 + base)
                    texto_cifrado += nuevo
                else:
                    texto_cifrado += c
            print("Texto cifrado correctamente.")

    elif opcion == "3":
        if texto_cifrado == "":
            print("Primero debes cifrar un texto.")
        else:
            texto_descifrado = ""
            for c in texto_cifrado:
                if c.isalpha():
                    base = ord('A') if c.isupper() else ord('a')
                    nuevo = chr((ord(c) - base - desplazamiento) % 26 + base)
                    texto_descifrado += nuevo
                else:
                    texto_descifrado += c
            print("Texto descifrado:", texto_descifrado)

    elif opcion == "4":
        if texto_cifrado == "":
            print("Todavía no hay texto cifrado.")
        else:
            print("Texto cifrado:", texto_cifrado)

    elif opcion == "0":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida.")
