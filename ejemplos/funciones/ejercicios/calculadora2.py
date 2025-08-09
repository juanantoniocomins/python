salir = "si"

while salir == "si":

    num1 = int(input("Introducde el primer número: "))
    num2 = int(input("Introducde el segundo número: "))
    operacion = int(input("Indica si quieres sumar (1), restar (2), multiplicar (3) o dividir (4): "))

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
                    print("Error: división por cero.")
                    res = None
                else: 
                    res = n1 / n2
                    print(f"{n1} / {n2} = {res}")
            case _:
                print("Operación invalida.")
                res = None
        return res

    operando(num1, num2, operacion)

    salir = input("¿Quieres volver a intentarlo (si/no)?: ").lower()