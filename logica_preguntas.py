from preguntas import *
import time
def mostrar_pregunta_y_opciones(pregunta_dict,tiempo_limite):
    """
    Muestra una pregunta y sus opciones por consola.
    Args:
        pregunta_dict (dict): Un diccionario que contiene la pregunta bajo la clave "pregunta" y una lista de opciones bajo la clave "opciones".
    """
    print(f"Llena cada pregunta en menos de {tiempo_limite} o perdes todo")
    input("Ingrese cualquier cosa para continuar: ")
    print(pregunta_dict["pregunta"])
    print("")
    opciones = pregunta_dict["opciones"]
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")

def solicitar_apuestas(dinero,tiempo_limite):
    """
    Solicita al usuario que ingrese una cantidad de dinero para apostar por cada opción, validando que las apuestas no supere el dinero disponible.
    Parámetros:
        dinero (int): La cantidad de dinero disponible para apostar.
    Retorna:
        (list): La cantidad/es apostada/s por el usuario.
    """
    flag_tiempo = False
    apuestas = [0, 0, 0, 0]
    apostando = 0
    print("")
    for i in range(len(apuestas)):
        # NOTA IMPORTANTE SOBRE TIME E INPUTIMEOUT, no se si estaria permitido importar inputimeout 
        # Limita cada input a un tiempo determinado algo asi:
        # from inputimeout import inputimeout, TimeoutOccurred
        # respuesta = inputimeout(prompt='Escribe algo en 5 segundos: ', timeout=5)
        # el problema que veo es que es para usar excepciones y no le va a gustar a german
        # como parche temporal hice esto con el time que si se pasa del limite perdes el juego entero
        tiempo_inicial = time.time() # inicio temporizador
        apuestas[i] = int(input(f"¿Cuánto apuesta por la opción {i+1}?: "))
        while apostando + apuestas[i] > dinero:
            print(f"\nLo siento, no cuenta con dinero suficiente. Usted tiene ${dinero - apostando}.")
            apuestas[i] = int(input(f"¿Cuánto apuesta por la opción {i+1}?: "))    
        apostando += apuestas[i]
        #tiempo
        tiempo_final = time.time()
        tiempo_transcurrido = tiempo_final - tiempo_inicial
        if tiempo_transcurrido > tiempo_limite:
            print("\n Excediste el tiempo limite para responder, perdes todo ")    
            flag_tiempo = True
        #tiempo
    if flag_tiempo:
        apuestas = [0, 0, 0, 0]
    return apuestas

def procesar_respuesta(pregunta_dict, dinero, apuestas):
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

    print(f"\n¡Y la respuesta correcta era {pregunta_dict["opciones"][correcta]}!")
    print(f"¡La opción número {correcta+1}!")
    print(f"¡Espero que haya apostado bien!")
    print("Su dinero es...")

    return dinero

def gameplay(dinero,tiempo_limite):
    """
    Gameplay general del juego Salve al millón.
    """
    
    nivel = 1
    
    print("\nComenzemos!\n ")
    print(f"Tomá! Este $1.000.000 es tuyo!\n")

    for i in  range(len(preguntas)):
        print(f'[Dinero disponible: ${dinero}]\n')
        print(f"[Pregunta {nivel:}]\n")
        print("(!) Recuerde que lo que no apuesta, lo pierde. (!)\n")
        
        # simple print de preguntas y opciones.
        mostrar_pregunta_y_opciones(preguntas[i],tiempo_limite,nivel)
        # pregunta por cada opción.
        apuestas = solicitar_apuestas(dinero,tiempo_limite)
        # la opción ganadora es el nuevo dinero.
        dinero = procesar_respuesta(preguntas[i], dinero, apuestas)
        # avanza de nivel
        nivel += 1
        
        if dinero <= 0:
            print("\n¡Te has quedado sin dinero! Fin del juego.")
            break

    if dinero == 1000000:
        print("\n¡Felicidades! ¡Ústed salvó al millón!\n")
    else:
        print(f"\nJuego terminado. Se va con ${dinero}.\n")