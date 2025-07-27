usuario = "Juan Antonio"
usuario_modificado = ""

for c in usuario:
    if c == 'a' or c == 'A':
        usuario_modificado += '1'
    elif c == 'e' or c == 'E':
        usuario_modificado += '2'
    elif c == 'i' or c == 'I':
        usuario_modificado += '3'
    elif c == 'o' or c == 'O':
        usuario_modificado += '4'
    elif c == 'u' or c == 'U':
        usuario_modificado += '5'
    else:
        usuario_modificado += c

print(usuario_modificado)