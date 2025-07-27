cadena = input("Introduce una frase: ")

if cadena.isdigit():
    print(f"{cadena}, solo contiene numeros.")
else:
    print(f"{cadena}, NO solo contiene numeros.")    

""" 
Pasará por el **else** en todos estos casos:

Si contiene letras:

"abc"
"123abc"
"abc123"

Si contiene espacios:

"123 456"
" 123 "

Si contiene signos:

"-123"
"+456"

Si contiene decimales (puntos o comas):

"12.3"
"3,14"

Si está vacía:

""

Si contiene símbolos:

"123!"
"#45" 
"""