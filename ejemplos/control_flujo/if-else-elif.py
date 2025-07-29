# if condición1:
    # bloque si condición1 es verdadera
# elif condición2:
    # bloque si condición2 es verdadera
# elif condición3:
    # puedes añadir más elif si lo necesitas
# ...
# ...
# ...
# else:
    # bloque si ninguna condición anterior se cumple

nota = float(input("Introduce tu nota (0-10): "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
