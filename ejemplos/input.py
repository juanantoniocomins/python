"""

- La función input() es capaz de leer datos que fueron introducidos por el usuario y pasar esos datos al programa en ejecución.
- Cuando la función input() es llamada o invocada, el flujo del programa se detiene, el símbolo del cursor se mantiene parpadeando (le está indicando al usuario que tome acción ya que la consola está en modo de entrada) hasta que el usuario haya ingresado un dato y/o haya presionado la tecla Enter.
- El programa solicita al usuario que inserte algún dato desde la consola (seguramente utilizando el teclado, aunque también es posible introducir datos utilizando la voz o alguna imagen).
- La función input() es invocada sin argumentos (es la manera mas sencilla de utilizar la función); la función pondrá la consola en modo de entrada; aparecerá un cursor que parpadea, y podrás introducir datos con el teclado, al terminar presiona la tecla Enter; todos los datos introducidos serán enviados al programa a través del resultado de la función.
  Nota: el resultado debe ser asignado a una variable; esto es crucial, si no se hace los datos introducidos se perderán. 
        el resultado de la función input() es una cadena.

"""
print("Dime algo...")
anything = input()
print("Mmm...", anything, "...¿en serio?")
print("=========================================================================")
anything = float(input("Inserta un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)