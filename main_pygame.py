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
fuente_importada = pygame.font.Font('assets/PokemonGb-RAeo.ttf',24) ####### NO RECONOCE LAS FUENTES IMPORTADAS EN BOTONES, INVESTIGAR 
superficie_texto = fuente_importada.render(texto_prueba, True, BLANCO)
posicion_texto = superficie_texto.get_rect(center=POSICION_BOTON_INICIAR)
#################################
# BOTONES
boton_iniciar = crear_boton((200, 50), POSICION_BOTON_INICIAR, VENTANA, color_texto="Black", color_fondo="Yellow", texto="Iniciar", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_estadisticas = crear_boton((200, 50), (40, 470), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Estadisticas", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_configuracion = crear_boton((200, 50), (40, 540), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Configuracion", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_salir = crear_boton((200, 50), (40, 610), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Salir", fuente=('assets/PokemonGb-RAeo.ttf', 24))



lista_de_botones_menu_principal = [boton_iniciar,boton_estadisticas, boton_configuracion,boton_salir]#lista de botones
#################################
#banderas menues
flag_menu_principal = True



#########
flag_run = True 

while flag_run:
    VENTANA.fill(NEGRO)
    VENTANA.blit(fondo, (0, 0))#FONDO
    for evento in pygame.event.get():
        print(evento)
        ###############################################
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("raton presionado")
            if flag_menu_principal:#buscar como modularizar esto
                if boton_presionado(boton_iniciar,evento):
                    boton_iniciar['Presionado'] = True
                elif boton_presionado(boton_estadisticas,evento):
                    boton_estadisticas['Presionado'] = True
                elif boton_presionado(boton_configuracion,evento):
                    boton_configuracion['Presionado'] = True
                elif boton_presionado(boton_salir,evento):
                    boton_salir['Presionado'] = True
        ###############################################
        salida_pygame(evento, flag_run)
    if flag_menu_principal:
        for boton in lista_de_botones_menu_principal:
            dibujar_boton(boton)
    ##########################################################
    """Los booleanos que devuelven los botones pienso que pueden servir para activar o desactivar menues"""
    ##########################################################
    if boton_iniciar['Presionado'] == True:
        print("APRETASTE EL INICIAR")
        boton_iniciar['Presionado'] = False
        flag_menu_principal = False
    elif boton_estadisticas['Presionado']:
        print("apretaste stats")
        boton_estadisticas['Presionado'] = False
    elif boton_configuracion['Presionado']:
        print("apretaste configuracion")
        boton_configuracion['Presionado'] = False
    elif boton_salir['Presionado']:
        print("apretaste salir")
        flag_run = False
        # pygame.quit()  # Descomentar si se quiere cerrar la ventana al salir del juego

    pygame.display.flip()

    pygame.display.update()
    # musica_fondo.stop()  # Detiene la música al salir
pygame.quit()
