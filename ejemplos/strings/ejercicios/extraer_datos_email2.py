correo = input("Introduce tu dirección de correo electronico: ")
paso = False


for x in correo:
    if x == "@":
        paso = True

if paso == True:
    arroba = correo.find("@")
    usuario = correo[0:arroba]
    dominio = correo[arroba+1:]

    print(f"El usuario es: {usuario}")
    print(f"El dominio es: {dominio}")
else:
    print("No has introducido @")