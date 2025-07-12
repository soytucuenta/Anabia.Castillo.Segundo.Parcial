import copy
import random

def incrementar_clave_especifica(diccionario_usuario:dict, clave:str):
    diccionario_usuario[clave] += 1

def sumar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] += valor

def restar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] -= valor

def multiplicar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] *= valor

def mostrar_lista_diccionarios(lista:list, mensaje):
    for diccionario in lista:
        mostrar_diccionario_individual(diccionario, mensaje)

def dividir_en_clave(diccionario:dict, clave:str, valor:int):
    resultado = None
    if valor != 0:
        resultado =diccionario[clave] / valor
    return resultado

def reemplazar_en_clave(diccionario:dict, clave:str, valor):
    diccionario[clave] = valor

def sincronizar_diccionario(diccionario:dict, lista_usuarios:list, clave_busqueda:str):
    """
    Sincroniza un diccionario de usuario con una lista de usuarios, actualizando el usuario en la lista si existe.
    Args:
        diccionario (dict): Diccionario del usuario a sincronizar.
        lista_usuarios (list): Lista de usuarios donde se buscará el usuario a actualizar.
        clave_busqueda (str): Clave del diccionario que se usará para buscar al usuario en la lista.
    """
    for i in range(len(lista_usuarios)):
        if lista_usuarios[i][clave_busqueda] == diccionario[clave_busqueda]:
            lista_usuarios[i] = copy.deepcopy(diccionario)
            return
    lista_usuarios.append(copy.deepcopy(diccionario))

def buscar_maximo_lista(lista:list):
    """
    Busca y retorna el valor máximo de una lista de números.
    Args:
        lista (list): Lista de números a evaluar.
    Returns:
        int or float: El valor máximo encontrado en la lista. Si la lista está vacía, retorna 0.
    """

    if len(lista) == 0:
        maximo = 0
    else:
        maximo = lista[0]
        for i in range(len(lista)):
            if lista[i] > maximo:
                maximo = lista[i]
    return maximo

def buscar_maximo(maximo_anterior:int, nuevo_valor:int):
    """
    Compara un valor nuevo con un máximo anterior y devuelve el mayor de los dos.
    Args:
        maximo_anterior (int): El valor máximo anterior.
        nuevo_valor (int): El nuevo valor a comparar.
    Returns:
        int: El mayor entre el máximo anterior y el nuevo valor.
    """
    salida = maximo_anterior
    if nuevo_valor > maximo_anterior:
        salida = nuevo_valor
    return salida

def promediar_lista(lista:list):
    """
    Calcula el promedio (media) de los valores numéricos en una lista.
    Args:
        lista (list): Una lista de valores numéricos (int o float).
    Returns:
        float: El valor promedio de los elementos en la lista.
    Raises:
        ZeroDivisionError: Si la lista de entrada está vacía.
        TypeError: Si la lista contiene elementos no numéricos.
    """

    acumulador = 0
    for i in range(len(lista)):
        acumulador += lista[i]
    promedio = acumulador / len(lista)
    return promedio

def mostrar_diccionario_individual(diccionario:dict,mensaje=None):
    """
    Muestra los elementos de un diccionario en formato clave: valor, precedidos opcionalmente por un mensaje.
    Args:
        diccionario (dict): El diccionario cuyos elementos se desean mostrar.
        mensaje (str, optional): Un mensaje opcional que se imprime antes de mostrar el diccionario. Por defecto es None.
    Returns:
        None
    """

    if type(mensaje) == str:
        print(mensaje)
    for dato in diccionario:
        print(f"{dato}: {diccionario[dato]}")

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