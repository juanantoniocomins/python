def operando(n1, n2, op):
    match op:
        case 1:
            res = n1 + n2
            print(f"{n1} + {n2} = {res}")
        case 2:
            res = n1 - n2
            print(f"{n1} - {n2} = {res}")
        case 3:
            res = n1 * n2
            print(f"{n1} * {n2} = {res}")
        case 4:
            if n2 == 0:
                print("❌ Error: división por cero.")
                res = None
            else: 
                res = n1 / n2
                print(f"{n1} / {n2} = {res}")
        case _:
            print("❌ Operación invalida.")
            res = None
        
    return res

def inicio():

    salir = "si"
    while salir == "si":
        try: 
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
            operacion = int(input("Indica si quieres sumar (1), restar (2), multiplicar (3) o dividir (4): "))
        except ValueError:
            print("❌ Entrada no válida. Intenta de nuevo con números.")
            continue
        
        operando(num1, num2, operacion)

        salir = input("¿Quieres volver a intentarlo (si/no)?: ").strip().lower()
        while salir not in ("si", "no"):
            salir = input("Por favor escribe 'si' o 'no': ").strip().lower()

inicio()

