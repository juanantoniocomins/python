print("")
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
print("Bienvenido al Conversor de Unidades a Metros")
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
print("                                           💠")
print("🔹 Unidades disponibles:                   💠")
print("                                           💠")
print(" 1 - 🟦 Milímetro (mm)  → 0.001 m          💠")
print(" 2 - 🟨 Centímetro (cm) → 0.01 m           💠")
print(" 3 - 🟩 Decímetro (dm)  → 0.1 m            💠")
print(" 4 - 🟪 Decámetro (dam) → 10 m             💠")
print(" 5 - 🟫 Hectómetro (hm) → 100 m            💠")
print(" 6 - ⬛ Kilómetro (km)  → 1000 m           💠")
print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
print("")
entrada = input("📌 Selecciona una unidad para convertir a metros: ")

if entrada.isdigit():
    opcion = int(entrada)
    if opcion >= 1 and opcion <= 6:
        match opcion:
            case 1:
                cantidad = input("🔵 Introduce la cantidad en milimetros: ")
                if cantidad.replace(".", "", 1).isdigit():
                    mm = float(cantidad)
                    res = mm * 0.001
                    print(f"{mm} mm = {res:.3f} metros.")
                else:
                    print("❌ Cantidad inválida. Introduce un número.")   
            case 2:
                cantidad = input("🟡 Introduce la cantidad en centimetros: ")
                if cantidad.replace(".", "", 1).isdigit():
                    cm = float(cantidad)
                    res = cm * 0.01
                    print(f"{cm} cm = {res:.3f} metros.")
                else:
                    print("❌ Cantidad inválida. Introduce un número.")   
            case 3:
                cantidad = input("🟢 Introduce la cantidad en decimetros: ")
                if cantidad.replace(".", "", 1).isdigit():
                    dm = float(cantidad)
                    res = dm * 0.1
                    print(f"{dm} dm = {res:.3f} metros.")
                else:
                    print("❌ Cantidad inválida. Introduce un número.")  
            case 4:
                cantidad = input("🟣 Introduce la cantidad en decametros: ")
                if cantidad.replace(".", "", 1).isdigit():
                    dam = float(cantidad)
                    res = dam * 10
                    print(f"{dam} dam = {res:.3f} metros.")
                else:
                    print("❌ Cantidad inválida. Introduce un número.")          
            case 5:
                cantidad = input("🟤 Introduce la cantidad en hectometros: ")
                if cantidad.replace(".", "", 1).isdigit():
                    hm = float(cantidad)
                    res = hm * 100
                    print(f"{hm} hm = {res:.3f} metros.")
                else:
                    print("❌ Cantidad inválida. Introduce un número.")     
            case 6:
                cantidad = input("⚫ Introduce la cantidad en kilometros: ")
                if cantidad.replace(".", "", 1).isdigit():
                    km = float(cantidad)
                    res = km * 1000
                    print(f"{km} km = {res:.3f} metros.")
                else:
                    print("❌ Cantidad inválida. Introduce un número.")                                                                                                 
            case _:
                print("🚫 Error 🚫 Opción no váĺida")
        print("🎉 Conversión finalizada. ¡Gracias por usar el conversor métrico!")
    else:
        print("📛 Selección fuera de rango. Debes elegir un número del 1 al 6.")
else:
    print("❌ Entrada inválida. Solo se aceptan números enteros.")



