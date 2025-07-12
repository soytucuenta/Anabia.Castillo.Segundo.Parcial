import re
import json
from funciones_genericas import mostrar_diccionario_individual

def escribir_configuracion(configuracion:dict, archivo:str='config.json'):
    """
    Guarda un diccionario de configuración en un archivo JSON.
    Args:
        configuracion (dict): Diccionario que contiene la configuración a guardar.
        archivo (str, optional): Nombre del archivo donde se guardará la configuración. 
            Por defecto es 'config.json'.
    Raises:
        TypeError: Si 'configuracion' no es un diccionario.
        IOError: Si ocurre un error al escribir el archivo.
    """

    try:
        with open(archivo, 'w', encoding='utf8') as archivo:
            json.dump(configuracion, archivo, indent=4)
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Se creará uno nuevo.")

def cargar_configuracion(configuracion_default:dict,archivo:str='config.json') -> dict:
    """
    Carga la configuracion desde un archivo JSON.
    Si el archivo no existe, devuelve la configuracion por defecto.
    Args:
        configuracion_default (dict): Configuracion por defecto a usar si no se encuentra el archivo.
        archivo (str): Ruta al archivo JSON que contiene la configuracion.
    Returns:
        dict: La configuracion cargada desde el archivo o la configuracion por defecto.
    """
    bandera = False
    configuracion = {}
    try:
        with open(archivo, 'r', encoding='utf8') as archivo:
            configuracion =  json.load(archivo)
    except FileNotFoundError:
        configuracion = configuracion_default
        bandera = True
    if len(configuracion) != len(configuracion_default):#ver que no falten claves
        configuracion = configuracion_default
        bandera = True
    if bandera:
        print(f"Archivo de configuracion no encontrado o incompleto, se usara la configuracion por defecto: {configuracion_default}")
    return configuracion

def escribir_csv_usuarios(lista_dic_usuarios, archivo='csv/usuarios.csv'):
    """
    Escribe una lista de diccionarios de usuarios en un archivo CSV.

    Cada diccionario en la lista debe contener las siguientes claves:
        - 'id': Identificador único del usuario
        - 'nombre': Nombre del usuario
        - 'ganancias': Ganancias del usuario
        - 'participaciones': Cantidad de participaciones
        - 'mejor racha': Mejor racha del usuario
        - 'ranking': Ranking del usuario

    Args:
        lista_dic_usuarios (list): Lista de diccionarios, cada uno representando un usuario.
        archivo (str, opcional): Ruta al archivo CSV donde escribir. Por defecto es 'csv/usuarios.csv'.

    La función sobrescribe el archivo si ya existe.
    """
    try:
        with open(archivo,'w',encoding ='utf8') as archivo:
            delimitador = ','
            archivo.write('id,nombre,ganancias,participaciones,mejor_racha,ranking\n')
            for i in lista_dic_usuarios:
                mensaje = '{0},{1},{2},{3},{4},{5},{6}'
                mensaje = mensaje.format(i['id'] ,
                                    i['nombre'],
                                    i['ganancias'],
                                    i['participaciones'],
                                    i['mejor racha'],
                                    i['ranking'],
                                    i['dificultad'])
                archivo.write(f'{mensaje}\n')
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe. Se creará uno nuevo.")

def cargar_usuarios(path:str="csv/usuarios.csv") ->list:
    """
    Carga una lista de usuarios desde un archivo de texto.
    El archivo debe tener líneas con los siguientes campos separados por comas:
    nombre,edad,profesion,participaciones,ganancias
    Args:
        path (str): Ruta al archivo de texto que contiene los datos de los usuarios.
    Returns:
        list: Una lista de diccionarios, cada uno representando un usuario con las claves:
            - 'nombre' (str)
            - 'edad' (str)
            - 'profesion' (str)
            - 'participaciones' (int)
            - 'ganancias' (int)
    """

    lista =[]
    try:
        with open(path, 'r', encoding='UTF8') as archivo:
            archivo.readline()
            for linea in archivo:
                lectura = re.split(',|\n', linea)
                dato = {}
                dato['id'] = int(lectura[0])
                dato['nombre'] = lectura[1]
                dato['ganancias'] = int(lectura[2])
                dato['participaciones'] = int(lectura[3])
                dato['mejor racha'] = int(lectura[4])
                dato['ranking'] = int(lectura[5])
                dato['dificultad'] = lectura[6]
                lista.append(dato)
    except FileNotFoundError:
        print(f"El archivo {path} no existe.")
    return lista


def cargar_preguntas(ubicacion:str="csv/preguntas.csv")-> list:
    """
    Carga preguntas desde un archivo CSV y las almacena en una lista de diccionarios.

    Cada pregunta se representa como un diccionario con las siguientes claves:
    - 'id': Identificador de la pregunta.
    - 'pregunta': Texto de la pregunta.
    - 'opciones': Lista de opciones posibles.
    - 'correcta': Índice de la opción correcta.
    - 'dificultad': Dificultad de la pregunta ('facil', 'media', 'dificil').
    - 'categoría': Categoría a la que pertenece la pregunta.

    :return: Lista de diccionarios con las preguntas cargadas.
    """
    preguntas = []
    try:
        with open (ubicacion, "r", encoding='utf-8') as archivo:
            archivo.readline()
            for linea in archivo:
                registro = linea.strip().split(",")
                if registro[0][0] != "i":
                    lista = {}
                    lista["id"] = int(registro[0])
                    lista["pregunta"] = registro[1]
                    lista["opciones"] = registro[2].split("|")
                    lista["correcta"] = int(registro[3])
                    lista["dificultad"] = registro[4]
                    lista["categoría"] = registro[5]
                    preguntas.append(lista)
    except FileNotFoundError:
        print(f"El archivo {ubicacion} no existe.")
    return preguntas
