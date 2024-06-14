#Challenge dia 4
#Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.
def ordenar_lista(lista):
    return sorted(lista)

def main():
    numeros = input("Ingrese los números separados por espacios: ")
    lista_numeros = [int(x) for x in numeros.split()]
    lista_ordenada = ordenar_lista(lista_numeros)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()
