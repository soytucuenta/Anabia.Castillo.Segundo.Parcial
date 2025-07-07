import time
from funciones_genericas import *
from usuarios import *
from config import *
def jugar_consola(lista_usuarios:list, configuracion:dict, preguntas:list, cheats:bool):
    """
    Permite jugar una partida de preguntas y respuestas en la consola para un usuario seleccionado.
    Parámetros:
        lista_usuarios (list): Lista de diccionarios que contienen la información de los usuarios.
        configuracion (dict): Diccionario con la configuración general del juego.
        preguntas (list): Lista de preguntas disponibles para la partida.
        cheats (bool): Indica si los trucos están habilitados.
    El flujo de la función es el siguiente:
        - Selecciona un usuario de la lista.
        - Inicializa la racha y las estadísticas del usuario.
        - Ejecuta rondas de juego mientras el usuario desee continuar.
        - Calcula las ganancias y actualiza la racha según el desempeño.
        - Permite al usuario decidir si continúa o termina la partida.
        - Al finalizar, actualiza la mejor racha y sincroniza la información del usuario en la lista.
    Retorno:
        None
    """

    
    info_usuario = seleccion_usuario_consola(lista_usuarios)
    racha_previa = info_usuario['mejor racha']
    lista_rachas = [racha_previa]
    racha = 0
    continuar = True
    while continuar == True:
        dificultad_usuario = info_usuario['dificultad']
        configuraciones_partida = preparar_partida(configuracion, preguntas, dificultad_usuario)
        incrementar_clave_especifica(info_usuario, 'participaciones')
        fajos = gameplay(20, configuraciones_partida[0], cheats, configuraciones_partida[1])
        dinero =  50000 * fajos
        if dinero > 0:
            racha  += 1
            dinero = multiplicador_de_dificultad(dificultad_usuario) * dinero
            dinero = int(dinero)
            sumar_en_clave(info_usuario, 'ganancias', dinero)
            print(f"\n¡Felicidades! ¡Usted salvó ${dinero}!\n")
        else:
            lista_rachas.append(racha)
            racha = 0
        preguntar = input("¿Desea continuar? (s/n): ").lower()
        if preguntar != "s":
            continuar = False            
    if len(lista_rachas) > 0:
        info_usuario['mejor racha'] = buscar_maximo_lista(lista_rachas)
    sincronizar_diccionario(info_usuario,lista_usuarios, 'id')
def multiplicador_de_dificultad(dificultad:str) -> float:
    """
    Retorna un multiplicador basado en la dificultad de la pregunta.
    Args:
        dificultad (str): Dificultad de la pregunta ('facil', 'media', 'dificil').
    Returns:
        int: Multiplicador correspondiente a la dificultad.
    """
    match dificultad:
        case "facil":
            multiplicador = 0.5
        case "media":
            multiplicador = 1
        case "dificil":
            multiplicador = 2
    return multiplicador

def mostrar_pregunta_y_opciones(pregunta_dict:dict,tiempo_limite:int,cheats:bool):
    """
    Muestra una pregunta y sus opciones por consola.
    Args:
        pregunta_dict (dict): Un diccionario que contiene la pregunta bajo la clave "pregunta" 
        y una lista de opciones bajo la clave "opciones".
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
    Solicita al usuario que ingrese una cantidad de dinero para apostar por cada opción, validando 
    que las apuestas no supere el dinero disponible.
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
        tiempo_inicial = time.time()
        apuestas[i] = int(input(f"¿Cuántos fajos por la opción {i+1}?: "))
        while apostando + apuestas[i] > dinero:
            print(f"\nLo siento, no cuenta con fajos suficientes. Usted tiene {dinero - apostando} fajos.")
            apuestas[i] = int(input(f"¿Cuántos fajos por la opción {i+1}?: "))    
        apostando += apuestas[i]        
        tiempo_final = time.time()
        tiempo_transcurrido = tiempo_final - tiempo_inicial
        if tiempo_transcurrido > tiempo_limite:
            print("\n Excediste el tiempo limite para responder, perdes todo ")    
            flag_tiempo = True
        if apostando == dinero:
            print("\n¡Apostaste todo tu dinero!")
            break

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
    print("Te quedan...")
    return dinero

def gameplay(dinero:int,tiempo_limite:int,cheats:bool,preguntas:list):
    """
    Gameplay general del juego Salve al millón.
    """    
    nivel = 1    
    print("\nComenzemos!\n ")
    print(f"Tomá! Este ${dinero*50000} es tuyo!\n")
    for i in  range(len(preguntas)):
        print(f'[Fajos disponibles: {dinero}]\n')
        print(f"[Pregunta {nivel:}]\n")
        print("(!) Recuerde que lo que no apuesta, lo pierde. (!)\n")
        mostrar_pregunta_y_opciones(preguntas[i],tiempo_limite,cheats)
        apuestas = solicitar_apuestas(dinero,tiempo_limite)
        dinero = procesar_respuesta(preguntas[i], dinero, apuestas)
        nivel += 1
        if dinero <= 0: #Aca el minijuego si te quedas sin dinero?
            print("\n¡Te has quedado sin dinero! Fin del juego.")
            break
    return dinero