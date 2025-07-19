usu = "juan"
contra = "12345"
salir = "no"

while salir.lower() == "no":
    print("\n🔐 Autenticación de usuario")
    u = input("👤 Usuario: ")
    c = input("🔒 Contraseña: ")
    
    u = u.lower()

    if u == usu and c == contra:
        print(f"✅ ¡Bienvenido, {u.title()}! 🎉 Acceso concedido.")
    else:
        print(f"❌ Credenciales incorrectas: {u}:{c} 🚫 Acceso denegado.")

    salir = input("\n🔁 ¿Deseas salir? (si/no): ")

print("\n📴 Cerrando el programa... ¡Hasta la próxima! 👋")
