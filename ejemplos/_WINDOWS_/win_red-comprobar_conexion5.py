import subprocess

def ping_host(host="8.8.8.8", intentos=4):
    try:
        # Ejecutamos un ping "normal" (4 intentos)
        resultado = subprocess.check_output(
            ["ping", host, "-n", str(intentos)], text=True
        )
        # Si llega aquí, es porque el ping fue satisfactorio
        comentario = (
            f"✅ Prueba de conectividad correcta hacia {host}\n\n"
            f"Detalles de la prueba:\n{resultado}"
        )
    except subprocess.CalledProcessError as e:
        # Si falla, capturamos la salida del error
        comentario = (
            f"❌ Error de conectividad hacia {host}\n\n"
            f"Detalles de la prueba:\n{e.output if e.output else 'No se obtuvo salida'}"
        )
    return comentario


# Ejemplo de uso
texto_ticket = ping_host("8.8.8.8", intentos=3)
print(texto_ticket)
