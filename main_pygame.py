import pygame
from funciones_pygame import *
pygame.init()
from prints import *

# música 
pygame.mixer.init()
musica_fondo = pygame.mixer.Sound('assets/cancion_fondo.mp3')
musica_fondo.set_volume(0.50)
musica_fondo.play(-1)

ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
CENTRO_PANTALLA = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
# imagén de fondo
fondo = pygame.image.load('assets/susan_fondo_bienvenidad.png')
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
texto_prueba = menu
fuente = pygame.font.Font('assets/PokemonGb-RAeo.ttf', 24)  
superficie_texto = fuente.render(texto_prueba, True, BLANCO)
posicion_texto = superficie_texto.get_rect(center=CENTRO_PANTALLA)
flag_run = True 

while flag_run:
    VENTANA.fill(NEGRO)
    for evento in pygame.event.get():
        print(evento)
        ###############################################

        ###############################################
        flag_run = salida_pygame(evento, flag_run)
    VENTANA.blit(fondo, (0, 0)) 
    VENTANA.blit(superficie_texto, (posicion_texto))
    pygame.display.flip()

    pygame.display.update()
    # musica_fondo.stop()  # Detiene la música al salir
