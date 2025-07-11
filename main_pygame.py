import pygame
from funciones_pygame import *
pygame.init()
from prints import *

# música 
# pygame.mixer.init()
# musica_fondo = pygame.mixer.Sound('assets/cancion_fondo.mp3')
# musica_fondo.set_volume(0.50)
# musica_fondo.play(-1)
POSICION_BOTON_INICIAR = (40,395)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
#####ventana##########
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
CENTRO_PANTALLA = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Salven el Millon")#-------------------titulo de la ventana
icono = pygame.image.load("assets/ver_guita.png")#------------------ icono de la ventana
pygame.display.set_icon(icono)#------------------ icono de la ventana
# imagén de fondo
fondo = pygame.image.load('assets/susan_fondo_bienvenidad.png')
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
texto_prueba = menu
fuente_importada = pygame.font.Font('assets/PokemonGb-RAeo.ttf', 24) ####### NO RECONOCE LAS FUENTES IMPORTADAS EN BOTONES, INVESTIGAR 
superficie_texto = fuente_importada.render(texto_prueba, True, BLANCO)
posicion_texto = superficie_texto.get_rect(center=POSICION_BOTON_INICIAR)
#################################
# BOTONES
boton_iniciar = crear_boton((200, 50), POSICION_BOTON_INICIAR, VENTANA, "White", fuente=('Arial', 24), texto='Iniciar Juego')



lista_de_botones = [boton_iniciar]#lista de botones
#################################
flag_run = True 

while flag_run:
    VENTANA.fill(NEGRO)
    VENTANA.blit(fondo, (0, 0))#FONDO
    for evento in pygame.event.get():
        print(evento)
        ###############################################
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("raton presionado")
            if boton_iniciar["Rectangulo"].collidepoint(evento.pos):
                boton_iniciar['Presionado'] = True
        ###############################################
        flag_run = salida_pygame(evento, flag_run)
    for boton in lista_de_botones:
        dibujar_boton(boton_iniciar)
    if boton_iniciar['Presionado'] == True:
        print("APRETASTE EL INICIAR")
        boton_iniciar['Presionado'] = False
    pygame.display.flip()

    pygame.display.update()
    # musica_fondo.stop()  # Detiene la música al salir
pygame.quit()
