import re
from usuarios import *

def escribir_csv_usuarios(lista_dic_usuarios, archivo):
    """
    Escribe una lista de diccionarios de usuarios en un archivo CSV.
    Cada diccionario de la lista debe contener las claves: 'nombre', 'edad', 'profesion', 'participaciones' y 'ganancias'.
    Los valores de cada usuario se escribirán en una línea del archivo, separados por comas.
    Args:
        lista_dic_usuarios (list): Lista de diccionarios con los datos de los usuarios.
        archivo (str): Ruta del archivo donde se escribirá el CSV.
    Returns:
        None
    """

    with open(archivo,'w',encoding ='utf8') as archivo:
        delimitador = ','
        for i in lista_dic_usuarios:
            mensaje = '{0},{1},{2},{3},{4},{5}'
            mensaje = mensaje.format(i['nombre'],
                                i['edad'],
                                i['profesion'],
                                i['participaciones'],
                                i['ganancias'],
                                i['dificultad'])
            archivo.write(f'{mensaje}\n')


def cargar_usuarios(path: str) ->list:
    """
    Carga una lista de usuarios desde un archivo de texto.
    El archivo debe tener líneas con los siguientes campos separados por comas:
    nombre,edad,profesion,participaciones,ganancias
    Args:
        path (str): Ruta al archivo de texto que contiene los datos de los usuarios.
    Returns:
        list: Una lista de diccionarios, cada uno representando un usuario con las claves:
            - 'nombre' (str)
            - 'edad' (str)
            - 'profesion' (str)
            - 'participaciones' (int)
            - 'ganancias' (int)
    """

    lista =[]
    archivo = open(path, 'r', encoding ='UTF8')
    #archivo.readline()#lectura fantasma para saltar linea y leer el edad int bien
    for linea in archivo:
        lectura = re.split(',|\n', linea)
        dato = { }
        dato ['nombre'] = lectura[0]
        dato ['edad'] = lectura[1]
        dato ['profesion'] = lectura[2]
        dato ['participaciones'] = int(lectura[3])
        dato ['ganancias'] = int(lectura[4])
        dato ['dificultad'] = lectura[5]
        lista.append(dato)
    return lista


#test
#escribir_csv_usuarios(usuarios, 'usuarios.csv')
#lista_usuarios = cargar_usuarios('usuarios.csv')
#for usuario in lista_usuarios:
#    mostrar_datos_usuario(usuario, "\nMostrando informacion de los usuarios cargados desde el CSV: \n")