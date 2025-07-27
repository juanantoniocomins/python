cadena = input("Introduce una frase: ")

if cadena.isalnum():
    print(f"{cadena}, contiene letras y/o números (sin símbolos).")
else:
    print(f"{cadena}, contiene simbolos.")    

""" 


Entrará en el **else** si la cadena contiene:

Espacios

"hola mundo"
"123 hola"

Símbolos o signos

"hola!"
"123$"
"¿Qué tal?"
"email@example.com"

Puntuación

"Hola,"
"Sí."

Caracteres vacíos o especiales

"" (cadena vacía)
"\n" (salto de línea)
" " (espacio) 



"""