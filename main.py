from prints import *
from logica_preguntas import *
from usuarios import *
from leer_escribir_archivos import *
from funciones_genericas import *

#inicializacion de datos
# usuarios = cargar_usuarios('usuarios.csv') #carga los usuarios desde el CSV
# info_usuario = seleccion_usuario(usuarios)

opcion_menu = int(input(menu))

while opcion_menu != 6:
    match opcion_menu:
        case 1:
            dinero = gameplay(1000000, 60)
        case 2:
            print(instrucciones)
        case 3:
            mostrar_datos_usuario(info_usuario, "\nMostrando informacion del usuario actual: \n")
        case 4:
            for usuario in usuarios:
                mostrar_datos_usuario(usuario, "\nMostrando informacion de todos los usuarios: \n")
        case 5:
            pass
        
    # volver a preguntar por el menu
    opcion_menu = int(input(menu))
    
print(info_usuario)
print(usuarios)
#guardado de datos de usuarios
escribir_csv_usuarios(usuarios, 'usuarios.csv')
print("guardando puntajes... \n")


