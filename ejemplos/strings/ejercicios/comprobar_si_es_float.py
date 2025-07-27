valor = input("Introduce un valor: ")

try:
    float(valor)
    print(f"{valor} es un float válido.")
except ValueError:
    print(f"{valor} NO es un float válido.")