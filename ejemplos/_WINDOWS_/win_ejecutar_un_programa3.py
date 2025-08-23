import os

rc = os.system("notepad.exe")  # corregido: sin la 'w'
if rc != 0:
    print("No se encuentra el programa o falló al ejecutarse")