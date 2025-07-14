from funciones_minijuego import *
from colorama import Fore, Back, Style, init

def minijuego()->bool:
    init() 
    se_gano = False
    turno = True
    
    matriz = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
    ]

    while True:
        if turno:
            columna = ingresar_int("\nIngrese la columna: ", 1, 7)
            if not insertar_ficha(matriz, columna - 1, True):
                print("¡Columna llena! Intente con otra columna.")
                continue
        else:
            columna = generar_numero(0, 6)
            intentos = 0
            while not insertar_ficha(matriz, columna, False) and intentos < 7:
                columna = generar_numero(0, 6)
                intentos += 1
            
            if intentos >= 7:
                print("¡Empate! El tablero está lleno.")
                se_gano = False
                break
            
            print(f"\nYo elijo la columna: {columna + 1}\n")

        mostrar_matriz(matriz)
        turno = not turno

        ganador = (
            chequear_horizontal(matriz) 
            or chequear_vertical(matriz)
            or chequear_diagonal_bajada(matriz)
            or chequear_diagonal_subida(matriz)
        )

        if ganador == 1:
            se_gano = True
            break
        elif ganador == 2:
            se_gano = False
            break
        
        if verificar_empate(matriz):
            print("¡Empate! El tablero está lleno.")
            se_gano = False
            break

    if se_gano == True:
        print("¡Enhorabuena! ¡Ganó el juego!\n")
    else:
        print("Lo siento ¡usted perdió!, más suerte la próxima.\n")

    return se_gano
minijuego()