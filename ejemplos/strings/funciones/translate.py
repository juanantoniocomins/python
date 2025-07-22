# reemplaza, elimina o mapea caracteres de un string, según una tabla de traducción que tú defines.

tabla = str.maketrans("abc", "123") # Se usa la función str.maketrans() para crear la tabla.

nuevo_string = "abracadabra".translate(tabla)
print(nuevo_string)
# 'a' → '1'
# 'b' → '2'
# 'c' → '3'

# Cambiar letras por otras

tabla = str.maketrans("aeiou", "12345")
texto = "Hola Juanan".translate(tabla)
print(texto)

# eliminar caracteres

tabla = str.maketrans("", "", "aeiou")
texto = "Hola Juanan".translate(tabla)
print(texto)