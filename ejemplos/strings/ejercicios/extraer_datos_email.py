correo = input("Introduce tu dirección de correo electronico: ")

arroba = correo.find("@")
usuario = correo[0:arroba]
dominio = correo[arroba+1:]

print(f"El usuario es: {usuario}")
print(f"El dominio es: {dominio}")
