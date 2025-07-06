import random

def filtrar_lista_diccionarios(lista:list, clave:str, valor:str)->list:
    """ Filtra elementos de una lista, por una clave/valor especifico.
        Devuelve una lista con los elementos filtrados.
    Args:
        lista (list): Lista.
        clave (str): Clave.
        valor (str): Valor.
    Returns:
        list: Lista con elementos filtrados.
    """
    lista_nueva = []
    for elemento in lista:
        if elemento[clave] == valor:
            lista_nueva.append(elemento)
    return lista_nueva

def lista_random(lista:list):
    """ Devuelve un elemento random de una lista.
    Args:
        lista (list): Lista 
    Returns:
        (_type_): Elemento random, del tipo que sea.
    """
    indice_random = random.randint(0, len(lista) - 1)
    elemento_random = lista[indice_random]

    return elemento_random

def mostrar_datos_usuario(usuario:dict):
    """
    Muestra los datos de un diccionario de usuario.
    Args:
        usuario (dict): Un diccionario que contiene los datos del usuario a mostrar.
    Returns: 
    """
    print(f"{usuario["usuario"]} ${usuario["ganancia"]}")
