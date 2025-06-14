from prints import *
from preguntas import *

opcion_menu = int(input(menu))

while opcion_menu != 3:
    match opcion_menu:
        case 1:
            pass
        case 2:
            print(instrucciones)

    # volver a preguntar por el menu
    opcion_menu = int(input(menu))