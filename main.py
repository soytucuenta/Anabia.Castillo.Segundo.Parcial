from prints import *
from preguntas import *
from logica_preguntas import *
from usuarios import *
from leer_escribir_archivos import *
from funciones_genericas import *
from config import *
# meter tuplas o sets
# Trampa
cheats = True #pasa por parametro a gameplay y despues a la de mostrar pregunta y dice el numero de opcion de la correcta
#
#inicializacion de datos
todas_las_preguntas = cargar_preguntas() #carga las preguntas desde el CSV
usuarios = cargar_usuarios() #carga los usuarios desde el CSV
info_usuario = seleccion_usuario(usuarios)
config = cargar_configuracion(configuracion_default) #carga la configuracion desde el JSON

#menu principal
opcion_menu = int(input(menu))
while opcion_menu != 6:
    match opcion_menu:
        case 1:
            #consulta configuracion
            tiempo_limite = limitar_tiempo(config['dificultad'])
            print(f"\nTiempo limite: {tiempo_limite} segundos")
            if config['categoria'] == None:
                print("\nNo se ha seleccionado una categoria, se jugara con todo el pool de preguntas.")
                preguntas_filtradas = obtener_preguntas_filtrando(todas_las_preguntas, 5, dificultad=config['dificultad'])
            else:
                print(f"\nCategoria seleccionada: {config['categoria']}")
                preguntas_filtradas = obtener_preguntas_filtrando(todas_las_preguntas, 5, dificultad=config['dificultad'], categoria=config['categoria'])
            #contador participaciones
            operar_en_clave_especifica(usuarios, 'nombre', info_usuario, incrementar_clave_especifica, 'participaciones')
            #iniciar juego
            dinero = gameplay(1000000, tiempo_limite, cheats, preguntas_filtradas)
            #suma ganancias
            operar_en_clave_especifica(usuarios, 'nombre', info_usuario, sumar_en_clave, 'ganancias',dato_entrante=dinero)
        case 2:
            print(instrucciones)
        case 3:
            mostrar_diccionario_individual(info_usuario, "\nMostrando informacion del usuario actual: \n")
        case 4:#muestra el listado de usuarios
            for usuario in usuarios:
                mostrar_diccionario_individual(usuario, "\nMostrando informacion de todos los usuarios: \n")
        case 5:#configuracion del juego
            seleccion_configuracion = int(input(mensaje_configuraciones))
            while seleccion_configuracion != 4:
                match seleccion_configuracion:
                    case 1:
                        print(f"\nDificultad actual: {config['dificultad']}")
                        config['dificultad'] = seleccion_dificultad(mensaje_dificultad, config['dificultad'])
                        config['dificultad'] = info_usuario['dificultad']
                        print(f"\nDificultad seleccionada: {config['dificultad']}")
                    case 2:
                        print(f"\nCategoria actual: {config['categoria']}")
                        config['categoria'] = seleccion_categoria(mensaje_categoria, config['categoria'])
                    case 3:
                        mostrar_diccionario_individual(config, "\nMostrando configuracion actual: \n")
                seleccion_configuracion = int(input(mensaje_configuraciones))

    # volver a preguntar por el menu
    opcion_menu = int(input(menu))
    
def menu_configuraciones(mensaje_configuraciones:str):
    pass
#guardado de datos de usuarios
escribir_csv_usuarios(usuarios)
print("guardando puntajes... \n")
escribir_configuracion(config)
print("guardando configuracion... \n")
print("Gracias por jugar, hasta la proxima!")


