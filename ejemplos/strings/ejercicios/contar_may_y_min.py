frase = "Universidad Nacional de Educación a Distancia"
contador_may = 0
contador_min = 0

for caracter in frase:
    if caracter.isupper():
        contador_may += 1
    if caracter.islower():
        contador_min += 1       

print("Total mayusculas = " + str(contador_may))
print("Total mayusculas = " + str(contador_min))