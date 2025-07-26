salir = "si"

while salir == "si":
    valor = input("Introduce algo: ")

    try:
        valor_int = int(valor)
        print(f"'{valor}' es de tipo: entero (int)")
    except ValueError:
        try:
            valor_float = float(valor)
            print(f"'{valor}' es de tipo: decimal (float)")
        except ValueError:
            print(f"'{valor}' es de tipo: cadena (str)")

    seguir = input("¿Quieres seguir comprobando tipos? (si/no): ")
    salir = seguir.lower()