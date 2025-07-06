from manejo_archivos import *
from funciones_reutilizables import *

def registrar_usuario(dinero:int, dificultad:str):
    """ Guardar datos de usuario que recién jugó.
    Args:
        dinero (int): Dinero con el que se va.
        dificultad (str): Dificultad en la que jugó.
    """
    usuario = {}
    usuario["usuario"] = input("Ingrese el nombre usuario: ")
    usuario["ganancia"] = dinero
    usuario["dificultad"] = dificultad

    guardar_usuario_csv(usuario, "csv/usuarios.csv")

def leaderboard():
    """ Muestra la tabla de posiciones de todos los jugadores.
    Returns:
        _type_: Solo printea la tabla.
    """
    usuarios = cargar_usuarios_csv("csv/usuarios.csv")

    def ordernar_usuarios(lista):
        for i in range(len(lista) - 1):
            for j in range(i + 1, len(lista)):
                if lista[i]["ganancia"] < lista[j]["ganancia"]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        return lista

    usuarios_ordenados = ordernar_usuarios(usuarios)

    usuarios_facil = filtrar_lista_diccionarios(usuarios_ordenados, "dificultad", "fácil")
    usuarios_media = filtrar_lista_diccionarios(usuarios_ordenados, "dificultad", "media")
    usuarios_dificil = filtrar_lista_diccionarios(usuarios_ordenados, "dificultad", "difícil")

    print("\n### LEADERBOARD ###\n")
    print("---Difícil---")
    for usuario in usuarios_dificil:
        mostrar_datos_usuario(usuario)
    print("")

    print("---Media---")
    for usuario in usuarios_media:
        mostrar_datos_usuario(usuario)
    print("")

    print("---Fácil---")
    for usuario in usuarios_facil:
        mostrar_datos_usuario(usuario)