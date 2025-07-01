from prints import *
from preguntas import *
from logica_preguntas import *
from usuarios import *
# Trampa
cheats = True #pasa por parametro a gameplay y despues a la de mostrar pregunta y dice el numero de opcion de la correcta
#
info_usuario = seleccion_usuario(usuarios)
opcion_menu = int(input(menu))

while opcion_menu != 6:
    match opcion_menu:
        case 1:
            gameplay(1000000, 60, cheats)
        case 2:
            print(instrucciones)
        case 3:
            mostrar_datos_usuario(info_usuario, "\nMostrando informacion del usuario actual: \n")
        case 4:
            for usuario in usuarios:
                mostrar_datos_usuario(usuario, "\nMostrando informacion de todos los usuarios: \n")
        case 5:#configuraciones
            pass

    # volver a preguntar por el menu
    opcion_menu = int(input(menu))


