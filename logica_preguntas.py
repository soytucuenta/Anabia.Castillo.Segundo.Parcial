import time
from manejo_archivos import *
from manejo_usuarios import *

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

def procesar_respuesta(pregunta_dict:dict, apuestas:list) -> int:
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
    print(f"¡Espero que haya apostado bien!\n")

    return dinero

def gameplay():
    """
    Gameplay general del juego Salve al millón.
    """

    print("\nDISCLAIMER: Este juego fue desarrollado teniendo en cuenta\n"
        "a personas con capacidades diferentes, por eso hay una serie de preguntas\n"
        "que debemos hacerle para personalizar más su experiencia."
    )

    daltonico = int(input("\nEs usted daltonico?\n1. Si\n2. No\n\nSeleccione una opción: "))
    neurodivergente =  int(input("\nEs usted neurodivergente?\n1. Si\n2. No\n\nSeleccione una opción: "))

    nivel_dificultad =  int(input("\nElija un nivel de dificultad\n1. Fácil\n2. Medio\n3. Difícil\n\nSeleccione una opción: "))
    
    match nivel_dificultad:
        case 1:
            dificultad = "facil"
            tiempo_limite = 30
        case 2:
            dificultad = "medio"
            tiempo_limite = 20
        case 3:
            dificultad = "dificil"
            tiempo_limite = 10

    nivel = 1
    dinero = 1000000
    preguntas = cargar_preguntas_csv("csv/preguntas-test.csv")
    config = cargar_config_json("config.json")
    
    print("\nComenzemos!\n ")
    print(f"Tomá! Este $1.000.000 es tuyo!\n")
    print("(!) Recuerde que lo que no apuesta, lo pierde. (!)\n")

    for i in  range(len(preguntas)):
        print(f'[Dinero disponible: ${dinero}]\n')
        print(f"[Pregunta {nivel:}]\n")

        print("Eliga una de las categorías: ")
        print("#---------------------------------------------------------#")
        print(f"#1. Matemática{' ':>5}| 2. Ciencia{' ':>5}| 3. Deportes{' ':>9}|")
        print(f"#4. Artes{' ':>10}| 5. Historia{' ':>26}|")
        print(f"#---------------------------------------------------------#")
        categoría = input("Seleccione: ")

        

        # simple print de preguntas y opciones.
        mostrar_pregunta_y_opciones(preguntas[i])
        # apuesta por cada opción y tiempo límite
        apuestas = solicitar_apuestas(dinero, tiempo_limite)
        # la opción ganadora es el nuevo dinero.
        dinero = procesar_respuesta(preguntas[i], apuestas)
        
        nivel += 1
        
        if dinero <= 0:
            print("¡Te has quedado sin dinero!")
            break

    if dinero == 1000000:
        print("¡Felicidades! ¡Ústed salvó al millón!\n")
        print("¡Se va con $1.000.000!\n")
    else:
        print(f"Juego terminado. Se va con ${dinero}.\n")

    guardar_usuario(dinero, dificultad)