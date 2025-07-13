import pygame
import numpy as np

# Inicialización
pygame.init()
ANCHO, ALTO = 700, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Tablero (6 filas x 7 columnas)
tablero = np.zeros((6, 7))  # 0 = vacío, 1 = jugador, 2 = IA

# Colores
COLOR_FONDO = (30, 30, 150)
COLOR_TABLERO = (20, 20, 120)
COLOR_JUGADOR = (255, 0, 0)
COLOR_IA = (255, 255, 0)

def dibujar_tablero():
    pygame.draw.rect(pantalla, COLOR_TABLERO, (0, 0, ANCHO, ALTO))
    for fila in range(6):
        for col in range(7):
            pygame.draw.circle(
                pantalla, 
                COLOR_FONDO if tablero[fila][col] == 0 else COLOR_JUGADOR if tablero[fila][col] == 1 else COLOR_IA,
                (col * 100 + 50, fila * 100 + 50),
                40
            )

def soltar_ficha(col, jugador):
    for fila in range(5, -1, -1):
        if tablero[fila][col] == 0:
            tablero[fila][col] = jugador
            return True
    return False  # Columna llena

# Bucle del minijuego
def minijuego_linea4():
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False  # Pierde
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, _ = evento.pos
                col = x // 100
                if soltar_ficha(col, 1):  # Ficha del jugador
                    if verificar_ganador(1):
                        return True  # Gana
                    # Turno IA (simplificado)
                    soltar_ficha(np.random.randint(0, 7), 2)
                    if verificar_ganador(2):
                        return False  # Pierde
        
        pantalla.fill((0, 0, 0))
        dibujar_tablero()
        pygame.display.flip()
        reloj.tick(60)