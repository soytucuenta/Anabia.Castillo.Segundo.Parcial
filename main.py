from prints import *
from preguntas import *
from logica_preguntas import *
from usuarios import *
from leer_escribir_archivos import *
from funciones_genericas import *
from config import *
# meter tuplas o sets
# Trampa
cheats = True #pasa por parametro a gameplay y despues a la de mostrar pregunta y dice el numero de opcion de la correcta
#
#inicializacion de datos
todas_las_preguntas = cargar_preguntas() #carga las preguntas desde el CSV
usuarios = cargar_usuarios('csv/usuarios.csv') #carga los usuarios desde el CSV

config = cargar_configuracion(configuracion_default,'config.json') #carga la configuracion desde el JSON
#menu principal
opcion_menu = int(input(menu))
while opcion_menu != 6:
    match opcion_menu:
        case 1:
            jugar_consola(usuarios, config, todas_las_preguntas, cheats)
            ordenar_ranking(usuarios) 
        case 2:
            print(instrucciones)
        case 3:
            pass #stats aca
        case 4:#muestra el listado de usuarios
            mostrar_lista_diccionarios(usuarios, "Usuarios registrados:")
        case 5:#configuracion del juego
            configurar_juego(config, mensajes_config)
    # volver a preguntar por el menu
    opcion_menu = int(input(menu))
escribir_csv_usuarios(usuarios)
print("guardando puntajes... \n")
escribir_configuracion(config)
print("guardando configuracion... \n")
print("Gracias por jugar, hasta la proxima!")


