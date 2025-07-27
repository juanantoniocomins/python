cadena = input("Introduce una frase: ")

if cadena.isalpha():
    print("Solo contiene letras (cadena).")
else:
    print("No solo contiene letras.")


# "hola123" → contiene números → else
# "hola mundo" → contiene espacio → else
# "python!" → contiene símbolo → else
# "123" → solo números → else
# " " → solo espacio → else
# "" → cadena vacía → else