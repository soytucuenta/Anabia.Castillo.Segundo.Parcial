from prints import *
from preguntas import *
from logica_preguntas import *
from usuarios import *

trampa = True #pasa por parametro a gameplay y despues a la de mostrar pregunta y dice el numero de opcion de la correcta
seleccion_de_usuario = input("ingrese usuario ")
datos_usuario = copiar_usuario_por_nombre(seleccion_de_usuario,usuarios)
print(datos_usuario)
opcion_menu = int(input(menu))

while opcion_menu != 3:
    match opcion_menu:
        case 1:
            gameplay(dinero=1000000,tiempo_limite=60)
        case 2:
            print(instrucciones)

    # volver a preguntar por el menu
    opcion_menu = int(input(menu))


