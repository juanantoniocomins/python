vocal = input ("Introduce una vocal: a, e, i, o, u: ")
vocal = vocal.lower() # pasamos a minusculas

if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
    print(f"Has introducido una vocal: {vocal}")
else:
    print(f"{vocal}: no es una vocal.")


