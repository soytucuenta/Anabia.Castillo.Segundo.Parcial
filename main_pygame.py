import pygame
pygame.init()
from funciones_pygame import *
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
CENTRO_PANTALLA = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
imagen = pygame.image.load('your_image.png')
texto_prueba = "Hola, esto es un texto de prueba"
fuente = pygame.font.Font(None, 36)  
superficie_texto = fuente.render(texto_prueba, True, BLANCO)
posicion_texto = superficie_texto.get_rect(center=CENTRO_PANTALLA)
flag_run = True 

while flag_run:
    VENTANA.fill(NEGRO)
    for evento in pygame.event.get():
        print(evento)
        ###############################################
        VENTANA.blit(superficie_texto, (posicion_texto))

        ###############################################
        pygame.display.flip()
        flag_run = salida_pygame(evento, flag_run)
    pygame.display.update()

