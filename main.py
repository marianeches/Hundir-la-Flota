import numpy as np
import random

    
def crear_tablero_jugador(tamaño=(10,10)):
    return np.full(tamaño, " ")

def crear_tablero_maquina(tamaño=(10,10)):
    return np.full(tamaño, " ")

def crear_barco_random(eslora, orientacion):
    orientaciones = ["norte", "sur", "este", "oeste"]

    if orientacion in orientaciones:
        ("la orientacion es norte, sur, este u oeste")

    barco_random = []
    fila_random = random.randint(0,9)
    columna_random = random.randint(0,9)
    barco_random.append((fila_random, columna_random))   
   
    while len(barco_random) < eslora:
        if orientacion == 'norte':
            fila_random = random.randint(columna_random, fila_random - 1)
        elif orientacion == 'sur':
            fila_random = random.randint(columna_random, fila_random + 1)
        elif orientacion == 'este':
            columna_random = random.randint(fila_random, columna_random + 1)
        elif orientacion == 'oeste':
            columna_random = random.randint(fila_random, columna_random - 1)

        barco_random.append((fila_random, columna_random))
    
    return barco_random

def colocar_barcos_aleatorios(tablero, dimension):
    fila = random.randint(0, 9)
    columna = random.randint(0, 9)
    orientacion = random.choice(['h', 'v'])

    if orientacion == 'h' and columna + dimension <= 10:
        for i in range(dimension):
                tablero[fila][columna + i] = dimension
        
    elif orientacion == 'v' and fila + dimension <= 10:
        for i in range(dimension):
            tablero[fila + i][columna] = dimension


def disparar(tablero, casilla):
    if tablero[casilla] == " ":
        print("Agua")
        tablero[casilla] = "-"
    else:
        print("Tocado")
        tablero[casilla] = "X"
    return tablero

def main():

    print("¡Bienvenido al juego Hundir la flota!")
    print("Instrucciones:")
    print(" - Elige coordenadas para disparar a los barcos del oponente.")
    print(" - Gana el jugador que hunde todos los barcos del oponente.")
   
    tablero_jugador = crear_tablero_jugador()
    tablero_maquina = crear_tablero_maquina()

    barcos_jugador = crear_barco_random()
    barcos_maquina = crear_barco_random()

    colocar_barcos_aleatorios(barcos_jugador, tablero_jugador)
    colocar_barcos_aleatorios(barcos_maquina,tablero_maquina)

    

    while True:
        print("\nTu tablero:")
        print(tablero_jugador)

        try:
            x = int(input("Coordenada X para disparar"))
            y = int(input("Coordenada Y para disparar"))
        except: #numeros que no sean validos
            print("inserta números válidos.")
            continue

        if not (0 <= x < 10) or not (0 <= y < 10):
            print("Coordenadas no validas. Inténtalo de nuevo.")
            continue

        for turno in range(5):
            print(f"\nTurno {turno} - Tu tablero:")
            crear_tablero_jugador()

        if disparar(x, y):
            print(tablero_maquina, "¡Tocado! Contunua jugando.")
        else:
            print("\nTurno de la máquina:")
            for _ in range(5):
                x_maquina = random.randint(0, 9)
                y_maquina = random.randint(0, 9)

                print(f"Disparo de la máquina en ({x_maquina}, {y_maquina}):")
                
                if disparar(tablero_jugador, x_maquina, y_maquina):
                    print("¡Tocado! Espera.")
                    break
                else:
                    print("¡Agua! Tu turno.")
                    break

main()
