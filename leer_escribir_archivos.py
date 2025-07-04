import re
from usuarios import *

def cargar_usuarios(path: str) ->list:
    """ Devuelve la lista de usuarios.
    Args:
        path (str): Ruta al archivo csv.
    Returns:
        list: Lista con usuarios como diccionarios.
    """
    usuarios = []
    with open (path, "r") as archivo:
        for linea in archivo:
            registro = linea.strip().split(",")
            if registro[0][0] != "i":
                lista = {}
                lista["id"] = int(registro[0])
                lista["nombre"] = registro[1]
                lista["edad"] = int(registro[2])
                lista["profesion"] = registro[3]
                lista["participaciones"] = int(registro[4])
                lista["ganancias"] = int(registro[5])
                lista["dificultad"] = registro[6]
                usuarios.append(lista)
    return usuarios

def cargar_preguntas(path: str) ->list:
    """ Devuelve la lista de preguntas.
    Args:
        path (str): Ruta al archivo csv.
    Returns:
        list: Lista con las preguntas como diccionarios.
    """
    preguntas = []
    with open (path, "r") as archivo:
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
    return preguntas


def escribir_csv_usuarios(lista_dic_usuarios, archivo):
    """
    Escribe una lista de diccionarios de usuarios en un archivo CSV.
    Cada diccionario de la lista debe contener las claves: 'nombre', 'edad', 'profesion', 'participaciones' y 'ganancias'.
    Los valores de cada usuario se escribirán en una línea del archivo, separados por comas.
    Args:
        lista_dic_usuarios (list): Lista de diccionarios con los datos de los usuarios.
        archivo (str): Ruta del archivo donde se escribirá el CSV.
    Returns:
        None
    """

    with open(archivo,'w',encoding ='utf8') as archivo:
        delimitador = ','
        for i in lista_dic_usuarios:
            mensaje = '{0},{1},{2},{3},{4},{5}'
            mensaje = mensaje.format(i['nombre'],
                                i['edad'],
                                i['profesion'],
                                i['participaciones'],
                                i['ganancias'],
                                i['dificultad'])
            archivo.write(f'{mensaje}\n')