cadena = "Juan Antonio"
nueva_cadena = ""

for x in cadena:
    if x not in "aeiouAEIOU":
        nueva_cadena += x

print(nueva_cadena)