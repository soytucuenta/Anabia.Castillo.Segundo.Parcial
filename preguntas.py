from leer_escribir_archivos import *
import copy
import random

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
    with open (ubicacion, "r") as archivo:
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
    return preguntas


def obtener_preguntas_filtrando(preguntas:list, cantidad:int, dificultad:str=None, categoria:str=None):
    """
    Filtra preguntas por dificultad y categoria, y retorna una cantidad determinada aleatoria.

    :param preguntas: Lista de diccionarios con preguntas.
    :param cantidad: Numero de preguntas a devolver.
    :param dificultad: (opcional) Dificultad a filtrar ('facil', 'media', 'difcil').
    :param categoria: (opcional) Categoria a filtrar.
    :return: Lista de preguntas filtradas y seleccionadas aleatoriamente.
    """
    filtradas = []
    for pregunta in preguntas:
        cumple = True
        if dificultad is not None:
            if pregunta["dificultad"] != dificultad:
                cumple = False
        if categoria is not None:
            if pregunta["categoría"] != categoria:
                cumple = False
        if cumple:
            filtradas.append(pregunta)
    filtradas = mezclar_lista_diccionarios_cortando(filtradas, cantidad)
    return filtradas

def mezclar_lista_diccionarios_cortando(lista:list, cantidad:int):
    """
    Mezcla aleatoriamente una lista de diccionarios y devuelve una sublista con una cantidad específica de elementos.
    Args:
        lista (list): Lista de diccionarios a mezclar.
        cantidad (int): Número de elementos a devolver después de mezclar.
    Returns:
        list: Sublista mezclada de longitud 'cantidad' tomada de la lista original.
    Note:
        La función realiza una copia profunda de la lista original antes de mezclarla para evitar modificar la lista original.
    """
    
    mezclada = copy.deepcopy(lista)
    random.shuffle(mezclada)
    
    return mezclada[:cantidad]

#preguntas_leidas = cargar_preguntas("csv/preguntas.csv")
#preguntas = obtener_preguntas_filtrando(preguntas_leidas, 5, dificultad='media', categoria='ciencia')
#print(obtener_preguntas_filtrando(preguntas, 2, dificultad='media', categoria='ciencia'))

