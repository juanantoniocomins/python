"""
==================================================================================================
DECLARACION
==================================================================================================

__________________________________________________________________________________________________
def nombre_funcion(param1, param2=valor_por_defecto, *args, **kwargs):
    # Bloque de código que realiza la tarea
    # ...
    
    return valor  # Opcional, si no se usa, la función devuelve None
__________________________________________________________________________________________________

def: palabra reservada para definir una función.
nombre_funcion: el nombre que le das a la función (sin espacios, empieza con letra o guion bajo).
(param1, param2=valor_por_defecto, *args, **kwargs): parámetros que recibe la función.
param1, param2: parámetros normales.
param2=valor_por_defecto: parámetro con valor por defecto (opcional).
*args: recibe una cantidad variable de argumentos posicionales (como tuplas).
**kwargs: recibe una cantidad variable de argumentos nombrados (como diccionario).
return valor: devuelve un valor y termina la ejecución de la función (opcional).   

==================================================================================================
LLAMADA
==================================================================================================

__________________________________________________________________________________________________
nombre_funcion(argumento1, argumento2, argumento3, ...)
__________________________________________________________________________________________________

Forma de pasar argumentos	            Ejemplo de llamada
Posicional	                            f(10, 20)
Por nombre (keyword)	                f(b=20, a=10)
Con valores por defecto	                f(10) (si b tiene valor por defecto)
Variable cantidad con *args	            f(1, 2, 3, 4)
Variable cantidad con **kwargs	        f(nombre="Juan", edad=30)
Desempaquetar lista/tupla con *	        f(*[1, 2, 3])
Desempaquetar diccionario con **	     f(**{'a':1, 'b':2, 'c':3})
"""

def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años.")

saludar("Juanan", 50)