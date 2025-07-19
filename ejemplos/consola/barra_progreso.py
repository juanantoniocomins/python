ancho = 20

for i in range(ancho +1):
    porcentaje = int(i / ancho * 100)
    barra = "#" * i + "-" * (ancho-i)
    print(f"{barra}{porcentaje}%")