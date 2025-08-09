num1 = int(input("Introducde el primer número: "))
num2 = int(input("Introducde el segundo número: "))
operacion = int(input("Indica si quieres sumar (1), restar (2), multiplicar (3) o dividir (4): "))

def operando(n1, n2, op):
    match op:
        case 1:
            res = n1 + n2
        case 2:
            res = n1 - n2
        case 3:
            res = n1 * n2
        case 4:
            res = n1 / n2
        case _:
            print("Operación invalida.")
            res = None
    return res

total = operando(num1, num2, operacion)

if operacion == 1:
    print(f"{num1} + {num2} = {total}")
if operacion == 2:
    print(f"{num1} - {num2} = {total}")
if operacion == 3:
    print(f"{num1} * {num2} = {total}")
if operacion == 4:
    print(f"{num1} / {num2} = {total}")