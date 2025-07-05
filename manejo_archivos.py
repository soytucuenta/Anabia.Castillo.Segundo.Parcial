import re
import json
from manejo_usuarios import *

def cargar_config_json(path: str):
    with open(path, "r") as archivo: 
        config = json.load(archivo)
        return config

def cargar_usuarios_csv(path: str) ->list:
    usuarios = []
    with open (path, "r") as archivo:
        for linea in archivo:
            registro = linea.strip().split(",")
            if registro[0][0] != "i":
                lista = {}
                lista["id"] = int(registro[0])
                lista["nombre"] = registro[1]
                lista["edad"] = int(registro[2])
                lista["profesion"] = registro[3]
                lista["ganancias"] = int(registro[5])
                lista["dificultad"] = registro[6]
                usuarios.append(lista)
    return usuarios

def cargar_preguntas_csv(path: str) ->list:
    preguntas = []
    with open (path, "r") as archivo:
        for linea in archivo:
            registro = linea.strip().split(";")
            if registro[0][0] != "i":
                lista = {}
                lista["id"] = int(registro[0])
                lista["pregunta"] = registro[1]
                lista["opciones"] = registro[2].split("|")
                lista["correcta"] = int(registro[3])
                lista["dificultad"] = registro[4]
                lista["categoría"] = registro[5]
                preguntas.append(lista)
    return preguntas

def escribir_csv_usuarios(lista_dic_usuarios, archivo):
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