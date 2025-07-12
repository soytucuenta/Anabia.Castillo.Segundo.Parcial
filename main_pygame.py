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
fuente_basica = pygame.font.Font(None, 36)  # Fuente básica para el input box
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
##################

texto_usuario  = ''
rectangulo_usuario = pygame.Rect(40, 500, 325, 50)  # Rectángulo para el input box
color_usuario = pygame.Color('cyan')  # Color del texto del input box
boton_usuario = crear_boton((250, 75), (60, 300), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Guardar y volver al menu anterior", fuente=('assets/PokemonGb-RAeo.ttf', 24))


#################################
#ESTADO DEL PROGRAMA
#Esto es un diccionario que contiene el estado del programa, para saber en que menu estamos
#y que acciones tomar en cada caso
#########
estado_del_programa = {####!!!!!!!!!! ACORDARSE DE BAJAR LAS BANDERAS CUANDO SE CAMBIA DE MENU
    "menu_principal": True,
    "partida_iniciada": False,
    "seleccion_usuario": False,
    "cuadro_texto_usuario": False,
    'usuario_elegido_exitoso': False,
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
                if rectangulo_usuario.collidepoint(evento.pos):
                    estado_del_programa["cuadro_texto_usuario"] = True
                elif boton_presionado(boton_usuario, evento) and boton_usuario['Habilitado']:
                    estado_del_programa["seleccion_usuario"] = False
                    estado_del_programa["cuadro_texto_usuario"] = False
                    estado_del_programa["menu_principal"] = True

        elif evento.type == pygame.KEYDOWN:
            if estado_del_programa["seleccion_usuario"] and estado_del_programa["cuadro_texto_usuario"] == True:
                texto_usuario = manipular_texto(evento, texto_usuario)
                if len(texto_usuario) < 1:
                    boton_usuario['Habilitado'] = False
                
        ###############################################
        estado_del_programa['salir'] = salida_pygame(evento)
    #############################

    # if estado_del_programa["seleccion_usuario"]:
    #     #usuario = input_box(estado_del_programa,(200, 50), (40, 300), VENTANA, color_texto="Black", color_fondo="Yellow", fuente=('assets/PokemonGb-RAeo.ttf', 24))
    #     pass
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
        pygame.draw.rect(VENTANA, color_usuario, rectangulo_usuario,3)  # Dibuja el rectángulo del input box
        superficie_seleccion_usuario = fuente_importada.render(texto_usuario, True, color_usuario)
        VENTANA.blit(superficie_seleccion_usuario, (rectangulo_usuario.x + 5, rectangulo_usuario.y + 5))  # Dibuja el texto dentro del input box
        dibujar_boton(boton_usuario)
    
    ##########################################################
    """Los booleanos que devuelven los botones pienso que pueden servir para activar o desactivar menues"""
    ##########################################################
    acciones_menu_principal(lista_de_botones_menu_principal, estado_del_programa)

    pygame.display.flip()

    #pygame.display.update()
    # musica_fondo.stop()  # Detiene la música al salir

pygame.quit()

escribir_csv_usuarios(lista_usuarios)
