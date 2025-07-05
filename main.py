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
            configuraciones_partida = preparar_partida(config, todas_las_preguntas)
            #contador participaciones
            operar_en_clave_especifica(usuarios, 'nombre', info_usuario, incrementar_clave_especifica, 'participaciones')
            #iniciar juego
            fajos = gameplay(20, configuraciones_partida[0], cheats, configuraciones_partida[1])
            #suma ganancias
            dinero = fajos * 50000
            operar_en_clave_especifica(usuarios, 'nombre', info_usuario, sumar_en_clave, 'ganancias',dato_entrante=dinero)
        case 2:
            print(instrucciones)
        case 3:
            mostrar_diccionario_individual(info_usuario, "\nMostrando informacion del usuario actual: \n")
        case 4:#muestra el listado de usuarios
            for usuario in usuarios:
                mostrar_diccionario_individual(usuario, "\nMostrando informacion de todos los usuarios: \n")
        case 5:#configuracion del juego
            configurar_juego(config, mensajes_config)
    # volver a preguntar por el menu
    opcion_menu = int(input(menu))
    
#guardado de datos de usuarios
escribir_csv_usuarios(usuarios)
print("guardando puntajes... \n")
escribir_configuracion(config)
print("guardando configuracion... \n")
print("Gracias por jugar, hasta la proxima!")


