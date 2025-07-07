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

def swap(lista:list, i:int, j:int):
    """ Swapea dos elementos de una lista entre sí.
    Args:
        lista (list): Lista a swapear.
        i (int): Posición del elemento uno.
        j (int): Posición del elemento dos.
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def ordernar_lista_diccionarios(lista:list, propiedad:str):
    """ Ordena elementos de una lista de diccionarios de acuerdo a una propiedad.
    Args:
        lista (list): Lista de diccionarios.
        propiedad (str): Propiedad por la que se ordena.
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][propiedad] < lista[j][propiedad]:
                swap(lista,i,j)  

def mostrar_lista_diccionarios(lista:list,):
    """ Muestra propiedades y valores de una lista de diccionarios.
    Args:
        lista (list): Lista.
    """
    for elemento in lista:
        for propiedad in elemento:
            print(f"{elemento[propiedad] :<13} {propiedad :>12}")
        print("")