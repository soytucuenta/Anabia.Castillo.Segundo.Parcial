import copy
from funciones_genericas import *
def inicializar_usuario_actual(lista_dicc_usuarios)-> dict:

    datos_usuario = {"id": 0,"nombre": None, "ganancias": 0 , "participaciones": 0,"mejor racha": 0, "ranking": 0}
    datos_usuario["nombre"] = input("ingrese nombre de usuario: ")
    datos_usuario ["id"] = len(lista_dicc_usuarios) + 1 
    datos_usuario['ganancias'] = 0
    datos_usuario["participaciones"] = 0
    datos_usuario['mejor racha'] = 0
    datos_usuario['ranking'] = 0
    return datos_usuario

def finalizar_sesion(usuario_actual:dict, lista_dicc_usuarios:list):
    lista_dicc_usuarios.append(usuario_actual)
    return lista_dicc_usuarios
def ordenar_ranking(lista_dicc_usuarios:list):
    """
    Ordena la lista de usuarios por ganancias y asigna un ranking.
    Args:
        lista_dicc_usuarios (list): Lista de diccionarios de usuarios.
    Returns:
        list: Lista de usuarios ordenada por ganancias y con ranking asignado.
    """
    matriz_ranking = crear_matriz_ranking_ids(lista_dicc_usuarios)
    matriz_ranking = ordenar_matriz_burbujeo(matriz_ranking, 1)
    for i in range(len(matriz_ranking)):
        matriz_ranking[i][2] = i + 1
    lista_dicc_usuarios = cargar_matriz_en_diccionario(matriz_ranking, lista_dicc_usuarios)
    return lista_dicc_usuarios
def cargar_matriz_en_diccionario(matriz:list, lista_dicc_usuarios:list):
    lista_temporal = []
    for i in range(len(matriz)):
        fila = {}
        fila['id'] = matriz[i][0]
        fila['ganancias'] = matriz[i][1]
        fila['ranking'] = matriz[i][2]
        lista_temporal.append(fila)
    for i in range(len(lista_dicc_usuarios)):
        for j in range(len(lista_temporal)):
            if lista_dicc_usuarios[i]['id'] == lista_temporal[j]['id']:
                lista_dicc_usuarios[i]['ganancias'] = lista_temporal[j]['ganancias']
                lista_dicc_usuarios[i]['ranking'] = lista_temporal[j]['ranking']
    return lista_dicc_usuarios
        

def crear_matriz_ranking_ids(lista_dicc_usuarios:list):    
    matriz_ranking = []
    for i in range(len(lista_dicc_usuarios)):
        fila = []
        fila.append(lista_dicc_usuarios[i]['id'])
        fila.append(lista_dicc_usuarios[i]['ganancias'])
        fila.append(lista_dicc_usuarios[i]['ranking'])
        matriz_ranking.append(fila)
    return matriz_ranking

def leer_matriz_columna(matriz:list, columna:int)-> list:
    columna_leida = []
    for i in range(len(matriz)):
        columna_leida += (matriz[i][columna])
    return columna_leida

def ordenar_matriz_burbujeo(matriz:list, columna:int)-> list:
    for i in range(len(matriz)):
        for j in range(0,len(matriz) - i  - 1):
            if matriz[j][columna] < matriz[j + 1][columna]:
                aux = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = aux
    return matriz

def buscar_usuario(id_usuario, lista_usuarios):#deprecated

    for usuario in lista_usuarios:
        if usuario["id"] == id_usuario:
            return usuario
    return usuario

def copiar_usuario_por_nombre(nombre_a_buscar:str, usuarios:list)-> dict:#deprecated
    """
    Copia los datos de un usuario cuyo nombre coincida (ignorando mayúsculas/minúsculas) con el nombre proporcionado.
    Args:
        nombre_a_buscar (str): El nombre del usuario a buscar.
        usuarios (list): Lista de diccionarios, cada uno representando un usuario con sus datos.
    Returns:
        dict: Un diccionario con los datos del usuario encontrado. Si no se encuentra, retorna un diccionario con valores por defecto.
    """

    datos_usuario = {"nombre": None, "edad": 18, "profesion": None, "participaciones": 0, "ganancias": 0, "dificultad": 'media'}
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre_a_buscar.lower():
            datos_usuario= copy.deepcopy(usuario)  
    return datos_usuario

def seleccion_usuario_deprecated(lista_usuarios:list)-> dict:#deprecated
    """
    Permite al usuario seleccionar un usuario de una lista por nombre. Si el usuario no existe, solicita crear uno nuevo.
    Args:
        lista_usuarios (list): Una lista de diccionarios de usuarios.
    Returns:
        dict: El diccionario del usuario seleccionado o recién creado.
    """

    seleccion_de_usuario = input("ingrese usuario ")
    datos_usuario = copiar_usuario_por_nombre(seleccion_de_usuario,lista_usuarios)
    if datos_usuario["nombre"] == None:
        cargar_nuevo_usuario_consola(datos_usuario,seleccion_de_usuario)
        lista_usuarios.append(datos_usuario)
    return datos_usuario
    