a = [1, 2, 3]
b = [1, 2, 3]
c = [3, 2, 1]

if (a == b):
    print(f"{a} = {b}")

if (a == c):
    print(f"{a} = {c}")
else:
    print(f"{a} != {c}")

# metodo comp, hay que definir primero la funcion

def comp(lista1, lista2):
    return lista1 == lista2

print(comp(a, b))  # True (mismo orden y elementos)
print(comp(a, c))  # False (mismos elementos, distinto orden)

