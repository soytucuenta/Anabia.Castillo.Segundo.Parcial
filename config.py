from leer_escribir_archivos import *
from preguntas import obtener_preguntas_filtrando

configuracion_default = {
    "dificultad": "media",
    "categoria": None,
    "neurodivergente": False,
    "recuperatorio": False
}


def limitar_tiempo(dificultad:str) -> int:
    """
    Limita el tiempo de respuesta según la dificultad.
    Args:
        dificultad (str): Dificultad del juego ('facil', 'media', 'dificil').
    Returns:
        int: Tiempo límite en segundos.
    """
    if dificultad == 'facil':
        tiempo = 90
    elif dificultad == 'media':
        tiempo = 60
    else:
        tiempo = 30
    return tiempo


def preparar_partida(config:dict, todas_las_preguntas:list,dificultad_usuario) -> tuple:
    """
    Prepara la configuración de una partida seleccionando preguntas y estableciendo el tiempo límite.

    Args:
        config (dict): Diccionario de configuración que debe contener las claves 'dificultad' y 'categoria'.
        todas_las_preguntas (list): Lista de todas las preguntas disponibles.

    Returns:
        tuple: Una tupla que contiene:
            - tiempo_limite (int): El tiempo límite en segundos según la dificultad seleccionada.
            - preguntas_filtradas (list): Lista de preguntas filtradas según la dificultad y, si corresponde, la categoría seleccionada.

    Notas:
        - Si no se selecciona una categoría, se utilizarán preguntas de todo el pool.
    """
    if dificultad_usuario != None:
        config['dificultad'] = dificultad_usuario
    cantidad_preguntas = determinar_cantidad_preguntas(config)
    tiempo_limite = limitar_tiempo(config['dificultad'])
    print(f"\nTiempo limite: {tiempo_limite} segundos")
    if config['categoria'] == None:
        print("\nNo se ha seleccionado una categoria, se jugara con todo el pool de preguntas.")
        preguntas_filtradas = obtener_preguntas_filtrando(todas_las_preguntas, cantidad_preguntas, dificultad=config['dificultad'])
    else:
        print(f"\nCategoria seleccionada: {config['categoria']}")
        preguntas_filtradas = obtener_preguntas_filtrando(todas_las_preguntas, cantidad_preguntas, dificultad=config['dificultad'], categoria=config['categoria'])
    tupla_salida = (tiempo_limite, preguntas_filtradas)
    return tupla_salida


def determinar_cantidad_preguntas(config:dict) -> int:
    """
    Determina la cantidad de preguntas a realizar en función de la configuración del juego.

    Args:
        config (dict): Diccionario de configuración que debe contener la clave 'dificultad'.

    Returns:
        int: Cantidad de preguntas a realizar.
    """
    if config['dificultad'] == 'facil':
        cantidad_preguntas = 5
    elif config['dificultad'] == 'media':
        cantidad_preguntas = 7
    else:
        cantidad_preguntas = 12
    return cantidad_preguntas

def configurar_juego(config:dict, lista_mensajes:list) -> dict:
    """
    Función para configurar las opciones del juego.
    
    Args:
        config (dict): Diccionario con la configuración actual del juego
        mensaje_configuraciones (str): Mensaje del menú de configuraciones
        mensaje_dificultad (str): Mensaje para seleccionar dificultad
        mensaje_categoria (str): Mensaje para seleccionar categoría
    
    Returns:
        dict: Diccionario con la configuración actualizada
    """
    mensaje_configuraciones = lista_mensajes [0]
    mensaje_dificultad = lista_mensajes [1]
    mensaje_categoria = lista_mensajes [2]  
    seleccion_configuracion = int(input(mensaje_configuraciones))
    while seleccion_configuracion != 4:
        match seleccion_configuracion:
            case 1:
                print(f"\nDificultad actual: {config['dificultad']}")
                config['dificultad'] = seleccion_dificultad(mensaje_dificultad, config['dificultad'])
                print(f"\nDificultad seleccionada: {config['dificultad']}")
            case 2:
                print(f"\nCategoria actual: {config['categoria']}")
                config['categoria'] = seleccion_categoria(mensaje_categoria, config['categoria'])
            case 3:
                mostrar_diccionario_individual(config, "\nMostrando configuracion actual: \n")
        
        seleccion_configuracion = int(input(mensaje_configuraciones))
    
    return config


def seleccion_dificultad(mensaje_menu:str, valor_actual: str):
    control = valor_actual
    seleccion = int(input(mensaje_menu))
    while seleccion != 4:
        match seleccion:
            case 1:
                dificultad = 'fácil'
            case 2:
                dificultad = 'media'
            case 3:
                dificultad = 'difícil'
            case 4:
                dificultad = None
                break
        seleccion = int(input(mensaje_menu))
    if dificultad == None:
        dificultad = control
    return dificultad
def seleccion_categoria(mensaje_menu: str, valor_actual: str):
    control = valor_actual
    lista_categorias = [ #esto puede entrar por una lectura de lista de preguntas
        "ciencia",
        "arte",
        "historia",
        "matemáticas",
        "deportes",
        "geografía"
    ]
    categoria = None
    seleccion = int(input(mensaje_menu))
    while seleccion != 8:
        match seleccion:
            case 1:
                categoria = lista_categorias[0]
                break
            case 2:
                categoria= lista_categorias[1]
                break
            case 3:
                categoria = lista_categorias[2]
                break
            case 4:
                categoria = lista_categorias[3]
                break
            case 5:
                categoria = lista_categorias[4]
                break
            case 6:
                categoria = lista_categorias[5]
                break
            case 7:
                categoria = None
                break
        
        seleccion = int(input(mensaje_menu))
    if valor_actual == None and categoria == None:
        categoria = valor_actual

    return categoria

