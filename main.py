import numpy as np
import random

    
def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, " ")


def crear_barco_random(eslora, orientacion):
    orientaciones = ["norte", "sur", "este", "oeste"]

    if orientacion in orientaciones:
        barco_random = []
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        barco_random.append((fila_random, columna_random))   
    
        while len(barco_random) < eslora:
            if orientacion == 'norte' and 0 <= fila_random - 1<= 9 :
                fila_random = fila_random - 1
            elif orientacion == 'sur'and 0 <= fila_random + 1<= 9:
                fila_random = fila_random + 1
            elif orientacion == 'este'and 0 <= columna_random + 1<= 9:
                columna_random = columna_random + 1
            elif orientacion == 'oeste'and 0 <= columna_random - 1<= 9:
                columna_random = columna_random - 1
            else: 
                return ""
    

            barco_random.append((fila_random, columna_random))
    
        return barco_random
    
    else: 
        print("Introduce orientacion correcta")

def colocar_barcos_aleatorios(tablero, barco):
    for coordenada in barco:
        if tablero[coordenada[0]][coordenada[1]] == " ":
            tablero[coordenada[0]][coordenada[1]] = "O"
        else:
            return ""
    

def disparar(tablero, casilla):
    if tablero[casilla[0]][casilla[1]] == " ":
        print("Agua")
        acierto = False
        tablero[casilla[0]][casilla[1]] = "-"
    elif tablero[casilla[0]][casilla[1]] == "O":
        print("Tocado")
        acierto = True
        tablero[casilla[0]][casilla[1]] = "X"
    else:
        print("Disparo hecho")
        return ""
    return tablero, acierto

def poner_barcos_jugadores(eslora, n_barcos, tablero_jugador, tablero_maquina):
    lista_orientaciones = ["norte","sur","este","oeste"]
    n_barcos_colocados = 0
    while n_barcos_colocados < n_barcos:
                nuevo_barco = crear_barco_random(eslora, lista_orientaciones[random.randint(0,3)])
                if nuevo_barco:
                    nuevo_tablero = colocar_barcos_aleatorios(tablero_jugador, nuevo_barco)
                    if nuevo_tablero:
                        tablero_jugador = nuevo_tablero
                        n_barcos_colocados = n_barcos_colocados + 1
            
    n_barcos_colocados = 0
            
    while n_barcos_colocados < n_barcos:
        nuevo_barco = crear_barco_random(eslora, lista_orientaciones[random.randint(0,3)])
        if nuevo_barco:
            nuevo_tablero = colocar_barcos_aleatorios(tablero_maquina, nuevo_barco)
            if nuevo_tablero:
                tablero_maquina = nuevo_tablero
                n_barcos_colocados = n_barcos_colocados + 1
    
    return tablero_jugador, tablero_maquina


def crear_partida():
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()
    tablero_jugador, tablero_maquina = poner_barcos_jugadores(1, 4, tablero_jugador, tablero_maquina)
    tablero_jugador, tablero_maquina = poner_barcos_jugadores(2, 3, tablero_jugador, tablero_maquina)
    tablero_jugador, tablero_maquina = poner_barcos_jugadores(3, 2, tablero_jugador, tablero_maquina)
    tablero_jugador, tablero_maquina = poner_barcos_jugadores(4, 1, tablero_jugador, tablero_maquina)   

    return tablero_jugador, tablero_maquina

    

def main():

    print("¡Bienvenido al juego Hundir la flota!")
    print("Instrucciones:")
    print(" - Elige coordenadas para disparar a los barcos del oponente.")
    print(" - Gana el jugador que hunde todos los barcos del oponente.")   

    tablero_jugador, tablero_maquina = crear_partida()
    turno = 1
    acierto_jugador = 0
    acierto_maquina = 0 

    while True:
        print("\nTu tablero:")
        print(tablero_jugador)

        try:
            x = int(input("Coordenada X para disparar"))
            y = int(input("Coordenada Y para disparar"))
        except: #numeros que no sean validos
            print("inserta números")
            continue

        if not (0 <= x < 10) or not (0 <= y < 10):
            print("Coordenadas no validas. Inténtalo de nuevo.")
            continue
        
        disparo_valido, acierto = disparar(tablero_maquina, (x,y))

        if disparo_valido:
           tablero_maquina = disparo_valido
           if acierto:
              acierto_jugador = acierto_jugador + 1 
        else:
            continue

        print("Turno de la maquina")

        disparo_valido_maquina = False

        while not disparo_valido_maquina:
            disparo_valido, acierto = disparar(tablero_jugador, (random.randint(0,9),random.randint(0,9)))
            if disparo_valido:
                tablero_jugador = disparo_valido
                disparo_valido_maquina = True
                if acierto:
                    acierto_maquina = acierto_maquina + 1
            else:
                continue 
        
       
        print("Final de la ronda" + str(turno))

        turno = turno + 1

        if turno == 20 or acierto_jugador == 20 or acierto_maquina == 20:
            break
        else:
            continue 

    

        """
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
                    """





main()
