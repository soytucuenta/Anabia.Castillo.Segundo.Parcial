from preguntas import *


def obtener_numero_respuesta_correcta(pregunta):
    """
    Returns the position (1-based index) of the correct answer option in a given question.
    Args:
        pregunta (dict): A dictionary representing a question. It must contain:
            - 'opciones': a list of possible answer options.
            - 'correcta': the correct answer option (should match one of the items in 'opciones').
    Returns:
        int: The 1-based index of the correct answer option in the 'opciones' list.
    Example:
        pregunta = {
            'opciones': ['A', 'B', 'C', 'D'],
            'correcta': 'C'
        }
        obtener_numero_respuesta_correcta(pregunta)  # Returns 3
    """
    

    contador = 1
    for opcion in pregunta['opciones']:
        if opcion == pregunta['correcta']:
            break
        contador += 1
    return contador


def mostrar_pregunta(pregunta_dict):
    """
    Muestra una pregunta y sus opciones por consola, solicita al usuario que elija una opción y devuelve la elección.
    Args:
        pregunta_dict (dict): Un diccionario que contiene la pregunta bajo la clave "pregunta" y una lista de opciones bajo la clave "opciones".
    Returns:
        int: El número de la opción elegida por el usuario (basado en 1).
    Raises:
        ValueError: Si la entrada del usuario no es un número entero válido.
        KeyError: Si el diccionario no contiene las claves esperadas ("pregunta" y "opciones").
    """

    print(pregunta_dict["pregunta"])
    opciones = pregunta_dict["opciones"]
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")
    eleccion = int(input("Elige el número de la opción: "))
    return eleccion

def solicitar_apuesta(dinero):
    """
    Solicita al usuario que ingrese una cantidad de dinero para apostar, validando que la apuesta sea mayor que 0 y no supere el dinero disponible.
    Parámetros:
        dinero (int): La cantidad de dinero disponible para apostar.
    Retorna:
        int: La cantidad apostada por el usuario, validada según las restricciones.
    """

    while True:
        apuesta = int(input(f"¿Cuánto quieres apostar? Tienes ${dinero}: "))
        if 0 < apuesta <= dinero:
            break
        else:
            print("Apuesta inválida. Debe ser mayor que 0 y no superar tu dinero disponible.")
    return apuesta

def procesar_respuesta(eleccion, pregunta_dict, dinero, apuesta):
    """
    Procesa la respuesta del usuario a una pregunta, actualizando el dinero según si la respuesta es correcta o incorrecta.
    Args:
        eleccion (int): Índice (1-based) de la opción elegida por el usuario.
        pregunta_dict (dict): Diccionario con la información de la pregunta, que debe contener las claves "opciones" (lista de opciones) y "correcta" (respuesta correcta).
        dinero (int): Cantidad actual de dinero del usuario antes de la apuesta.
        apuesta (int): Cantidad de dinero apostada en la pregunta actual.
    Returns:
        int: Cantidad actualizada de dinero después de procesar la respuesta.
    """
    opciones = pregunta_dict["opciones"]
    correcta = pregunta_dict["correcta"]
    dinero -= apuesta

    if opciones[eleccion - 1] == correcta:
        dinero += apuesta
        dinero += apuesta
        print(f"¡Correcto! Recuperas tu apuesta de ${apuesta}.")
    else:
        print(f"Incorrecto. La respuesta correcta era: {correcta}")
        print(f"Perdiste tu apuesta de ${apuesta}.")
    print(f"Te quedan ${dinero}.\n")
    return dinero

def gameplay():
    dinero = 500
    preguntas = nivel_1
    print("¡Bienvenido al juego del millon copiado de Susana Gimenez")
    print(f"Empiezas con ${dinero}.\n")

    for clave in preguntas:
        pregunta = preguntas[clave]
        print(f"Dinero disponible: ${dinero}")
        eleccion = mostrar_pregunta(pregunta)
        apuesta = solicitar_apuesta(dinero)
        dinero = procesar_respuesta(eleccion, pregunta, dinero, apuesta)
        if dinero <= 0:
            print("¡Te has quedado sin dinero! Fin del juego.")
            break

    print(f"Juego terminado. Terminaste con ${dinero}.")