import subprocess

try:
    subprocess.run(["notepad.exe"], check=True)
except FileNotFoundError:
    print("No se encuentra 'notepad.exe' en el PATH")
except subprocess.CalledProcessError as e:
    print(f"El programa se ejecutó pero devolvió error: {e.returncode}")