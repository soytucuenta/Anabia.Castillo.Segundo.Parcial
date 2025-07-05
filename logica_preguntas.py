import time
import random
from prints import *
from manejo_archivos import *
from manejo_usuarios import *
from funciones_reutilizables import *

def mostrar_pregunta_y_opciones(pregunta_dict):
    """
    Muestra una pregunta y sus opciones por consola.
    Args:
        pregunta_dict (dict): Un diccionario que contiene la pregunta bajo la clave "pregunta" y una lista de opciones bajo la clave "opciones".
    """
    print(pregunta_dict["pregunta"])
    opciones = pregunta_dict["opciones"]
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")
    

def solicitar_apuestas(dinero:int, tiempo_limite:int)-> list:
    """
    Solicita al usuario que ingrese una cantidad de dinero para apostar por cada opción, validando que las apuestas no supere el dinero disponible.
    Args:
        dinero (int): La cantidad de dinero disponible para apostar.
    Returns:
        (list): La cantidad/es apostada/s por el usuario.
    """
    # flag_tiempo = False
    apuestas = [0, 0, 0, 0]
    apostando = 0
    print("")

    for i in range(len(apuestas)):
        # print(f"Tiene {tiempo_limite} segundos para contestar cada pregunta!.")
        # input("¿Está listo? Presione una tecla para continuar!\n")
        # tiempo_inicial = time.time() # inicio temporizador
        apuestas[i] = int(input(f"¿Cuánto apuesta por la opción {i+1}?: "))
        while apostando + apuestas[i] > dinero:
            print(f"\nLo siento, no cuenta con dinero suficiente. Usted tiene ${dinero - apostando}.")
            apuestas[i] = int(input(f"¿Cuánto apuesta por la opción {i+1}?: "))    
        apostando += apuestas[i]

        # tiempo_transcurrido = time.time() - tiempo_inicial
        
        # if tiempo_transcurrido > tiempo_limite:
        #     print("\nSe acabó el tiempo!.")    
        #     flag_tiempo = True
    
    return apuestas

def procesar_respuestas(pregunta_dict:dict, apuestas:list) -> int:
    """
    Procesa las respuestas del usuario, y devuelve el nuevo dinero.
    Args:
        dinero (int): Cantidad actual de dinero antes de la/s apuesta/s.
        apuestas (int): Cantidad de dinero apostado en cada opción.
    Returns:
        int: Cantidad actualizada del dinero del usuarios después de procesar la/s apuesta/s.
    """
    correcta = pregunta_dict["correcta"]
    dinero = apuestas[correcta]

    print("\n-------------------------------------------------")
    print(f"¡Y la respuesta correcta era {pregunta_dict["opciones"][correcta]}!")
    print(f"¡La opción número {correcta+1}!")
    print(f"¡Espero que haya apostado bien!")
    print("-------------------------------------------------\n")

    return dinero

def gameplay():
    """ Gameplay general del juego Salve al millón.
    """
    nivel = 1
    dinero = 1000000
    reglas = cargar_config_json("config.json")
    preguntas = cargar_preguntas_csv("csv/preguntas.csv")

    print(disclaimer)
    daltonico = int(input("\nEs usted daltonico?\n1. Si\n2. No\n\nSeleccione una opción: "))
    neurodivergente =  int(input("\nEs usted neurodivergente?\n1. Si\n2. No\n\nSeleccione una opción: "))
    dificultad =  input("\nElija un nivel de dificultad\n1. Fácil\n2. Medio\n3. Difícil\n\nSeleccione una opción: ")
    nivel_dificultad = reglas["dificultad"][dificultad]["nombre"]
    tiempo_dificultad = reglas["dificultad"][dificultad]["tiempo"]

    print("\nComenzemos!\n ")
    print(f"Tomá! Este $1.000.000 es tuyo!\n")
    print("(!) Recuerde que lo que no apuesta, lo pierde. (!)\n")

    while nivel <= 8:
        print(f'[Dinero disponible: ${dinero}]\n')
        print(f"[Pregunta {nivel:}]\n")
        print("Eliga una de las siguientes categorías:")
        print(f"1. Matemática{' ':>4}2. Ciencia{' ':>5}3. Deportes{' ':>9}")
        print(f"4. Arte{' ':>10}5. Historia{' ':>26}")
        categoria = input("Seleccione: ")
        nombre_categoria = reglas["categorías"][categoria]

        preg_filtradas = filtrar_lista_diccionarios(preguntas, "categoría", nombre_categoria)
        preg_filtradas = filtrar_lista_diccionarios(preg_filtradas, "dificultad", nivel_dificultad)
        pregunta_random = lista_random(preg_filtradas)
        print("")
        # simple print de preguntas y opciones.
        mostrar_pregunta_y_opciones(pregunta_random)
        # apuesta por cada opción y tiempo límite
        apuestas = solicitar_apuestas(dinero, tiempo_dificultad)
        # la opción ganadora es el nuevo dinero.
        dinero = procesar_respuestas(pregunta_random, apuestas)
        
        nivel += 1
        
        if dinero <= 0:
            print("¡Te has quedado sin dinero!")
            break

    if dinero == 1000000:
        print("¡Felicidades! ¡Ústed salvó al millón!\n")
        print("¡Se va con $1.000.000!\n")
    else:
        print(f"Juego terminado. Se va con ${dinero}.\n")

    # guardar_usuario(dinero, nivel_dificultad) 