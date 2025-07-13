import pygame
from funciones_pygame import *
from prints import *
from leer_escribir_archivos import *
from usuarios import *
from menues_pygame import *
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

#########
#ESTADO DEL PROGRAMA
#Esto es un diccionario que contiene el estado del programa, para saber en que menu estamos
#y que acciones tomar en cada caso
estado_del_programa = {####!!!!!!!!!! ACORDARSE DE BAJAR LAS BANDERAS CUANDO SE CAMBIA DE MENU
    "menu_principal": True,
    "partida_iniciada": False,
    "seleccion_usuario": False,
    'usuario_elegido_exitoso': False,
    "usuario_ya_cargado": False,
    "estadisticas": False,
    "configuracion": False,
    'partida_lista': False,
    "salir": False,

}

info_usuario = {"id": 0, "nombre": None, "ganancias": 0, "participaciones": 0, "mejor racha": 0, "ranking": 0, "dificultad": "media"} #diccionario que contiene los datos del usuario seleccionado
#########
#FUENTES

fuente_importada = pygame.font.Font('assets/PokemonGb-RAeo.ttf',24) ####### NO RECONOCE LAS FUENTES IMPORTADAS EN BOTONES, INVESTIGAR 

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
boton_usuario = crear_boton((250, 75), (40, 300), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Guardar y volver al menu anterior", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_usuario['Habilitado'] = False  # Deshabilitado inicialmente

#################################

boton_dificultad = crear_boton((200, 50), (40, 395), VENTANA, color_texto="Black", color_fondo="Yellow", texto=f"Dificultad: {info_usuario['dificultad']}", fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_categoria = crear_boton((200, 50), (40, 470), VENTANA, color_texto="Black", color_fondo="Yellow", texto=f'Categoria: {configuracion_pygame['categoria']}', fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_daltonismo = crear_boton((200, 50), (40, 540), VENTANA, color_texto="Black", color_fondo="Yellow", texto=f'Daltonismo: {configuracion_pygame['daltonismo']}', fuente=('assets/PokemonGb-RAeo.ttf', 24))
boton_menu_principal = crear_boton((200, 50), (40, 610), VENTANA, color_texto="Black", color_fondo="Yellow", texto="Menu Principal", fuente=('assets/PokemonGb-RAeo.ttf', 24))
lista_de_botones_menu_configuracion = [boton_dificultad, boton_categoria, boton_daltonismo, boton_menu_principal]#lista de botones


while estado_del_programa['salir'] == False:
    if estado_del_programa["partida_iniciada"] == False:
        VENTANA.blit(fondo, (0, 0))
    else:
        VENTANA.blit(fondo_jugando, (0, 0))
    if estado_del_programa["usuario_elegido_exitoso"] and len(texto_usuario.strip()) > 0 and estado_del_programa["usuario_ya_cargado"] == False:
        info_usuario = buscar_usuario_pygame(lista_usuarios, texto_usuario)
        estado_del_programa["usuario_ya_cargado"] = True
        
    for evento in pygame.event.get():#gestor de eventos
        print(evento)
        ###############################################
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("raton presionado")
            if estado_del_programa["menu_principal"]:
                buscar_boton_presionado(lista_de_botones_menu_principal, evento)
            elif estado_del_programa["partida_iniciada"]:
                pass
            elif estado_del_programa["configuracion"]:
                buscar_boton_presionado(lista_de_botones_menu_configuracion, evento)
            elif estado_del_programa["estadisticas"]:
                pass
            elif estado_del_programa["seleccion_usuario"]:
                if rectangulo_usuario.collidepoint(evento.pos):
                    estado_del_programa["cuadro_texto_usuario"] = True
                elif boton_presionado(boton_usuario, evento) and boton_usuario['Habilitado']:
                    estado_del_programa["seleccion_usuario"] = False
                    estado_del_programa["menu_principal"] = True
                    estado_del_programa['usuario_elegido_exitoso'] = True

        elif evento.type == pygame.KEYDOWN:
            if estado_del_programa["seleccion_usuario"] and estado_del_programa["cuadro_texto_usuario"] == True:
                texto_usuario = manipular_texto(evento, texto_usuario)
                if len(texto_usuario.strip()) >0:
                    boton_usuario['Habilitado'] = True
                else:
                    boton_usuario['Habilitado'] = False

                
        ###############################################
        estado_del_programa['salir'] = salida_pygame(evento)
    #############################

    # Dibujado segun estado del programa
    if estado_del_programa["menu_principal"]:
        for boton in lista_de_botones_menu_principal:
            dibujar_boton(boton)
        acciones_menu_principal(lista_de_botones_menu_principal, estado_del_programa)
    elif estado_del_programa["partida_iniciada"]:
        pass
    elif estado_del_programa["configuracion"]:######### FALTA CAGAR LA CONFIGURACION DEL JUEGO DESDE JSON Y GUARDARLA
        for boton in lista_de_botones_menu_configuracion:
            dibujar_boton(boton)
        acciones_menu_configuracion(lista_de_botones_menu_configuracion, estado_del_programa,info_usuario)
    elif estado_del_programa["estadisticas"]:
        #mostrar_texto_multilinea(VENTANA, (ANCHO_VENTANA // 2 -600, ALTO_VENTANA // 2 + 50), cortar_string_por_palabras(texto_prueba2,50), fuente_importada,color='black', color_fondo="Yellow")
    elif estado_del_programa["seleccion_usuario"]:
        dibujar_seleccion_usuario(VENTANA,fuente_importada, rectangulo_usuario, color_usuario, texto_usuario, boton_usuario)


    pygame.display.flip()

    #pygame.display.update()
    # musica_fondo.stop()  # Detiene la música al salir

pygame.quit()
if estado_del_programa['usuario_elegido_exitoso']:
    sincronizar_diccionario(info_usuario, lista_usuarios, "id")
    escribir_csv_usuarios(lista_usuarios)
