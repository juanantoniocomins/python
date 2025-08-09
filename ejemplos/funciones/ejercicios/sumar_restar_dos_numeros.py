num1 = int(input("Introducde el primer número: "))
num2 = int(input("Introducde el segundo número: "))
operacion = int(input("Indica si quieres sumar (1) o restar (2): "))

def operando(n1, n2, op):
    if op == 1:
        suma = n1 + n2
        return suma
    elif op == 2:
        resta = n1 - n2
        return resta
    else:
        return "Opcion incorrecta."

res = operando(num1, num2, operacion)

if operacion == 1:
    print(f"El resultado es: {num1} + {num2} = {res}") 
if operacion == 2:
    print(f"El resultado es: {num1} - {num2} = {res}") 


