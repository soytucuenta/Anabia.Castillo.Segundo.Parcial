from prints import *
from preguntas import *
from logica_preguntas import *

opcion_menu = int(input(menu))


while opcion_menu != 3:
    match opcion_menu:
        case 1:
            gameplay()
        case 2:
            print(instrucciones)

    # volver a preguntar por el menu
    opcion_menu = int(input(menu))


