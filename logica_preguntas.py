
import time

def mostrar_pregunta_y_opciones(pregunta_dict:dict,tiempo_limite:int,cheats:bool):
    """
    Muestra una pregunta y sus opciones por consola.
    Args:
        pregunta_dict (dict): Un diccionario que contiene la pregunta bajo la clave "pregunta" y una lista de opciones bajo la clave "opciones".
    """
    print(f"Llena cada pregunta en menos de {tiempo_limite} segundos o perdes todo")
    input("Ingrese cualquier cosa para continuar: ")
    print(pregunta_dict["pregunta"])
    print("")
    if cheats == True:
        print(f"APAGA LOS HACKS!!\n¡La respuesta correcta es la opción número {pregunta_dict['correcta'] + 1}!")
    opciones = pregunta_dict["opciones"]
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")

def solicitar_apuestas(dinero:int,tiempo_limite:int)-> list:
    """
    Solicita al usuario que ingrese una cantidad de dinero para apostar por cada opción, validando que las apuestas no supere el dinero disponible.
    Args:
        dinero (int): La cantidad de dinero disponible para apostar.
    Returns:
        (list): La cantidad/es apostada/s por el usuario.
    """
    flag_tiempo = False
    apuestas = [0, 0, 0, 0]
    apostando = 0
    print("")
    for i in range(len(apuestas)):
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

def procesar_respuesta(pregunta_dict:dict, dinero:int, apuestas:list) -> int:
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

def gameplay(dinero:int,tiempo_limite:int,cheats:bool,preguntas:list):
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
        mostrar_pregunta_y_opciones(preguntas[i],tiempo_limite,cheats)
        # pregunta por cada opción.
        apuestas = solicitar_apuestas(dinero,tiempo_limite)
        # la opción ganadora es el nuevo dinero.
        dinero = procesar_respuesta(preguntas[i], dinero, apuestas)
        # avanza de nivel
        nivel += 1
        
        if dinero <= 0: #Aca el minijuego si te quedas sin dinero?
            print("\n¡Te has quedado sin dinero! Fin del juego.")
            break

    if dinero == 1000000:
        print("\n¡Felicidades! ¡Ústed salvó al millón!\n")
    else:
        print(f"\nJuego terminado. Se va con ${dinero}.\n")

    return dinero