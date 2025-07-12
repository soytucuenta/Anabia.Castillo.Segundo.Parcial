import random

def ingresar_int(mensaje, inicio, fin):
    num = int(input(mensaje))
    while num < inicio or num > fin:
        num = int(input(mensaje))
    return num

def insertar_ficha(matriz, columna, jugador):
    for i in reversed(range(len(matriz))):
        if matriz[i][columna] == 0:
            if jugador:
                matriz[i][columna] = 1
                break
            else:
                matriz[i][columna] = 2
                break

def mostrar_matriz(matriz:list):
    for i in range(len(matriz)):
        print(matriz[i])

def generar_numero(inicio:int, fin:int)->int:
    num_random = random.randint(inicio, fin)
    return num_random

def comprobar_4(fila, i):
    pass

def chequear_horizontal(matriz):
    ganador = 0
    for i in reversed(range(len(matriz))):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                contador = 1
                for k in range(j+1, len(matriz)):
                    if matriz[i][k] == 1:
                        contador += 1
                    else: 
                        break
                if contador >= 4:
                    ganador = 1
            elif matriz[i][j] == 2:
                contador = 1
                for k in range(j+1, len(matriz)):
                    if matriz[i][k] == 1:
                        contador += 1
                    else: 
                        break
                if contador >= 4:
                    ganador = 2
    return ganador   

def chequear_vertical(matriz):
    for col in range(len(matriz[0])):
        for i in range(len(matriz)-1, 2, -1):  # Desde abajo hacia arriba
            if (matriz[i][col] != 0 and
                matriz[i][col] == matriz[i-1][col] and
                matriz[i][col] == matriz[i-2][col] and
                matriz[i][col] == matriz[i-3][col]):
                return matriz[i][col]
    return 0

def chequear_diagonal_bajada(matriz):
    # Verificar diagonales principales (\) 
    for fila in range(len(matriz)-3):  # Solo necesitamos verificar hasta 3 filas antes del final
        for col in range(len(matriz[0])-3):  # Y 3 columnas antes del final
            if (matriz[fila][col] != 0 and
                matriz[fila][col] == matriz[fila+1][col+1] and
                matriz[fila][col] == matriz[fila+2][col+2] and
                matriz[fila][col] == matriz[fila+3][col+3]):
                return matriz[fila][col]
    return 0

def chequear_diagonal_subida(matriz):
    # Verificar diagonales secundarias (/)
    for fila in range(3, len(matriz)):  # Comenzamos desde la fila 3 (cuarta fila)
        for col in range(len(matriz[0])-3):  # Verificamos hasta 3 columnas antes del final
            if (matriz[fila][col] != 0 and
                matriz[fila][col] == matriz[fila-1][col+1] and
                matriz[fila][col] == matriz[fila-2][col+2] and
                matriz[fila][col] == matriz[fila-3][col+3]):
                return matriz[fila][col]
    return 0
