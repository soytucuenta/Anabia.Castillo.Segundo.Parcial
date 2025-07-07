import copy
from funciones_genericas import *
from prints import *
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


def copiar_usuario_por_nombre(nombre:str, lista_usuarios:list)-> dict:
    """
    Busca un usuario por su nombre en una lista de usuarios.
    Args:
        nombre (str): El nombre del usuario a buscar.
        lista_usuarios (list): Lista de diccionarios, cada uno representando un usuario con sus datos.
    Returns:
        dict: Un diccionario con los datos del usuario encontrado. Si no se encuentra, retorna un diccionario con valores por defecto.
    """
    datos_usuario = {"nombre": None, "ganancias": 0,"participaciones": 0, "dificultad": "media"}
    for usuario in lista_usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            datos_usuario =  copy.deepcopy(usuario)
    return datos_usuario
def buscar_nombre_en_lista_diccionarios(nombre:str, lista_usuarios:list)-> bool:
    """
    Busca si un nombre dado existe en una lista de diccionarios de usuarios.
    Args:
        nombre (str): El nombre a buscar.
        lista_usuarios (list): Lista de diccionarios, cada uno representando un usuario con al menos la clave 'nombre'.
    Returns:
        bool: True si se encuentra un usuario cuyo nombre coincide (ignorando mayúsculas/minúsculas) o si el valor de 'nombre' es None; False en caso contrario.
    """
    bandera = False
    for usuario in lista_usuarios:
        if usuario["nombre"].lower() == nombre.lower() or usuario['nombre'] == None:
            bandera = True
            break
    return bandera
def agregar_nuevo_usuario_consola(lista_usuarios:list, nombre:str,)-> dict:
    """
    Crea un nuevo usuario con el nombre proporcionado y lo agrega a la lista de usuarios.
    Args:
        lista_usuarios (list): Lista de diccionarios de usuarios.
        nombre (str): Nombre del nuevo usuario.
    Returns:
        dict: El diccionario del nuevo usuario creado.
    """
    nuevo_usuario = {"id": len(lista_usuarios) + 1, "nombre": nombre, "ganancias": 0, "participaciones": 0, "mejor racha": 0, "ranking": 0, "dificultad": "media"}
    lista_usuarios.append(nuevo_usuario)
    return nuevo_usuario
def seleccion_usuario_consola(lista_usuarios:list,mensaje:str = 'Ingrese usuario ', mensaje_usuario_encontrado:str = 'Usuario encontrado')-> dict:
    """
    Solicita al usuario que seleccione o ingrese un nombre de usuario por consola, luego recupera o crea los datos correspondientes.

    Args:
        lista_usuarios (list): Lista de diccionarios de usuarios para buscar.
        mensaje (str, opcional): Mensaje mostrado al usuario para el ingreso. Por defecto es 'Ingrese usuario '.
        mensaje_usuario_encontrado (str, opcional): Mensaje mostrado cuando se encuentra un usuario. Por defecto es 'Usuario encontrado'.

    Returns:
        dict: Diccionario con los datos del usuario, ya sea recién creado o copiado de uno existente.

    Notas:
        - Si el nombre ingresado existe en la lista, se crea un nuevo usuario mediante `agregar_nuevo_usuario_consola`.
        - Si el nombre no existe, se copian los datos del usuario existente mediante `copiar_usuario_por_nombre`.
        - Depende de las funciones externas: `buscar_nombre_en_lista_diccionarios`, `agregar_nuevo_usuario_consola` y `copiar_usuario_por_nombre`.
    """

    seleccion_de_usuario = input(mensaje)
    if buscar_nombre_en_lista_diccionarios(seleccion_de_usuario, lista_usuarios) == False:
        datos_usuario = agregar_nuevo_usuario_consola(lista_usuarios, seleccion_de_usuario)
    else:
        print(f"{mensaje_usuario_encontrado}: {seleccion_de_usuario}")
        datos_usuario = copiar_usuario_por_nombre(seleccion_de_usuario, lista_usuarios)
    return datos_usuario


