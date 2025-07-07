from prints import *
from preguntas import *
from logica_preguntas import *
from usuarios import *
from leer_escribir_archivos import *
from funciones_genericas import *
from config import *
from stats import *


def main():
    cheats = True #pasa por parametro a gameplay y despues a la de mostrar pregunta y dice el numero de opcion de la correcta

    todas_las_preguntas = cargar_preguntas() 
    usuarios = cargar_usuarios() 
    config = cargar_configuracion(configuracion_default) 
    
    opcion_menu = int(input(menu))
    while opcion_menu != 7:
        match opcion_menu:
            case 1:
                jugar_consola(usuarios, config, todas_las_preguntas, cheats)
                ordenar_ranking(usuarios) 
            case 2:
                print(instrucciones)
            case 3:
                seleccion_stats(usuarios, mensaje_usuarios_stats)
            case 4:
                mostrar_lista_diccionarios(usuarios, "Usuarios registrados:")
            case 5:
                configurar_juego(config, mensajes_config)
            case 6:
                info_usuario = agregar_nuevo_usuario_main(usuarios)
                if info_usuario != None:
                    sincronizar_diccionario(info_usuario, usuarios, 'id')
        opcion_menu = int(input(menu))
    escribir_csv_usuarios(usuarios)
    print("guardando puntajes... \n")
    escribir_configuracion(config)
    print("guardando configuracion... \n")
    print("Gracias por jugar, hasta la proxima!")

if __name__ == "__main__":
    main()


