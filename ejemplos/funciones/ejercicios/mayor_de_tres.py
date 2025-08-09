num1 = int(input("Introducde el primer número: "))
num2 = int(input("Introducde el segundo número: "))
num3 = int(input("Introducde el tercer número: "))

def mayor(n1, n2, n3):
    
    if n1 > n2:
        mayor = n1
    else: 
        mayor = n2
    if n3 > mayor:
        mayor = n3
        
    print(f"El mayor de {n1}, {n2} y {n3} = {mayor}")

mayor(num1, num2, num3)