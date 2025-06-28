from preguntas import *

def mostrar_pregunta_y_opciones(pregunta_dict):
    """
    Muestra una pregunta y sus opciones por consola.
    Args:
        pregunta_dict (dict): Un diccionario que contiene la pregunta bajo la clave "pregunta" y una lista de opciones bajo la clave "opciones".
    """

    print(pregunta_dict["pregunta"])
    print("")
    opciones = pregunta_dict["opciones"]
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")

def solicitar_apuestas(dinero):
    """
    Solicita al usuario que ingrese una cantidad de dinero para apostar por cada opción, validando que las apuestas no supere el dinero disponible.
    Parámetros:
        dinero (int): La cantidad de dinero disponible para apostar.
    Retorna:
        (list): La cantidad/es apostada/s por el usuario, validada según las restricciones.
    """
    apuestas = [0, 0, 0, 0]
    apostando = 0
    print("")
    for i in range(len(apuestas)):
        apuestas[i] = int(input(f"¿Cuánto apuesta por la opción {i+1}?: "))
        while apostando + apuestas[i] > dinero:
            print(f"\nLo siento, no cuenta con dinero suficiente. Usted tiene ${dinero - apostando}.")
            apuestas[i] = int(input(f"¿Cuánto apuesta por la opción {i+1}?: "))
        apostando += apuestas[i]
    
    return apuestas

def procesar_respuesta(pregunta_dict, dinero, apuestas):
    """
    Procesa las respuestas del usuario, y devuelve el nuevo dinero del usuario.
    Args:
        dinero (int): Cantidad actual de dinero del usuario antes de la/s apuesta/s.
        apuestas (int): Cantidad de dinero apostado por opciones.
    Returns:
        int: Cantidad actualizada de dinero después de procesar las apuestas.
    """
    correcta = pregunta_dict["correcta"]
    dinero = apuestas[correcta]

    print(f"\n¡Y la respuesta correcta era {pregunta_dict["opciones"][correcta]}!")
    print(f"¡La opción número {correcta+1}!")
    print(f"¡Espero que haya apostado bien!")
    print("Su dinero es...")

    return dinero

def gameplay():
    dinero = 1000000
    nivel = 1
    
    print("\nComenzemos!\n ")
    print(f"Tomá! Este $1.000.000 es tuyo!\n")

    for i in  range(len(preguntas)):
        print(f'[Dinero disponible: ${dinero}]\n')
        print(f"[Pregunta {nivel:}]\n")
        print("(!) Recuerde que lo que no apuesta, lo pierde. (!)\n")
        
        # simple print de preguntas y opciones.
        mostrar_pregunta_y_opciones(preguntas[i])
        # pregunta por cada opción.
        apuestas = solicitar_apuestas(dinero)
        # la opción ganadora es el nuevo dinero.
        dinero = procesar_respuesta(preguntas[i], dinero, apuestas)
        # avanza de nivel
        nivel += 1
        
        if dinero <= 0:
            print("\n¡Te has quedado sin dinero! Fin del juego.")
            break

    print(f"\nJuego terminado. Usted terminó con ${dinero}.\n")