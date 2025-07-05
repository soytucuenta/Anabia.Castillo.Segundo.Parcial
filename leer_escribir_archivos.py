import re
import json
from funciones_genericas import mostrar_diccionario_individual

#usar try except para manejar errores de lectura/escritura de archivos
"""-----------------------CONFIGURACION-----------------------"""

def escribir_configuracion(configuracion:dict, archivo:str='config.json'):
    with open(archivo, 'w', encoding='utf8') as archivo:
        json.dump(configuracion, archivo, indent=4)


def cargar_configuracion(configuracion_default:dict,archivo:str='config.json') -> dict:
    """
    Carga la configuracion desde un archivo JSON.
    Si el archivo no existe, devuelve la configuracion por defecto.
    Args:
        configuracion_default (dict): Configuracion por defecto a usar si no se encuentra el archivo.
        archivo (str): Ruta al archivo JSON que contiene la configuracion.
    Returns:
        dict: La configuracion cargada desde el archivo o la configuracion por defecto.
    """
    bandera = False
    configuracion = {}
    try:
        with open(archivo, 'r', encoding='utf8') as archivo:
            configuracion =  json.load(archivo)
    except FileNotFoundError:
        configuracion = configuracion_default
        bandera = True
    if len(configuracion) != len(configuracion_default):#ver que no falten claves
        configuracion = configuracion_default
        bandera = True
    if bandera:
        print(f"Archivo de configuracion no encontrado o incompleto, se usara la configuracion por defecto: {configuracion_default}")
    return configuracion

"""-----------------------CSV USUARIOS-----------------------"""


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
        archivo.write('id,nombre,edad,profesion,participaciones,ganancias,dificultad\n')
        for i in lista_dic_usuarios:
            mensaje = '{0},{1},{2},{3},{4},{5},{6}'
            mensaje = mensaje.format(i['id'] ,
                                i['nombre'],
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
    with open(path, 'r', encoding='UTF8') as archivo:
        archivo.readline()
        for linea in archivo:
            lectura = re.split(',|\n', linea)
            dato = {}
            dato['id'] = int(lectura[0])
            dato['nombre'] = lectura[1]
            dato['edad'] = int(lectura[2])
            dato['profesion'] = lectura[3]
            dato['participaciones'] = int(lectura[4])
            dato['ganancias'] = int(lectura[5])
            dato['dificultad'] = lectura[6]
            lista.append(dato)
    return lista


#test
# test_usuarios = cargar_usuarios()
# escribir_csv_usuarios(test_usuarios, 'csv/usuarios.csv')


# # lista_usuarios = cargar_usuarios()
# for usuario in test_usuarios:
#     mostrar_diccionario_individual(usuario, "\nMostrando informacion de los usuarios cargados desde el CSV: \n")