"""
POide tres numeros al usuario y los suma
"""
print("################################################################################################")
print ("------------Programa:---------------------")
print ("------------Sumar tres numeros------------")
print ("------------------------------------------")
print ("Está permitido el introducir decimales.\nAcuerdate que la parte decimal es con un punto")
print("################################################################################################\n")

n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
n3 = float(input("Introduce el tercer número: "))

suma = n1 + n2 + n3

print (str(n1) + " + " + str(n2) + " + " + str(n3) + " = " + str(suma))