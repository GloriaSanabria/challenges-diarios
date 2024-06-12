#Tabla de Multiplicar:
#Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Pedir al usuario el número
try: #utilizado para manejar excepciones

    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

except ValueError: # se produce cuando el usuario ingresa algo que sea entero
    print("Por favor, ingrese un número válido.")
