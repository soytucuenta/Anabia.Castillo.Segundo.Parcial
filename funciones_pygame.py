import pygame
def salida_pygame(evento, flag_run):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            flag_run = False
    if evento.type == pygame.QUIT:        
        flag_run = False
    return flag_run
