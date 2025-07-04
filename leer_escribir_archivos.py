import re
from usuarios import *
#usar try except para manejar errores de lectura/escritura de archivos

def escribir_csv_usuarios(lista_dic_usuarios, archivo='csv/usuarios.csv'):
    """
    Escribe una lista de diccionarios de usuarios en un archivo CSV.
    Cada diccionario debe contener las siguientes claves: 'nombre', 'edad', 'profesion', 'participaciones', 'ganancias' y 'dificultad'.
    La función escribe los datos de cada usuario como una línea separada por comas en el archivo CSV especificado.
    Args:
        lista_dic_usuarios (list of dict): Lista de diccionarios de usuarios a escribir en el archivo CSV.
        archivo (str, opcional): Ruta al archivo CSV. Por defecto es 'csv/usuarios.csv'.
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


def cargar_usuarios(path:str="csv/usuarios.csv") ->list:
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
    archivo.readline()#lectura fantasma para saltar linea y leer el edad int bien
    for linea in archivo:
        lectura = re.split(',|\n', linea)
        dato = { }
        dato ['id'] = int(lectura[0])
        dato ['nombre'] = lectura[1]
        dato ['edad'] = lectura[2]
        dato ['profesion'] = lectura[3]
        dato ['participaciones'] = int(lectura[4])
        dato ['ganancias'] = int(lectura[5])
        dato ['dificultad'] = lectura[6]
        lista.append(dato)
    return lista


#test
#escribir_csv_usuarios(usuarios, 'usuarios.csv')
lista_usuarios = cargar_usuarios()
for usuario in lista_usuarios:
    mostrar_datos_usuario(usuario, "\nMostrando informacion de los usuarios cargados desde el CSV: \n")