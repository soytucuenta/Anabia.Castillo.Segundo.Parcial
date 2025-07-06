import copy
def inicializar_usuarios(lista_dicc_usuarios)-> dict:

    datos_usuario = {"id": 0,"nombre": None, "ganancias": 0 , "participaciones": 0,"mejor racha": 0, "ranking": 0}
    datos_usuario["nombre"] = input("ingrese nombre de usuario: ")
    datos_usuario ["id"] = len(lista_dicc_usuarios) + 1 
    datos_usuario['ganancias'] = 0
    datos_usuario["participaciones"] = 0
    datos_usuario['mejor racha'] = 0
    datos_usuario['ranking'] = 0
    lista_dicc_usuarios.append(datos_usuario)
    return datos_usuario



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
    