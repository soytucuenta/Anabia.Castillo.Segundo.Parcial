
from usuarios import ordenar_ranking
from funciones_genericas import *
from prints import *

def mostrar_por_ranking(lista_dicc_usuarios:list):
    """
    Muestra la lista de usuarios ordenada por ranking.
    Args:
        lista_dicc_usuarios (list): Lista de diccionarios de usuarios.
    """
    lista_dicc_usuarios = ordenar_ranking(lista_dicc_usuarios)
    print("Usuarios ordenados por ranking:")
    for usuario in lista_dicc_usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Ganancias: {usuario['ganancias']}, Participaciones: {usuario['participaciones']}, Mejor racha: {usuario['mejor racha']}, Ranking: {usuario['ranking']}")



def burbujear_top(lista_dicc_usuarios:list, cantidad:int = 10,clave:str = 'ranking') -> list:
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
    lista_ganancias = []
    for usuario in lista_dicc_usuarios:
        lista_ganancias.append(usuario[clave])
    promedio = promediar_lista(lista_ganancias)
    lista_arriba_promedio = []
    for usuario in lista_dicc_usuarios:
        if usuario[clave] > promedio:
            lista_arriba_promedio.append(usuario)
    return lista_arriba_promedio
def usuarios_mas_participaciones(lista_dicc_usuarios:list, cantidad:int = 10) -> list:
def mostrar_usuarios_por_clave(lista_usuarios:list, clave:str = 'ganancias'):

    for usuario in lista_usuarios:
        print(f"Nombre: {usuario['nombre']}, {clave}: {usuario[clave]}")
def mostrar_usuarios_top(lista_dicc_usuarios:list, cantidad:int = 10, clave:str = 'ranking'):
    """
    Muestra los usuarios con el mejor ranking.
    Args:
        lista_dicc_usuarios (list): Lista de diccionarios de usuarios.
        cantidad (int): Cantidad de usuarios a mostrar. Por defecto es 10.
    """
    lista_top = burbujear_top(lista_dicc_usuarios, cantidad, clave)
    print(f"Top {cantidad} usuarios:")
    for usuario in lista_top:
        print(f"Nombre: {usuario['nombre']}, Ganancias: {usuario['ganancias']}, Mejor racha: {usuario['mejor racha']}, Ranking: {usuario['ranking']}")
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
"""---------TESTING---------"""
#mostrar_por_ranking(lista_dicc_usuarios)
#mostrar_usuarios_top(lista_dicc_usuarios,10,'ranking')
#mostrar_usuarios_por_clave(usuarios_arriba_del_promedio(lista_dicc_usuarios), 'ganancias')

