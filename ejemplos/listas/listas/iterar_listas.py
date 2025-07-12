frutas = ["manzana", "pera", "plátano", "naranja"]
precios = [1.2, 0.8, 1.5, 2.0]

# ----------------------------------------------------------------------- for

print("-----------------------for-----------------------")

for fruta in frutas: # muestra valores
    print(fruta)

print("-------------------------------------------------")

for fruta in reversed(frutas): # muestra valores a la inversa
    print(fruta)

print("-------------------------------------------------")

for indice, fruta in enumerate(frutas): # muestra indices y valores
    print(f"{indice}:{fruta}")

print("-------------------------------------------------")

for fruta, precio in zip(frutas, precios): # recorrer los valores de dos simultaneamente
    print(f"{fruta} = {precio} €")

print("-------------------------------------------------")

for fruta in frutas: # utilizando una condicion
    if fruta == "manzana":
        print(f"La {fruta} si que esta.")

# ----------------------------------------------------------------------- for + range

print("------------------for + range---------------------")

for indice in range(len(precios)): # muestra indices 
    print(indice)

print("-------------------------------------------------")

for precio in range(len(precios)): # muestra valores
    print(precios[precio])

print("-------------------------------------------------")

for fruta in range(len(frutas)): # modificar los valores: convertir a mayusculas
    frutas[fruta] = frutas[fruta].upper()

print(frutas)

print("-------------------------------------------------")

for fruta in range(3): # recorrer los valores e indices de 0 a 3 (no se incluye)
    print(f"{fruta} : {frutas[fruta]}")

print("-------------------------------------------------")

for fruta in range(1, 4): # recorrer valores del 1 al 4 (no se incluye)
    print(f"{frutas[fruta]}")

print("-------------------------------------------------")

for fruta in range(0, 3, 2): # utilizar un salto: cada 2, empezando por el primero (0)
    print(f"{frutas[fruta]}")

print("-------------------------------------------------")

for i in range(3, -1, -1): # inverso
    print(frutas[i])

# ----------------------------------------------------------------------- for + for (listas anidadas)

print("------------------for + range---------------------")
print("----------------listas anidadas-------------------")

cursos = [["Juan", "Pedro"], ["Ana", "Lucía"]]
for grupo in cursos:
    for alumno in grupo:
        print(alumno)

