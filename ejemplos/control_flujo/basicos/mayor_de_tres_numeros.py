num1 = int(input("Introduce el primer número: "))
num2 = int(input("Intropduce el segundo número: "))
num3 = int(input("Intropduce el tercer número: "))

if num1 > num2:
    mayor = num1
else:
    mayor = num2

if num3 > mayor:
    mayor = num3

print (f"El número mayor de los tres introducidos es: {mayor}")