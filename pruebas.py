import pygame
pygame.init()

fuentes = pygame.font.get_fonts()
for fuente in fuentes:
    print(fuente)
