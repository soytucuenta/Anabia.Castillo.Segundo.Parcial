from prints import *
from preguntas import *
from logica_preguntas import *
from usuarios import *
from leer_escribir_archivos import *
from funciones_genericas import *
# meter tuplas o sets
# Trampa
cheats = True #pasa por parametro a gameplay y despues a la de mostrar pregunta y dice el numero de opcion de la correcta
#
#inicializacion de datos
todas_las_preguntas = cargar_preguntas("csv/preguntas.csv") #carga las preguntas desde el CSV
usuarios = cargar_usuarios() #carga los usuarios desde el CSV
info_usuario = seleccion_usuario(usuarios)
opcion_menu = int(input(menu))
preguntas_filtradas = obtener_preguntas_filtrando(todas_las_preguntas, 5, dificultad=info_usuario['dificultad'], categoria='ciencia')

while opcion_menu != 6:
    match opcion_menu:
        case 1:
            #contador participaciones
            operar_en_clave_especifica(usuarios, 'nombre', info_usuario, incrementar_clave_especifica, 'participaciones')
            dinero = gameplay(1000000, 60, cheats, preguntas_filtradas)
            #suma ganancias
            operar_en_clave_especifica(usuarios, 'nombre', info_usuario, sumar_en_clave, 'ganancias',dato_entrante=dinero)
        case 2:
            print(instrucciones)
        case 3:
            mostrar_datos_usuario(info_usuario, "\nMostrando informacion del usuario actual: \n")
        case 4:#muestra el listado de usuarios
            for usuario in usuarios:
                mostrar_datos_usuario(usuario, "\nMostrando informacion de todos los usuarios: \n")
        case 5:
            seleccion_configuracion = int(input(mensaje_configuraciones))
            while seleccion_configuracion != 3:
                match seleccion_configuracion:
                    case 1:
                        dificultad = seleccion_dificultad(mensaje_dificultad)
                        preguntas_filtradas = obtener_preguntas_filtrando(todas_las_preguntas, 5, dificultad=info_usuario['dificultad'], categoria='ciencia')
                    case 2:
                        menu_categoria = input(mensaje_categoria)
                        categoria = seleccion_categoria(menu_categoria)
                        preguntas_filtradas = obtener_preguntas_filtrando(todas_las_preguntas, 5, dificultad=info_usuario['dificultad'], categoria=info_usuario['categoria'])

    # volver a preguntar por el menu
    opcion_menu = int(input(menu))
    
print(info_usuario)
print(usuarios)
#guardado de datos de usuarios
escribir_csv_usuarios(usuarios)
print("guardando puntajes... \n")


