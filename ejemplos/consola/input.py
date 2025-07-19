# Entrada de usuario (consola)
# input() siempre devuelve una cadena de texto (str). 
# Si necesitas un número, debes convertirlo.

entrada = input("Escribe algo: ")
print("Escribiste:", entrada)

# entrada de un entero: 

edad = int(input("Introduce tu edad: "))
print("El próximo año tendrás", edad + 1)


# TIPOS MÁS COMUNES A CONVERTIR DESDE input()
# 
# Tipo	    Conversión	    Descripción	            Ejemplo entrada	    Resultado final
# 
# int	    int()	        Número entero	        42	                42 (int)
# float	    float()	        Número con decimales	3.14	            3.14 (float)
# bool	    bool()	        Lógico verdadero/falso 	True	            True (bool)
# str	    str()	        Texto 	                hola	            "hola" (str)
# list	    eval()	        Lista	                [1, 2, 3]	        [1, 2, 3] (list)
# tuple	    eval()	        Tupla	                (4, 5)	            (4, 5) (tuple)
# dict	    eval()	        Diccionario	            {"a": 1}	        {'a': 1} (dict)