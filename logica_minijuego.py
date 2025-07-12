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
            insertar_ficha(matriz, columna - 1, True)
        else:
            columna = generar_numero(0, 6)
            insertar_ficha(matriz, columna, False)
            print(f"\nYo elijo la columna: {columna + 1}\n")

        mostrar_matriz(matriz)
        turno = not turno

        ganador = chequear_horizontal(matriz)
        ganador = chequear_vertical(matriz)
        # ganador = chequear_diagonal_bajada()
        # ganador = chequear_diagonal_subida()

        

        empate = 0
        if ganador == 1:
            se_gano = True
            break
        if empate == 1 or ganador == 2:
            se_gano = False
            break

    if se_gano == True:
        print("¡Enorabuena! Ganó el juego!\n")
    else:
        print("Lo siento ¡usted perdió!, más suerte la próxima.\n")

    return se_gano

minijuego()