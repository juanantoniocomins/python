frase = "Esta es una frase de prueba"
sin_vocales = []

for c in frase:
    if c not in "aeiouAEIOU":
        sin_vocales.append(c)

resultado = "".join(sin_vocales)
print(resultado)