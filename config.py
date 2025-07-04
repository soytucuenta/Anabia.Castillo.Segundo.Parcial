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



def seleccion_dificultad(mensaje_menu:str):
    seleccion = int(input(mensaje_menu))
    while seleccion != 4:
        match seleccion:
            case 1:
                dificultad = 'fácil'
            case 2:
                dificultad = 'media'
            case 3:
                dificultad = 'difícil'
        seleccion = int(input(mensaje_menu))
    return dificultad
def seleccion_categoria(mensaje_menu: str):
    lista_categorias = [ #esto puede entrar por una lectura de lista de preguntas
        "ciencia",
        "arte",
        "historia",
        "matemáticas",
        "deportes",
        "geografía"
    ]
    categoria = None
    seleccion = int(input(mensaje_menu))
    while seleccion != 7:
        match seleccion:
            case 1:
                categoria = lista_categorias[0]
            case 2:
                categoria= lista_categorias[1]
            case 3:
                categoria = lista_categorias[2]
            case 4:
                categoria = lista_categorias[3]
            case 5:
                categoria = lista_categorias[4]
            case 6:
                categoria = lista_categorias[5]
            case _:
                print("Opción no válida.")
                categoria = None
        seleccion = int(input(mensaje_menu))

    return categoria

