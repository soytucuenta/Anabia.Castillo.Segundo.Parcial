from prints import *
from logica_preguntas import *
from logica_usuarios import *

opcion_menu = int(input(menu))

while opcion_menu != 4:
    match opcion_menu:
        case 1:
            gameplay()
        case 2:
            print(instrucciones)
        case 3:
            leaderboard()
            
    # volver a preguntar por el menu
    opcion_menu = int(input(menu))

