import pygame
from usuarios import *
from config import *
def salida_pygame(evento):
    """
    Maneja los eventos de salida de Pygame para actualizar la bandera de ejecución.
    Parámetros:
        evento (pygame.event.Event): El evento de Pygame a procesar.
        flag_run (bool): El estado actual de la bandera de ejecución.
    Retorna:
        bool: Bandera de ejecución actualizada. Retorna False si se presiona la tecla ESC o se cierra la ventana, de lo contrario retorna el valor original de flag_run.
    """
    bandera = False
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:#cambiable por si queremos retroceder a un menu despues
            bandera = True
    elif evento.type == pygame.QUIT:        
        bandera = True
    return bandera


#######################
def manipular_texto(evento, texto, limite = 11):
    """
    Maneja los eventos de entrada de texto para una aplicación Pygame, permitiendo agregar caracteres y eliminar con retroceso.
    Args:
        evento (pygame.event.Event): El objeto de evento de Pygame que contiene la información de la tecla presionada.
        texto (str): La cadena de texto actual a manipular.
        limite (int, opcional): La longitud máxima permitida del texto. Por defecto es 11.
    Returns:
        str: La cadena de texto actualizada después de procesar el evento de entrada.
    """

    if evento.key == pygame.K_BACKSPACE:
        texto = texto[:-1]
    else:
        if len(texto) <= limite:
            texto += evento.unicode
    return texto

def crear_boton(dimensiones, posicion, ventana, color_texto="Black", color_fondo="Yellow", imagen=None, fuente=None, texto=None):
    """
    Crea un diccionario que representa un botón para usar en una interfaz gráfica con Pygame.
    Args:
        dimensiones (tuple): Tamaño del botón como (ancho, alto).
        posicion (tuple): Posición del botón en la ventana como (x, y).
        ventana (pygame.Surface): Superficie de Pygame donde se dibujará el botón.
        color_texto (str or tuple, optional): Color del texto del botón. Por defecto es "Black".
        color_fondo (str or tuple, optional): Color de fondo del botón. Por defecto es "Yellow".
        imagen (str, optional): Ruta a una imagen para usar como fondo del botón. Si se proporciona, se ignoran fuente y texto.
        fuente (tuple, optional): Tupla con el nombre de la fuente y tamaño (nombre_fuente, tamaño). Por defecto usa "droidsans" y tamaño 24.
        texto (str, optional): Texto a mostrar en el botón. Solo se usa si no se proporciona una imagen.
    Returns:
        dict: Diccionario con las propiedades del botón, incluyendo la superficie, rectángulo, colores, estado y referencia a la ventana.
    """
    

    boton = {}
    boton["Ventana"] = ventana
    boton["Dimensiones"] = dimensiones
    boton["Posicion"] = posicion
    boton['ColorTexto'] = color_texto
    boton['ColorFondo'] = color_fondo
    boton["Presionado"] = False
    boton['Habilitado'] = True
    if imagen != None:
        img = pygame.image.load(imagen)
        boton["Superficie"] = pygame.transform.scale(img, boton["Dimensiones"])
    else:
        if fuente == None:
            fuente = pygame.font.Font("droidsans", 24)
        tipo, tamano = fuente
        fuente = pygame.font.SysFont(tipo, tamano)
        boton["Superficie"] = fuente.render(texto,False, color_texto,color_fondo)
    boton["Rectangulo"] = boton["Superficie"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]
    

    return boton

def dibujar_boton(boton:dict):
    """
    Dibuja un botón en la ventana de Pygame especificada usando las propiedades definidas en el diccionario dado.
    Args:
        boton (dict): Un diccionario que contiene las siguientes claves:
            - "Ventana": La superficie de Pygame (ventana) donde se dibujará el botón.
            - "Superficie": La superficie de Pygame que representa la apariencia del botón.
            - "Posicion": Una tupla (x, y) que indica la posición para dibujar el botón.
            - "ColorTexto": El color (tupla RGB) para el borde del botón.
            - "Rectangulo": Un objeto pygame.Rect que define el área rectangular del botón.
    Returns:
        None
    """

    boton["Ventana"].blit(boton["Superficie"], boton["Posicion"])
    pygame.draw.rect(boton["Ventana"],boton["ColorTexto"],boton["Rectangulo"],2)

def boton_presionado(boton:dict, evento):
    """
    Verifica si un botón ha sido presionado basado en un evento dado.
    Args:
        boton (dict): Un diccionario que representa el botón, debe tener la clave 'Rectangulo' con un valor de tipo pygame.Rect.
        evento: El objeto de evento, típicamente un evento de pygame, que debe tener el atributo 'pos' indicando la posición del mouse.
    Returns:
        bool: True si la posición del evento colisiona con el rectángulo del botón, False en caso contrario.
    """

    bandera = False
    if boton['Rectangulo'].collidepoint(evento.pos) and boton['Habilitado']:
        bandera = True
    return bandera

def buscar_boton_presionado(lista_botones, evento):
    for boton in lista_botones:                    
        if boton_presionado(boton,evento):
            boton['Presionado'] = True


def acciones_menu_principal(lista_de_botones_menu_principal,estado_del_programa):
    boton_iniciar = lista_de_botones_menu_principal[0]
    boton_estadisticas = lista_de_botones_menu_principal[1]
    boton_configuracion = lista_de_botones_menu_principal[2]
    boton_seleccion_usuario = lista_de_botones_menu_principal[3]
    boton_salir = lista_de_botones_menu_principal[4]

    for boton in lista_de_botones_menu_principal:
        if boton['Presionado']:
            boton['Presionado'] = False
            if boton == boton_salir:
                estado_del_programa["salir"] = True
            elif boton == boton_iniciar and boton_iniciar['Habilitado']:#chequear si se selecciono un usuario pendiente
                estado_del_programa["partida_iniciada"] = True
                estado_del_programa["menu_principal"] = False
                print("Iniciar partida")
            elif boton == boton_estadisticas:
                print("Estadísticas seleccionadas")
                estado_del_programa["estadisticas"] = True
                estado_del_programa["menu_principal"] = False
            elif boton == boton_seleccion_usuario:
                print("Seleccionar usuario")
                estado_del_programa["seleccion_usuario"] = True
                estado_del_programa["menu_principal"] = False
            elif boton == boton_configuracion:
                estado_del_programa["configuracion"] = True
                estado_del_programa["menu_principal"] = False
                print("Configuración seleccionada")



def acciones_menu_configuracion(lista_de_botones_menu_configuracion, estado_del_programa, info_usuario):
    boton_dificultad = lista_de_botones_menu_configuracion[0]
    boton_categoria = lista_de_botones_menu_configuracion[1]
    boton_daltonismo = lista_de_botones_menu_configuracion[2]
    boton_menu_principal = lista_de_botones_menu_configuracion[3]

    for boton in lista_de_botones_menu_configuracion:
        if boton['Presionado']:
            boton['Presionado'] = False
            if boton == boton_dificultad:
                print(f"Dificultad ANTES: {info_usuario['dificultad']}")
                info_usuario['dificultad'] = cambiar_dificultad_pygame(info_usuario['dificultad'])
                print(f"Dificultad DESPUÉS: {info_usuario['dificultad']}")
            elif boton == boton_categoria:
                print("Cambiar categoria")
            elif boton == boton_daltonismo:
                print("Cambiar daltonismo")
            elif boton == boton_menu_principal:
                estado_del_programa["menu_principal"] = True
                estado_del_programa["configuracion"] = False

def buscar_usuario_pygame(lista_usuarios:list, usuario:str)-> dict:
    if buscar_nombre_en_lista_diccionarios(usuario, lista_usuarios):
        usuario_encontrado = copiar_usuario_por_nombre(usuario, lista_usuarios)
    else:
        usuario_encontrado = {"id": len(lista_usuarios) + 1, "nombre": usuario, "ganancias": 0, "participaciones": 0, "mejor racha": 0, "ranking": 0, "dificultad": "media"}
    return usuario_encontrado

