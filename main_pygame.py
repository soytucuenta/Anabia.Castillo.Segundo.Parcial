import pygame
from funciones_pygame import *
from prints import *
from leer_escribir_archivos import *
lista_usuarios = cargar_usuarios()
todas_las_preguntas = cargar_preguntas()




pygame.init()

#PROPIEDADES
ANCHO_VENTANA = 1280#francisco: los cambio porque sino no veo los botones
ALTO_VENTANA = 720
VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
CENTRO_PANTALLA = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
POSICION_BOTON_INICIAR = (40,395)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

#VENTANA PROPIEDADES
pygame.display.set_caption("SALVEN EL MILLÓN")
icono = pygame.image.load("assets/ver_guita.png")
pygame.display.set_icon(icono)

#IMÁGENES
fondo = pygame.image.load('assets/susan_fondo_bienvenidad.png')
fondo_2 = pygame.image.load('assets/susana_fondo_jugando.png')
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
fondo_jugando = pygame.transform.scale(fondo_2, (ANCHO_VENTANA, ALTO_VENTANA))

#FUENTES
texto_prueba = menu
fuente_importada = pygame.font.Font('assets/PokemonGb-RAeo.ttf',24) ####### NO RECONOCE LAS FUENTES IMPORTADAS EN BOTONES, INVESTIGAR 
superficie_texto = fuente_importada.render(texto_prueba, True, BLANCO)
posicion_texto = superficie_texto.get_rect(center=POSICION_BOTON_INICIAR)

#MÚSICA
# pygame.mixer.init()
# musica_fondo = pygame.mixer.Sound('assets/cancion_fondo.mp3')
# musica_fondo.set_volume(0.50)
# musica_fondo.play(-1)

#BOTONES
boton_iniciar = crear_boton((200, 50), POSICION_BOTON_INICIAR, VENTANA, color_texto="Black", color_fondo="Yellow", texto="Iniciar", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_estadisticas = crear_boton((200, 50), (40, 470), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Estadisticas", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_configuracion = crear_boton((200, 50), (40, 540), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Configuracion", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_seleccion_usuario = crear_boton((200, 50), (40, 610), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Seleccionar Usuario", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_salir = crear_boton((200, 50), (40, 670), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Salir", fuente=('assets/PokemonGb-RAeo.ttf', 24))
lista_de_botones_menu_principal = [boton_iniciar,boton_estadisticas, boton_configuracion,boton_seleccion_usuario,boton_salir]#lista de botones
#################################
#ESTADO DEL PROGRAMA
#Esto es un diccionario que contiene el estado del programa, para saber en que menu estamos
#y que acciones tomar en cada caso
#########
estado_del_programa = {####!!!!!!!!!! ACORDARSE DE BAJAR LAS BANDERAS CUANDO SE CAMBIA DE MENU
    "menu_principal": True,
    "partida_iniciada": False,
    "seleccion_usuario": False,
    "estadisticas": False,
    "configuracion": False,
    "salir": False,

}
#########


while estado_del_programa['salir'] == False:
    if estado_del_programa["partida_iniciada"] == False:
        VENTANA.blit(fondo, (0, 0))
    else:
        VENTANA.blit(fondo_jugando, (0, 0))
    for evento in pygame.event.get():#gestor de eventos
        print(evento)
        ###############################################
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("raton presionado")
            if estado_del_programa["menu_principal"]:#buscar como modularizar esto
                buscar_boton_presionado(lista_de_botones_menu_principal, evento)
            elif estado_del_programa["partida_iniciada"]:
                pass
            elif estado_del_programa["configuracion"]:
                pass
            elif estado_del_programa["estadisticas"]:
                pass
            elif estado_del_programa["seleccion_usuario"]:
                pass
        ###############################################
        estado_del_programa['salir'] = salida_pygame(evento)
    #############################

    # Dibujado de menues
    if estado_del_programa["menu_principal"]:
        for boton in lista_de_botones_menu_principal:
            dibujar_boton(boton)
    elif estado_del_programa["partida_iniciada"]:
        pass
    elif estado_del_programa["configuracion"]:
        pass
    elif estado_del_programa["estadisticas"]:
        pass
    elif estado_del_programa["seleccion_usuario"]:
        pass
    
    ##########################################################
    """Los booleanos que devuelven los botones pienso que pueden servir para activar o desactivar menues"""
    ##########################################################
    acciones_menu_principal(lista_de_botones_menu_principal, estado_del_programa)

    pygame.display.flip()

    #pygame.display.update()
    # musica_fondo.stop()  # Detiene la música al salir

pygame.quit()

escribir_csv_usuarios(lista_usuarios)
