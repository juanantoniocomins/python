# Los bucles for y while pueden llevar una cláusula else, y su comportamiento es el siguiente:
# El bloque else se ejecuta solo si el bucle no se interrumpe con un break.

# El uso de else en bucles es útil cuando buscas algo, como en una búsqueda lineal

# ---------------------------------------- for + else 

for i in range(5):
    print(i)
else:
    print("El bucle 'for' terminó sin usar break.") # Aquí el else se ejecuta porque el bucle no se interrumpe con break.

# ---------------------------------------- for + break + else

for i in range(5):
    if i == 3:
        print("Se encontró un 3. Se interrumpe.")
        break # En este caso, el else NO se ejecuta porque el bucle se rompe con break.
    print(i)
else:
    print("No se encontró un 3.")

# ---------------------------------------- while + else

x = 0
while x < 3:
    print(x)
    x += 1
else: # El else se ejecuta porque el bucle acaba de forma natural.
    print("El bucle 'while' terminó sin break.")

# ---------------------------------------- while + break + else

x = 0
while x < 5:
    if x == 2:
        print("Interrumpido con break en x = 2")
        break
    print(x)
    x += 1
else: # Aquí no se ejecuta el else porque el bucle fue interrumpido.
    print("El bucle 'while' terminó sin usar break.")