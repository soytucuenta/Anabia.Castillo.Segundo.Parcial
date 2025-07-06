from prints import *
import random
from funciones_reutilizables import *

def minijuego()->bool:
    ganado = False
    print(bienvenida_minijuego)
    palabras = ["busca", "mundo", "volar", "buena", "gorra", "cielo", "viola", "cinco", "arbol"]
    palabra_random = lista_random(palabras)
    palabra_lista = []
    for i in range(len(palabra_random)):
        palabra_lista.append(palabra_random[i])

    matriz = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    ]

    nivel = 1

    palabra_armada = ["#", "#", "#", "#", "#"]

    while nivel <= 5:
        letra = input("Ingrese una letra: ")

        for i in range(len(palabra_lista)):
            if palabra_lista[i] == letra:
                coincide = 0

        nivel += 1

    return ganado
