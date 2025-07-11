import random
from prints import *
from funciones_genericas import *
from colorama import Fore, Back, Style, init

def minijuego()->bool:
    init() 
    se_gano = False
    palabras = [
    "arena", "skate", "manga", "notas", "nivel", "bosque",
    "playa", "ollie", "otaku", "ritmo", "pixel", "flora",
    "marea", "grind", "senpu", "sonar", "vidas", "hojas",
    "coros", "rampa", "chibi", "guitar", "logro", "viento"
    ]
    
    palabra_adivinar = lista_random(palabras)
    nivel = 1
    coincidencias = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    palabras_intentadas = ["", "", "", "", "", ""]
    print(bienvenida_minijuego)
    
    while nivel <= 7:
        cadena = "\n"

        # mostrar matriz
        for i in range(len(coincidencias)):
            aciertos = 0
            if len(palabras_intentadas[i]) > 0:
                cadena += "["
                for j in range(len(palabras_intentadas[i])):
                    match coincidencias[i][j]: 
                        case 1:
                            cadena += (Fore.GREEN + palabras_intentadas[i][j] + Style.RESET_ALL)
                            aciertos += 1
                            if aciertos == 5:
                                se_gano = True
                        case 2:
                            cadena += (Fore.YELLOW + palabras_intentadas[i][j] + Style.RESET_ALL)
                        case 0:
                            cadena += (Fore.WHITE + palabras_intentadas[i][j] + Style.RESET_ALL)
                    if j != 4:
                        cadena += ", "
                cadena += "]"
            else:
                cadena += (Fore.WHITE + "[#, #, #, #, #]" + Style.RESET_ALL)
            cadena += "\n"
        print(cadena)
        
        # chequea si gano o que
        if se_gano or nivel == 7:
            break
        
        # ingresar palabras
        palabra_ingresada = input(f"Ingrese palabra: ")
        while len(palabra_ingresada) != 5:
            palabra_ingresada = input(f"Ingrese palabra de 5 caracteres: ")

        # calcular las coincidencias
        j = nivel - 1
        for i in range(len(coincidencias[j])):
            if palabra_ingresada[i] == palabra_adivinar[i]:
                    coincidencias[j][i] = 1
            else:
                for k in range(len(palabra_adivinar)):
                    if palabra_adivinar[k] == palabra_ingresada[i]:
                        coincidencias[j][i] = 2
                        break
            
        # agregar palabra a lista de palabras
        palabras_intentadas[j] = palabra_ingresada
        
        # aumentar nivel
        nivel += 1

    if se_gano == True:
        print("¡Enorabuena! Ganó el juego!\n")
    else:
        print("Lo siento ¡usted perdió!, más suerte la próxima.\n")

    return se_gano

# minijuego()