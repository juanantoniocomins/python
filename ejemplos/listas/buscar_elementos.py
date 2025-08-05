numeros = [4, 10, 15, 3, 20]
palabras = ["sol", "luna", "estrella", "mar"]
reales = [-5, 3, -1, 0, 7, -8]

# metodo filter

# -------------------------------------------------------------------------------

def pares (n): # devuelve los pares
    return n % 2 == 0

res1 = filter(pares, numeros)
print(list(res1))

# -------------------------------------------------------------------------------

def palabras_cortas(n): # palabras con menos de tres letras
    return len(n) < 4

res2 = filter(palabras_cortas, palabras)
print(list(res2))

# -------------------------------------------------------------------------------

def negativos (n): # numeros negativos
    return n < 0

res3 = filter(negativos, reales)
print(list(res3))

# -------------------------------------------------------------------------------

def termina_en_vocal(palabra): # palabras que terminen en vocal
    return palabra[-1] in "aeiou"

resultado = filter(termina_en_vocal, palabras)
print(list(resultado))

# -------------------------------------------------------------------------------

def no_esta_vacia(cadena): # cadenas no vacias
    return cadena != ""

resultado1 = filter(no_esta_vacia, palabras)
print(list(resultado1))