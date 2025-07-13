# Codifica el string

# EJEMPLOS:
# 'utf-8'	Codificación estándar moderna, compatible con casi todo.
# utf-16'	Usa 2 bytes por carácter; puede incluir BOM.
# 'utf-32'	Usa 4 bytes por carácter; más pesado, pero directo.
# 'ascii'	Solo admite caracteres estándar (0-127).
# 'latin-1' o 'iso-8859-1'	Muy usada en Europa occidental, permite hasta 256 caracteres.
# 'cp1252'	Similar a latin-1, usado en Windows.
# 'cp437'	Código original de MS-DOS.
# 'euc_jp'	Japonés.
# 'koi8_r'	Ruso.

poema = "Con tres cañoes por banda..."

print(poema.encode('utf-8'))
print(poema.encode('cp437'))