from prints import *
import random
from funciones_reutilizables import *
from colorama import Fore, Back, Style, init

def minijuego()->bool:
    init() 
    se_gano = False
    palabras = ["playa", "amigo", "bueno", "mejor" "mundo", "libre", "volar", "libro", "dulce", "gorra", "cielo", "fuego", "cinco", "arbol", "verde", "lapiz"]
    palabra_random = lista_random(palabras)
    intentos = 1
    filas = 6
    resultado_intento = [0, 0, 0, 0, 0]
    resultados_intentos = []
    palabras_intentadas = ["", "", "", "", "", ""]
    print(bienvenida_minijuego)
    
    while intentos <= 6:
        # mostrar matriz
        cadena = "\n"
        aciertos = 0
        for i in range(filas):
            if len(palabras_intentadas[i]) > 0:
                cadena += "["
                for j in range(len(palabras_intentadas[i])):
                    match resultados_intentos[i][j]: 
                        case 1:
                            cadena += (Fore.GREEN + palabras_intentadas[i][j] + Style.RESET_ALL)
                            aciertos += 1
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
        
        # calcular si ganó
        if aciertos == 5:
            print("¡Enorabuena! Ganó el juego!\n")
            gano = True
            break
            
        # ingresar palabras
        palabra_intento = input(f"Ingrese palabra: ")
        while len(palabra_intento) != 5:
            palabra_intento = input(f"Ingrese palabra de 5 caracteres: ")

        # buscar coincidencias
        resultado_intento = [0, 0, 0, 0, 0]
        for i in range(len(palabra_intento)):
            if palabra_intento[i] == palabra_random[i]:
                    resultado_intento[i] = 1
            else:
                for j in range(len(palabra_random)):
                    if palabra_intento[i] == palabra_random[j]:
                        resultado_intento[i] = 2
                        break

        # agregar palabra y resultados a listas
        palabras_intentadas[intentos - 1] = palabra_intento
        resultados_intentos.append(resultado_intento)
        
        # aumentar intentos
        intentos += 1

    if intentos > 6:
        print("\nLo siento, más suerte la próxima.\n")

    return se_gano

minijuego()