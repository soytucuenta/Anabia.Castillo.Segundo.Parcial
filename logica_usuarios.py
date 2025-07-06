from manejo_archivos import *
from funciones_reutilizables import *

def registrar_usuario(dinero:int, dificultad:str, tiempo:int):
    """ Guardar datos de usuario que recién jugó.
    Args:
        dinero (int): Dinero que ganó el usuario.
        dificultad (str): Dificultad en la que jugó.
    """
    usuario = {}
    usuario["nombre"] = input("Ingrese el nombre de usuario: ")
    usuario["ganado"] = dinero
    usuario["dificultad"] = dificultad
    usuario["segundos"] = tiempo

    guardar_usuario_csv(usuario, "csv/usuarios.csv")

def leaderboard():
    """ Leaderboard general del juego Salve al millón.
    """
    print("\n### LEADERBOARD ###\n")

    # Carga usuarios
    usuarios = cargar_usuarios_csv("csv/usuarios.csv")

    # Ordernar lista
    ordernar_lista_diccionarios(usuarios, "ganado")

    # Filtra lista
    usuarios_facil = filtrar_lista_diccionarios(usuarios, "dificultad", "fácil")
    usuarios_media = filtrar_lista_diccionarios(usuarios, "dificultad", "media")
    usuarios_dificil = filtrar_lista_diccionarios(usuarios, "dificultad", "difícil")

    # Muestra lista
    print("---Difícil---")
    mostrar_lista_diccionarios(usuarios_dificil)
    print("---Medio---")
    mostrar_lista_diccionarios(usuarios_media)
    print("---Fácil---")
    mostrar_lista_diccionarios(usuarios_facil)