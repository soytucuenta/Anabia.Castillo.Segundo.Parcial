import re
import json
from manejo_usuarios import *

def cargar_config_json(path: str):
    with open(path, "r", encoding ='utf8') as archivo: 
        config = json.load(archivo)
        return config

def cargar_preguntas_csv(path: str) ->list:
    preguntas = []
    with open (path, "r", encoding ='utf8') as archivo:
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

def cargar_usuarios_csv(path: str) ->list:
    usuarios = []
    with open (path, "r", encoding ='utf8') as archivo:
        for linea in archivo:
            registro = linea.strip().split(";")
            if registro[0][0] != "i":
                lista = {}
                lista["id"] = int(registro[0])
                lista["nombre"] = registro[1]
                lista["edad"] = int(registro[2])
                lista["profesión"] = registro[3]
                lista["ganancia"] = int(registro[4])
                lista["dificultad"] = registro[5]
                usuarios.append(lista)
    return usuarios

# def escribir_usuario_csv(usuario_dic, path):
