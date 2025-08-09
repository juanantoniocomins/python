num1 = int(input("Introducde el primer número: "))
num2 = int(input("Introducde el segundo número: "))

def mayor(n1, n2):
    if n1 > n2:
        print(f"El mayor de {n1} y {n2} es {n1}")
    elif n2 > n1:
        print(f"El mayor de {n2} y {n1} es {n2}") 
    else:
        print(f"{n1} = {n2}")     

mayor(num1, num2)