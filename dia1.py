#DIA 1
#Inversión de una Cadena: Escribe un programa que invierta una cadena de caracteres dada por el usuario.

def invertir_cadena_recursivamente(cadena):
    # Caso base: si la cadena está vacía o tiene un solo carácter,
    # simplemente la devolvemos.
    if len(cadena) <= 1:
        return cadena
    # Caso recursivo: invertimos la subcadena que no incluye el último
    # carácter y luego añadimos el último carácter al final.
    return cadena[-1] + invertir_cadena_recursivamente(cadena[:-1])

# Pedimos al usuario que ingrese la cadena que quiere invertir.
cadena_original = input("Ingresa una cadena para invertirla: ")

# Llamamos a la función invertir_cadena_recursivamente() con la cadena ingresada
# por el usuario y mostramos el resultado invertido.
cadena_invertida = invertir_cadena_recursivamente(cadena_original)
print("Cadena invertida:", cadena_invertida)
