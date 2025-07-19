from colorama import init, Fore, Style

init()  # <-- inicialización recomendada

print(Fore.GREEN + "Hola Mundo!!!")
print("Sigue en verde.")
print(Fore.RED + "Adios Mundo!!!" + Style.RESET_ALL)
print("Volvemos a lo normal.")