# ========================================================
# Ejemplos de break, continue y pass en bucles en Python
# ========================================================

# break: Sale inmediatamente del bucle actual, sin ejecutar más iteraciones.
# continue: Salta a la siguiente iteración del bucle, omitiendo el resto del código en la actual.
# pass: No hace nada; se usa como marcador de posición donde se requiere sintácticamente un bloque de código.


# -----------------------------------
# 1. Uso de 'break' en un bucle for
# -----------------------------------

print("Ejemplo 1: break en bucle for")
for num in range(10):
    if num == 5:
        print("¡Se encontró el 5, se detiene el bucle!")
        break
    print(num)

# -----------------------------------
# 2. Uso de 'break' en un bucle while
# -----------------------------------

print("\nEjemplo 2: break en bucle while")
x = 0
while x < 10:
    if x == 5:
        print("¡Se encontró el 5, se detiene el bucle!")
        break
    print(x)
    x += 1

# -----------------------------------
# 3. Uso de 'continue' en un bucle for
# -----------------------------------

print("\nEjemplo 3: continue en bucle for")
for num in range(5):
    if num == 2:
        print("Salta el 2")
        continue
    print(num)

# -----------------------------------
# 4. Uso de 'continue' en un bucle while
# -----------------------------------

print("\nEjemplo 4: continue en bucle while")
x = 0
while x < 5:
    x += 1
    if x == 3:
        print("Salta el 3")
        continue
    print(x)

# -----------------------------------
# 5. Uso de 'pass' en un bucle for
# -----------------------------------

print("\nEjemplo 5: pass en bucle for")
for letra in "hola":
    if letra == "o":
        pass  # Aquí no se hace nada con la 'o'
    print(letra)

# -----------------------------------
# 6. Uso de 'pass' en un bucle while
# -----------------------------------

print("\nEjemplo 6: pass en bucle while")
x = 0
while x < 3:
    if x == 1:
        pass  # Se deja sin implementar acción
    print(x)
    x += 1