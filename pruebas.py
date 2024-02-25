import random
import string

# Lista de caracteres
caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"

# Longitud de la contraseña
longitud = 16

# Generación de la contraseña
contrasena = "".join(random.choice(caracteres) for i in range(longitud))

# Impresión de la contraseña
print(f"Tu contraseña segura es: {contrasena}")
