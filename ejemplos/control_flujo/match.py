# match expresión:
#     case patrón1:
#         # Código si coincide patrón1
#     case patrón2:
#         # Código si coincide patrón2
#     case patrónN:
#         # Código si coincide patrónN
#     case _:
#         # Código si no coincide ningún patrón (caso por defecto)

color = input("Introduce un color (rojo, verde, azul): ")

match color:
    case "rojo":
        print("Color rojo seleccionado")
    case "verde":
        print("Color verde seleccionado")
    case "azul":
        print("Color azul seleccionado")
    case _:
        print("Color no reconocido")

# se puede usar condiciones: 

nota = int(input("Introduce tu nota: "))

match nota:
    case _ if 0 <= nota < 5:
        print("Estas suspendido.")
    case _ if 5 <= nota < 7:
        print("Estas aprobado.")   
    case _ if 7<= nota < 9:     
        print("Estas aprobado con notable.")   
    case _ if 9 <= nota <= 10:
        print("Estas aprobado con sobresaliente")
    case _:
        print("Nota inválida")        