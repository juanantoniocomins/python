# print() – Imprimir en consola
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# *objects: uno o varios valores a imprimir.
# sep=' ' → separador entre los valores (por defecto un espacio).
# end='\n' → qué poner al final (por defecto un salto de línea).
# file=sys.stdout → salida (puede ser un archivo en vez de la consola).
# flush=False → fuerza la impresión inmediata si es True.

print("Hola, mundo")                    # Texto simple
print("Nombre:", "Juanan")              # Múltiples valores
print("Suma:", 3 + 5)                   # Expresión
print("Hola", "Mundo", sep="-")         # Hola-Mundo
print("Hola\nMundo")                    # Salto de línea
print("A\tB\tC")                        # Tabulación
print("Texto", end=" ")                 # Sin salto final