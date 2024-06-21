import random
import string

def generar_contraseña():
    longitud = random.randint(8, 16)  # Longitud aleatoria entre 8 y 16 caracteres
    caracteres = string.ascii_letters + string.digits  # Letras y números
    
    # Generar la contraseña segura
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

# Generar y mostrar la contraseña generada
contraseña_generada = generar_contraseña()
print("Contraseña generada:", contraseña_generada)
