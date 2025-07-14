import copy
from funciones_genericas import *
from prints import *
from config import seleccion_dificultad

def inicializar_usuario_actual(lista_dicc_usuarios)-> dict:
    """
    Inicializa un nuevo usuario con datos predeterminados y solicita el nombre por consola.
    Args:
        lista_dicc_usuarios (list): Lista de diccionarios que representan los usuarios existentes.
    Returns:
        dict: Diccionario con los datos del nuevo usuario, incluyendo id, nombre, ganancias, participaciones, mejor racha y ranking.
    """

    datos_usuario = {"id": 0,"nombre": None, "ganancias": 0 , "participaciones": 0,"mejor racha": 0, "ranking": 0}
    datos_usuario["nombre"] = input("ingrese nombre de usuario: ")
    datos_usuario ["id"] = len(lista_dicc_usuarios) + 1 
    datos_usuario['ganancias'] = 0
    datos_usuario["participaciones"] = 0
    datos_usuario['mejor racha'] = 0
    datos_usuario['ranking'] = 0
    return datos_usuario

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
    """
    Actualiza una lista de diccionarios de usuarios con los valores de 'ganancias' y 'ranking' provenientes de una matriz dada.
    Args:
        matriz (list): Una lista de listas, donde cada lista interna contiene datos de usuario en el orden [id, ganancias, ranking].
        lista_dicc_usuarios (list): Una lista de diccionarios, cada uno representando un usuario con al menos la clave 'id'.
    Returns:
        list: La lista actualizada de diccionarios de usuarios con los campos 'ganancias' y 'ranking' establecidos según la matriz.
    Nota:
        Solo se actualizarán los usuarios cuyo 'id' coincida entre la matriz y la lista de diccionarios de usuarios.
    """

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
    """
    Genera una matriz que contiene los valores de 'id', 'ganancias' y 'ranking' para cada usuario en la lista de entrada.
    Args:
        lista_dicc_usuarios (list): Una lista de diccionarios, donde cada diccionario representa un usuario y contiene las claves 'id', 'ganancias' y 'ranking'.
    Returns:
        list: Una lista de listas (matriz), donde cada lista interna contiene el 'id', 'ganancias' y 'ranking' de un usuario.
    """

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
    """
    Ordena una matriz (lista de listas) en orden descendente según los valores de una columna especificada utilizando el algoritmo de burbujeo.
    Args:
        matriz (list): La matriz a ordenar, donde cada elemento es una lista que representa una fila.
        columna (int): El índice de la columna por la cual se ordenará.
    Returns:
        list: La matriz ordenada en orden descendente según la columna especificada.
    """

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
        if usuario["nombre"].lower() == nombre.lower(): #or usuario['nombre'] != None:
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
        print(f"Usuario nuevo: {seleccion_de_usuario}")
    else:
        print(f"{mensaje_usuario_encontrado}: {seleccion_de_usuario}")
        datos_usuario = copiar_usuario_por_nombre(seleccion_de_usuario, lista_usuarios)
    return datos_usuario

def agregar_nuevo_usuario_main(lista_usuarios:list)-> dict:
    """
    Crea un nuevo usuario con el nombre proporcionado y lo agrega a la lista de usuarios.
    Args:
        lista_usuarios (list): Lista de diccionarios de usuarios.
        nombre (str): Nombre del nuevo usuario.
    Returns:
        dict: El diccionario del nuevo usuario creado.
    """
    seleccion_nombre = input(f"Ingrese nombre de usuario: ")
    if buscar_nombre_en_lista_diccionarios(seleccion_nombre, lista_usuarios):
        print(f"El nombre {seleccion_nombre} ya existe, ingrese desde inicio de partida")
        nuevo_usuario = {}
    else:
        print(f"Creando nuevo usuario: {seleccion_nombre}")
        dificultad_default = "media"
        dificultad = seleccion_dificultad(mensaje_dificultad, dificultad_default)
        if dificultad == None:
            dificultad = "media"
        nuevo_usuario = {"id": len(lista_usuarios) + 1, "nombre": seleccion_nombre, "ganancias": 0, "participaciones": 0, "mejor racha": 0, "ranking": 0, "dificultad": dificultad}
    return nuevo_usuario

def formatear_usuarios_string(lista_usuarios:list) -> list:
    """
    Formatea una lista de diccionarios de usuarios en una lista de cadenas formateadas.
    Cada diccionario de usuario debe contener las claves: 'nombre', 'ganancias', 'mejor racha' y 'ranking'.
    La función retorna una lista de cadenas, cada una representando un usuario con sus detalles formateados.
    Args:
        lista_usuarios (list): Una lista de diccionarios, cada uno representando un usuario.
    Returns:
        list: Una lista de cadenas formateadas con la información de los usuarios.
    """

    strings_formateados = []
    for usuario in lista_usuarios:
        string_formateado = f"Nombre: {usuario['nombre']}, Ganancias: {usuario['ganancias']}, Mejor racha: {usuario['mejor racha']}, Ranking: {usuario['ranking']}"
        strings_formateados.append(string_formateado)
    return strings_formateados




