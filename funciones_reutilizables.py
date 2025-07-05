import random

def filtrar_lista_diccionarios(lista:list, clave:str, valor:str)->list:
    lista_nueva = []
    for elemento in lista:
        if elemento[clave] == valor:
            lista_nueva.append(elemento)
    return lista_nueva

def lista_random(lista:list):
    indice_random = random.randint(0, len(lista) - 1)
    elemento_random = lista[indice_random]
    return elemento_random

def ordenamiento_ascendente(asced:bool, vector_a, vector_b):
    """ Ordena 2 listas paralelas de manera ascendente o descendente según primer parametro.
    
    Args:
        asced (bool): Detetermina si es ascendente o descendente.
        vector_a (list): Lista a.
        vector_b (list): Lista b.
    """
    for i in range(len(vector_a) - 1):
        for j in range(i + 1, len(vector_a)):
            match asced:
                case True:
                    if vector_a[i]["ganancia"] > vector_a[j]["ganancia"]:
                        swap(vector_a, i, j)
                        swap(vector_b, i, j)
                case False:
                    if vector_a[i]["ganancia"] < vector_a[j]["ganancia"]:
                        swap(vector_a, i, j)
                        swap(vector_b, i, j)

def swap(lista:list, i:int, j:int):
    """ Intercambia la posición de dos elementos en una lista.

    Args:
        lista (list): Lista.
        i (int): Posicion 1 a intercambiar.
        j (int): Posicion 2 a intercambiar.
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def mostrar_datos_usuario(usuario:dict):
    """
    Muestra los datos de un diccionario de usuario con un mensaje personalizado.
    Args:
        usuario (dict): Un diccionario que contiene los datos del usuario, donde las claves son los campos y los valores la información correspondiente.
        mensaje (str): Un mensaje para mostrar antes de listar los datos del usuario.
    Returns:
        None
    """
    print(f"{usuario["nombre"]} ${usuario["ganancia"]}")

    # for dato in usuario:
    #     print(f"{dato}: {usuario[dato]}")