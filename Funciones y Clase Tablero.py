import numpy as np
import random

class Tablero:

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