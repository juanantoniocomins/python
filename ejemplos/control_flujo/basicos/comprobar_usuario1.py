usu = "juan"
contra = "12345"

u = input("👤 Introduce el nombre del usuario: ")
c = input("🔒 Introduce la contraseña: ")

u = u.lower()

if u == usu and c == contra:
    print(f"✅ Bienvenido, {u.title()} 🎉 ¡Acceso concedido!")
else:
    print(f"❌ Credenciales incorrectas: {u}:{c} 🚫 Acceso denegado")
