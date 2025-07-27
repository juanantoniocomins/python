# ------------------------------- cada caracter en una posicion 

cadena1 = "hola"
lista1 = list(cadena1)
print(lista1)  # ['h', 'o', 'l', 'a']

# ------------------------------- cada palabra en una posicion 

cadena2 = "hola mundo"
palabras = cadena2.split()

print(palabras)

for i in range(len(palabras)):
    print(f"Palabra {i}: {palabras[i]}")

# modificar varias letras

palabra = "caballo"
lista = list(palabra)

lista[0] = 'g'
lista[2] = 'v'

nueva = ''.join(lista)
print(nueva)

# modificar varias palabras de una frase: 

frase11 = "hola mundo bonito"
palabras11 = frase11.split()

palabras11[0] = "adiós"
palabras11[2] = "feo"

nueva_frase = ' '.join(palabras11)
print(nueva_frase)