
from usuarios import ordenar_ranking
from funciones_genericas import *
from prints import *

#from funciones_pygame import  mostrar_texto

def burbujear_top(lista_dicc_usuarios:list, cantidad:int = 10,clave:str = 'ranking') -> list:
    """
        Ordena una lista de diccionarios de usuarios utilizando el método de burbuja según una clave especificada y retorna los N primeros elementos.
        Args:
            lista_dicc_usuarios (list): Lista de diccionarios, cada uno representando un usuario con al menos la clave especificada.
            cantidad (int, opcional): Cantidad de elementos superiores a retornar. Por defecto es 10.
            clave (str, opcional): Clave en los diccionarios por la cual ordenar. Por defecto es 'ranking'.
        Returns:
            list: Una lista con los N primeros diccionarios de usuarios ordenados en orden ascendente según la clave especificada.
        """

    lista_copiada = copy.deepcopy(lista_dicc_usuarios)
    lista_copiada = ordenar_ranking(lista_copiada)
    for i in range(len(lista_copiada)):
        for j in range(0, len(lista_copiada) - i - 1):
            if lista_copiada[j][clave] > lista_copiada[j + 1][clave]:
                aux = lista_copiada[j]
                lista_copiada[j] = lista_copiada[j + 1]
                lista_copiada[j + 1] = aux
    return lista_copiada[:cantidad]
def usuarios_arriba_del_promedio(lista_dicc_usuarios:list, clave:str = 'ganancias') -> list:
    """
        Devuelve una lista de diccionarios de usuarios cuyo valor para la clave especificada está por encima del promedio.
        Args:
            lista_dicc_usuarios (list): Lista de diccionarios, cada uno representando un usuario con al menos la clave especificada.
            clave (str, opcional): Clave en los diccionarios de usuario a comparar. Por defecto es 'ganancias'.
        Returns:
            list: Lista de diccionarios de usuarios donde el valor para la clave especificada es mayor al promedio de esa clave entre todos los usuarios.
        Raises:
            KeyError: Si algún diccionario de usuario no contiene la clave especificada.
        """

    lista_ganancias = []
    for usuario in lista_dicc_usuarios:
        lista_ganancias.append(usuario[clave])
    promedio = promediar_lista(lista_ganancias)
    lista_arriba_promedio = []
    for usuario in lista_dicc_usuarios:
        if usuario[clave] > promedio:
            lista_arriba_promedio.append(usuario)
    return lista_arriba_promedio
def mostrar_usuarios_por_clave(lista_usuarios:list, clave:str = 'ganancias'):
    """
    Muestra información de usuarios basada en una clave específica.
    Args:
        lista_usuarios (list): Lista de diccionarios, donde cada diccionario representa un usuario.
        clave (str, optional): Clave del diccionario cuyo valor se desea mostrar junto al nombre del usuario. 
            Por defecto es 'ganancias'.
    Returns:
        None: Esta función imprime la información en consola y no retorna ningún valor.
    """

    for usuario in lista_usuarios:
        print(f"Nombre: {usuario['nombre']}, {clave}: {usuario[clave]}")
def mostrar_usuarios_top(lista_dicc_usuarios:list, cantidad:int = 10, clave:str = 'ranking',juego_grafico:bool = False,
                        superficie = None,posicion = (0,0), fuente = None,color = None, color_fondo = None, espaciado = 5, centrado = False):
    """
    Muestra los usuarios con el mejor ranking.
    Args:
        lista_dicc_usuarios (list): Lista de diccionarios de usuarios.
        cantidad (int): Cantidad de usuarios a mostrar. Por defecto es 10.
    """
    lista_top = burbujear_top(lista_dicc_usuarios, cantidad, clave)
    if juego_grafico == False:
        print(f"Top {cantidad} usuarios:")
        for usuario in lista_top:
            print(f"Nombre: {usuario['nombre']}, Ganancias: {usuario['ganancias']}, Mejor racha: {usuario['mejor racha']}, Ranking: {usuario['ranking']}")
    # else:
    #     lista_dicc = burbujear_top(lista_dicc_usuarios, cantidad, clave)
    #     lineas = formatear_usuarios_string(lista_dicc)
    #     y_actual = posicion[1]
    #     for linea in lineas:
    #         linea = mostrar_texto(superficie,(posicion[0], y_actual), linea, fuente, color, color_fondo,
    #                         centrado=centrado)
    #     y_actual += linea.height + espaciado

def seleccion_stats(lista_usuarios,mensaje:str):
    seleccion = int(input(mensaje))
    while seleccion != 4:
        match seleccion:
            case 1:
                mostrar_usuarios_top(lista_usuarios,10, 'ranking')
            case 2:            
                mostrar_usuarios_por_clave(usuarios_arriba_del_promedio(lista_usuarios))
            case 3:
                mostrar_usuarios_top(lista_usuarios,10, 'participaciones')
            case _:
                print("Selección no válida. Intente nuevamente.")
        seleccion = int(input(mensaje))




'''------------------------pygame------------------------'''

