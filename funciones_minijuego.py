import random
from colorama import Fore, Back, Style, init
init() 

def ingresar_int(mensaje, inicio, fin):
    """
    Solicita un número entero al usuario dentro del rango especificado.
    Maneja errores de entrada y repite la solicitud si es necesario.
    """
    while True:
        
        num = int(input(mensaje))
        if inicio <= num <= fin:
            return num
        else:
            print(f"Por favor, ingrese un número entre {inicio} y {fin}.")


def insertar_ficha(matriz, columna, jugador):
    """
    Inserta una ficha en la columna especificada.
    Retorna True si se pudo insertar, False si la columna está llena.
    """
    resultado = False
    for i in reversed(range(len(matriz))):
        if matriz[i][columna] == 0:
            if jugador:
                matriz[i][columna] = 1
            else:
                matriz[i][columna] = 2
            resultado = True
            break
    return resultado

def verificar_empate(matriz):
    """
    Verifica si el tablero está lleno (empate).
    """
    resultado = True
    for fila in matriz:
        for celda in fila:
            if celda == 0:
                resultado =  False
    return resultado

def mostrar_matriz(matriz:list):
    """
    Muestra la matriz del juego con colores.
    """
    print("\n  1 2 3 4 5 6 7")
    print(" ---------------")
    for i in range(len(matriz)):
        print("|", end="")
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                print(Fore.RED + "●" + Style.RESET_ALL, end="|")
            elif matriz[i][j] == 2:
                print(Fore.YELLOW + "●" + Style.RESET_ALL, end="|")
            else:
                print(" ", end="|")
        print()
    print(" ---------------\n")

def generar_numero(inicio:int, fin:int)->int:
    """
    Genera un número aleatorio entre inicio y fin (inclusivo).
    """
    num_random = random.randint(inicio, fin)
    return num_random

def chequear_horizontal(matriz):
    """
    Verifica si hay 4 fichas consecutivas horizontalmente.
    """
    ganador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i]) - 3): 
            if matriz[i][j] != 0:
                if (matriz[i][j] == matriz[i][j+1] == 
                    matriz[i][j+2] == matriz[i][j+3]):
                    ganador = matriz[i][j]
                    break
        if ganador != 0:
            break
    return ganador   

def chequear_vertical(matriz):
    """
    Verifica si hay 4 fichas consecutivas verticalmente.
    """
    resultado = 0
    for col in range(len(matriz[0])):
        for i in range(len(matriz) - 3): 
            if matriz[i][col] != 0:
                if (matriz[i][col] == matriz[i+1][col] == 
                    matriz[i+2][col] == matriz[i+3][col]):
                    resultado = matriz[i][col]
    return resultado

def chequear_diagonal_bajada(matriz):
    """
    Verifica diagonales principales (\) - de arriba-izquierda a abajo-derecha.
    """
    resultado = 0
    for fila in range(len(matriz)-3):
        for col in range(len(matriz[0])-3):
            if matriz[fila][col] != 0:
                if (matriz[fila][col] == matriz[fila+1][col+1] == 
                    matriz[fila+2][col+2] == matriz[fila+3][col+3]):
                    resultado = matriz[fila][col]
    return resultado

def chequear_diagonal_subida(matriz):
    """
    Verifica diagonales secundarias (/) - de abajo-izquierda a arriba-derecha.
    """
    resultado = 0
    for fila in range(3, len(matriz)):
        for col in range(len(matriz[0])-3):
            if matriz[fila][col] != 0:
                if (matriz[fila][col] == matriz[fila-1][col+1] == 
                    matriz[fila-2][col+2] == matriz[fila-3][col+3]):
                    resultado = matriz[fila][col]
    return resultado