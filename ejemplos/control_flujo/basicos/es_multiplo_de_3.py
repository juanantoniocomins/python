num = int(input("Introduce un número: "))
multiplo = 3

print(f"Conozcamos si el {num} es multiplo de {multiplo}: ")

if num % multiplo == 0:
    print(f"{num} es multiplo de {multiplo}")
else:
    print(f"{num} NO es multiplo de {multiplo}")