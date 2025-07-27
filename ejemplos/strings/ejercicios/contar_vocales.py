cadena = input("Introduce una frase: ")
contar_a = 0
contar_e = 0
contar_i = 0
contar_o = 0
contar_u = 0

for x in cadena:
    if x == "a" or x == "A":
        contar_a += 1
    if x == "e" or x == "E":
        contar_e += 1
    if x == "i" or x == "I":
        contar_i += 1
    if x == "o" or x == "O":
        contar_o += 1
    if x == "u" or x == "U":
        contar_u += 1          

print("El total de vocales introducidas es:")       
print("a = " + str(contar_a))    
print("e = " + str(contar_e))    
print("i = " + str(contar_i))    
print("o = " + str(contar_o))  
print("u = " + str(contar_u))    
          