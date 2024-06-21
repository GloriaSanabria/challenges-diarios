import random

import random

def nombre_jugada(jugada):
    if jugada == 1:
        return "piedra"
    elif jugada == 2:
        return "papel"
    elif jugada == 3:
        return "tijera"

print("      JUEGO DE PIEDRA, PAPEL O TIJERAS      ")
jugada_jugador = int(input("Elige tu jugada:\n 1. piedra\n 2. papel\n 3. tijera\n"))

jugada_maquina = random.randint(1, 3)

nombre_jugada_jugador = nombre_jugada(jugada_jugador)
nombre_jugada_maquina = nombre_jugada(jugada_maquina)

print(f"El jugador eligió {nombre_jugada_jugador} y la máquina eligió {nombre_jugada_maquina}")

if jugada_jugador == jugada_maquina:
    print("¡Es un empate!")
elif (jugada_jugador == 1 and jugada_maquina == 3) or \
     (jugada_jugador == 2 and jugada_maquina == 1) or \
     (jugada_jugador == 3 and jugada_maquina == 2):
    print("¡Ganaste!")
else:
    print("¡La máquina gana!")
