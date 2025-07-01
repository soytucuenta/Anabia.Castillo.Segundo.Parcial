import re
from usuarios import *
def escribir_csv_usuarios(lista_dic_usuarios, archivo):
    with open(archivo,'w',encoding ='utf8') as archivo:
        delimitador = ','
        for i in lista_dic_usuarios:
            mensaje = '{0},{1},{2},{3},{4}'
            mensaje = mensaje.format(i['nombre'],
                                i['edad'],
                                i['profesion'],
                                i['participaciones'],
                                i['ganancias'])
            archivo.write(f'{mensaje}\n')


def cargar_usuarios(path: str) ->list:
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
        lista.append(dato)
    return lista




#test
# escribir_csv_usuarios(usuarios, 'usuarios.csv')
# lista_usuarios = cargar_usuarios('usuarios.csv')
# for usuario in lista_usuarios:
#     mostrar_datos_usuario(usuario, "\nMostrando informacion de los usuarios cargados desde el CSV: \n")