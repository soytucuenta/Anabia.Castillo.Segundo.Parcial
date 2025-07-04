configuracion_default = {
    "dificultad": "media",
    "tiempo": 60,
    "dinero_inicial": 1000000,
    "neurodivergencia": False,
    "categoria": "todas",
}

dificultades = {
    "facil": {
        "pool_preguntas": "facil"
    },
    "media": {
        "pool_preguntas": "media"
    },
    "dificil": {
        "pool_preguntas": "dificil"
    }
}


# el usuario JUAN juega se crea un registro de un usuarios nuevo
# ese registro se guarda en el archivo de usuarios
# los registros de todos los usuarios se guardarn de mayor a menor quien gano mas plata
# APRTE se pueden crear estadisticas, del rango edad, sexo que mas gano
# las preguntas se cargan aparte
# los usuarios tambien
# SIEMPRE AL TERMINAR SE GUARDA ESE USUARIO
# ENTRO ELIJO EL NIVEL DE DIFICULTAD< LUEGO QUE ME PREGUNTE POR LA CATEGORIA Y ME DE UNA PREGUNTA RANDOM
# DE ESA CATEGORIA, QUE EL TIEMPO SEA DE ACUERDO AL NIVEL, Y TERMINO
