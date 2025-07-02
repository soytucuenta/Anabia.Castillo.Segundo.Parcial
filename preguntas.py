# HACER LÓGICA PARA ABRIR CSV Y CREAR LISTA DE DICCIONARIOS COMO ESTA ->
preguntas = []

with open ("preguntas.csv", "r") as archivo:
    for linea in archivo:
        registro = linea.strip().split(",")
        if registro[0][0] != "i":
            lista = {}
            lista["id"] = int(registro[0])
            lista["pregunta"] = registro[1]
            lista["opciones"] = registro[2].split("|")
            lista["correcta"] = int(registro[3])
            lista["dificultad"] = registro[4]
            lista["categoría"] = registro[5]
            preguntas.append(lista)