correo = input("Introduce tu dirección de correo electrónico: ")
errores = False

if correo.count("@") != 1:
    print("El correo debe contener una única '@'")
    errores = True
elif " " in correo:
    print("El correo no debe contener espacios")
    errores = True
else:
    arroba = correo.find("@")
    usuario = correo[:arroba]
    dominio = correo[arroba+1:]

    if usuario == "" or dominio == "":
        print("El usuario o el dominio está vacío")
        errores = True
    elif "." not in dominio:
        print("Dominio inválido: falta el punto '.'")
        errores = True
    else:
        print(f"Usuario: {usuario}")
        print(f"Dominio: {dominio}")

if errores:
    print("Correo inválido")
