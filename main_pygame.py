import pygame
from funciones_pygame import *
print(pygame.ver)
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720

VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
VENTANA.fill((0, 0, 0))

flag_run = True 
while flag_run:
    for evento in pygame.event.get():
        print(evento)
        ###############################################
        



        ###############################################
        flag_run = salida_pygame(evento, flag_run)
    pygame.display.update()

