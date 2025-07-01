import copy

usuarios = [
    {"nombre": "Juan", "edad": 30, "profesion": "Ingeniero", "participaciones": 3, "ganancias": 1200},
    {"nombre": "Maria", "edad": 25, "profesion": "Disenadora", "participaciones": 2, "ganancias": 850},
    {"nombre": "Luis", "edad": 40, "profesion": "Contador", "participaciones": 5, "ganancias": 2100},
    {"nombre": "Ana", "edad": 35, "profesion": "Doctora", "participaciones": 6, "ganancias": 3400},
    {"nombre": "Pedro", "edad": 28, "profesion": "Abogado", "participaciones": 1, "ganancias": 300},
    {"nombre": "Lucia", "edad": 32, "profesion": "Arquitecta", "participaciones": 4, "ganancias": 1600},
    {"nombre": "Carlos", "edad": 45, "profesion": "Profesor", "participaciones": 3, "ganancias": 1300},
    {"nombre": "Sofia", "edad": 22, "profesion": "Estudiante", "participaciones": 1, "ganancias": 150},
    {"nombre": "Diego", "edad": 38, "profesion": "Chef", "participaciones": 2, "ganancias": 750}
]

usuario_default = {"nombre": "default","edad": 18, "profesion": "Desocupado", "dificultad": 7, "participaciones": 0, "ganancias":0}

def mostrar_datos_usuario(usuario:dict,mensaje:str):
    """
    Muestra los datos de un diccionario de usuario con un mensaje personalizado.
    Args:
        usuario (dict): Un diccionario que contiene los datos del usuario, donde las claves son los campos y los valores la información correspondiente.
        mensaje (str): Un mensaje para mostrar antes de listar los datos del usuario.
    Returns:
        None
    """

    print(mensaje)
    for dato in usuario:
        print(f"{dato}: {usuario[dato]}")

def buscar_usuario(nombre, lista_usuarios, bienvenida=False):
    usuario = "default"
    for usuario_busqueda in lista_usuarios:
        if usuario_busqueda["nombre"].lower() == nombre.lower():
            usuario = usuario_busqueda
            if bienvenida:
                print(f"Bienvenido {usuario['nombre']}")
    return usuario

def copiar_usuario_por_nombre(nombre_a_buscar:str, usuarios:list)-> dict:
    """
    Copia los datos de un usuario cuyo nombre coincida (ignorando mayúsculas/minúsculas) con el nombre proporcionado.
    Args:
        nombre_a_buscar (str): El nombre del usuario a buscar.
        usuarios (list): Lista de diccionarios, cada uno representando un usuario con sus datos.
    Returns:
        dict: Un diccionario con los datos del usuario encontrado. Si no se encuentra, retorna un diccionario con valores por defecto.
    """

    datos_usuario = {"nombre": None, "edad": 18, "profesion": None, "participaciones": 0, "ganancias": 0}
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre_a_buscar.lower():
            datos_usuario= copy.deepcopy(usuario)  
    return datos_usuario

def cargar_nuevo_usuario_consola(datos_usuario,seleccion_de_usuario):
    """
    Solicita al usuario que ingrese los datos de un nuevo usuario a través de la consola y los almacena en el diccionario proporcionado.
    Args:
        datos_usuario (dict): Diccionario donde se almacenarán los datos del nuevo usuario.
        seleccion_de_usuario (str): Nombre del usuario que se está registrando.
    El usuario debe ingresar su edad (debe ser mayor a 18 y menor o igual a 100) y su profesión. 
    Inicializa los campos 'participaciones' y 'ganancias' en 0.
    """

    print(f"{seleccion_de_usuario} es nuevo, ingrese datos a continuacion ")
    datos_usuario["nombre"] = seleccion_de_usuario
    datos_usuario["edad"] = int(input("ingrese la edad "))
    while datos_usuario["edad"] < 18 or datos_usuario["edad"] > 100:
        print("La edad debe ser mayor a 18")
        datos_usuario["edad"] = int(input("ingrese la edad "))
    datos_usuario["profesion"] = input("Ingrese su profesion ")
    datos_usuario["participaciones"] = 0
    datos_usuario["ganancias"] = 0
    
def seleccion_usuario(lista_usuarios:list)-> dict:
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
        usuarios.append(datos_usuario)
    return datos_usuario
    