import pygame
from usuarios import *
from config import *
from stats import *
def cortar_string_por_palabras(texto, longitud_maxima):

    palabras = texto.split()
    lineas = []
    linea_actual = ""
    
    for palabra in palabras:
        if len(linea_actual + " " + palabra) <= longitud_maxima:
            if linea_actual:
                linea_actual += " " + palabra
            else:
                linea_actual = palabra
        else:
            if linea_actual:
                lineas.append(linea_actual)
            linea_actual = palabra
    if linea_actual:
        lineas.append(linea_actual)
    return lineas

lista_daltonismo = ['protanopia', 'deuteranopia', 'tritanopia', 'no']
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


def mostrar_texto(superficie, posicion , texto, fuente,color=(255, 255, 255), color_fondo=None, centrado=False):
    """
    Dibuja texto en una superficie de Pygame en una posición especificada, con color de fondo y centrado opcionales.
    Args:
        superficie (pygame.Surface): Superficie donde se dibujará el texto.
        posicion (tuple): Posición (x, y) para dibujar el texto. Si 'centrado' es True, es el centro; si no, es la esquina superior izquierda.
        texto (str): Cadena de texto a renderizar.
        fuente (pygame.font.Font): Objeto de fuente para renderizar el texto.
        color (tuple, opcional): Color RGB del texto. Por defecto es (255, 255, 255).
        color_fondo (tuple o None, opcional): Color RGB de fondo del texto. Si es None, el fondo es transparente. Por defecto es None.
        centrado (bool, opcional): Si es True, centra el texto en 'posicion'. Si es False, lo dibuja desde la esquina superior izquierda. Por defecto es False.
    Returns:
        pygame.Rect: Rectángulo que representa el área del texto renderizado en la superficie.
    """
    
    texto_surface = fuente.render(texto, True, color, color_fondo)
    
    texto_rect = texto_surface.get_rect()
    
    if centrado:
        texto_rect.center = posicion
    else:
        texto_rect.topleft = posicion
    
    superficie.blit(texto_surface, texto_rect)
    
    return texto_rect

def mostrar_texto_multilinea(superficie, posicion, lineas, fuente, color=(255, 255, 255),color_fondo=None, espaciado=5, centrado=False):
    """
    Renderiza múltiples líneas de texto en una superficie de Pygame, permitiendo opciones de color, fondo, espaciado y centrado.
    Args:
        superficie (pygame.Surface): Superficie donde se dibujará el texto.
        posicion (tuple): Coordenadas (x, y) iniciales para el texto.
        lineas (list): Lista de cadenas de texto a mostrar, cada una será una línea.
        fuente (pygame.font.Font): Fuente utilizada para renderizar el texto.
        color (tuple, optional): Color del texto en formato RGB. Por defecto es blanco (255, 255, 255).
        color_fondo (tuple, optional): Color de fondo del texto en formato RGB. Si es None, el fondo será transparente.
        espaciado (int, optional): Espacio en píxeles entre líneas de texto. Por defecto es 5.
        centrado (bool, optional): Si es True, centra el texto horizontalmente respecto a la posición dada.
    Returns:
        None
    """
        
    y_actual = posicion[1]
    for linea in lineas:
        linea = mostrar_texto(superficie,(posicion[0], y_actual), linea, fuente, color, color_fondo,
                            centrado=centrado)
        y_actual += linea.height + espaciado

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
            fuente = pygame.font.Font(None, 24)
        tipo, tamano = fuente
        fuente = pygame.font.Font(tipo, tamano)
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
    """
    Busca en una lista de botones cuál ha sido presionado según un evento dado y marca su estado como presionado.
    Args:
        lista_botones (list): Lista de diccionarios que representan los botones, cada uno con sus propiedades.
        evento (pygame.event.Event): Evento de Pygame que se utiliza para determinar si un botón ha sido presionado.
    Returns:
        None: La función modifica la lista de botones en su lugar, estableciendo la clave 'Presionado' en True para el botón correspondiente.
    """

    for boton in lista_botones:                    
        if boton_presionado(boton,evento):
            boton['Presionado'] = True

def actualizar_texto_boton(boton, nuevo_texto):
    """Actualiza el texto de un botón existente"""
    fuente = pygame.font.Font('assets/PokemonGb-RAeo.ttf', 24)
    boton["Superficie"] = fuente.render(nuevo_texto, False, boton['ColorTexto'], boton['ColorFondo'])
    boton["Rectangulo"] = boton["Superficie"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]

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

# def mostrar_usuarios_top(lista_dicc_usuarios:list, cantidad:int = 10, clave:str = 'ranking', juego_grafico:bool = False,
#                         superficie = None, posicion = (0,0), fuente = None, color = None, color_fondo = None, espaciado = 5, centrado = False):
#     """
#     Muestra los usuarios con el mejor ranking.
#     Args:
#         lista_dicc_usuarios (list): Lista de diccionarios de usuarios.
#         cantidad (int): Cantidad de usuarios a mostrar. Por defecto es 10.
#         clave (str): Clave por la cual ordenar. Por defecto es 'ranking'.
#         juego_grafico (bool): Si True, muestra en modo gráfico. Por defecto es False.
#         superficie: Superficie de pygame donde dibujar (requerido si juego_grafico=True).
#         posicion (tuple): Posición inicial (x, y) para el texto. Por defecto es (0,0).
#         fuente: Fuente para el texto (requerido si juego_grafico=True).
#         color: Color del texto.
#         color_fondo: Color de fondo del texto.
#         espaciado (int): Espaciado entre líneas. Por defecto es 5.
#         centrado (bool): Si el texto debe estar centrado. Por defecto es False.
#     """
#     lista_top = burbujear_top(lista_dicc_usuarios, cantidad, clave)
    
#     if juego_grafico == False:
#         print(f"Top {cantidad} usuarios:")
#         for usuario in lista_top:
#             print(f"Nombre: {usuario['nombre']}, Ganancias: {usuario['ganancias']}, Mejor racha: {usuario['mejor racha']}, Ranking: {usuario['ranking']}")
#     else:
#         lineas = formatear_usuarios_string(lista_top)
#         for linea in lineas:
#             print(linea)  # Imprime en consola para depuración
#         mostrar_texto_multilinea(superficie, posicion, lineas, fuente, color, color_fondo, espaciado, centrado)


def mostrar_top_simple(lista_dicc_usuarios:list,superficie, fuente,color ,color_fondo ,cantidad:int = 10, clave:str = 'ranking'):
    lista_top = burbujear_top(lista_dicc_usuarios, cantidad, clave)
    lista_formateada = formatear_usuarios_string(lista_top)
    for linea in lista_formateada:
        mostrar_texto_multilinea(superficie, (40, 100), [linea], fuente, color, color_fondo, espaciado=5, centrado=False)
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
                actualizar_texto_boton(boton_dificultad, f"Dificultad: {info_usuario['dificultad']}")
                print(f"Dificultad DESPUÉS: {info_usuario['dificultad']}")
            elif boton == boton_categoria:
                print("Cambiar categoria")
                configuracion_pygame['categoria'] = cambiar_categoria_pygame(configuracion_pygame['categoria'])
                actualizar_texto_boton(boton_categoria, f'Categoria: {configuracion_pygame["categoria"]}')
                print(f"Categoria seleccionada: {configuracion_pygame['categoria']}")
            elif boton == boton_daltonismo:
                print("Cambiar daltonismo")
                configuracion_pygame['daltonismo'] = cambiar_categoria_pygame(configuracion_pygame['daltonismo'], lista_daltonismo, configuracion_pygame['daltonismo'])
                actualizar_texto_boton(boton_daltonismo, f'Daltonismo: {configuracion_pygame["daltonismo"]}')
                print(f"Daltonismo seleccionado: {configuracion_pygame['daltonismo']}")
            elif boton == boton_menu_principal:
                estado_del_programa["menu_principal"] = True
                estado_del_programa["configuracion"] = False


def acciones_menu_estadisticas():
    pass


def buscar_usuario_pygame(lista_usuarios:list, usuario:str)-> dict:
    """
    Busca un usuario en una lista de diccionarios de usuarios. Si el usuario existe, lo retorna; 
    si no, crea y retorna un nuevo diccionario de usuario con valores predeterminados.
    Args:
        lista_usuarios (list): Lista de diccionarios, cada uno representando un usuario.
        usuario (str): Nombre del usuario a buscar.
    Returns:
        dict: Diccionario con los datos del usuario encontrado o uno nuevo si no existe.
    """

    if buscar_nombre_en_lista_diccionarios(usuario, lista_usuarios):
        usuario_encontrado = copiar_usuario_por_nombre(usuario, lista_usuarios)
    else:
        usuario_encontrado = {"id": len(lista_usuarios) + 1, "nombre": usuario, "ganancias": 0, "participaciones": 0, "mejor racha": 0, "ranking": 0, "dificultad": "media"}
    return usuario_encontrado

