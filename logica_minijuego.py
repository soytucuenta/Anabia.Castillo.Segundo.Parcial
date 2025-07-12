import random
from prints import *
from funciones_genericas import *
from colorama import Fore, Back, Style, init

def minijuego()->bool:
    init() 
    se_gano = False
    

    if se_gano == True:
        print("¡Enorabuena! Ganó el juego!\n")
    else:
        print("Lo siento ¡usted perdió!, más suerte la próxima.\n")

    return se_gano

# minijuego()