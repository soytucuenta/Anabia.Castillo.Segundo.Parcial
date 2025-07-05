from leer_escribir_archivos import *
configuracion_default = {
    "dificultad": "media",
    "categoria": None,
    "neurodivergente": False,
    "recuperatorio": False
}




def seleccion_dificultad(mensaje_menu:str, valor_actual: str):
    control = valor_actual
    seleccion = int(input(mensaje_menu))
    while seleccion != 4:
        match seleccion:
            case 1:
                dificultad = 'fácil'
            case 2:
                dificultad = 'media'
            case 3:
                dificultad = 'difícil'
            case 4:
                dificultad = None
                break
        seleccion = int(input(mensaje_menu))
    if dificultad == None:
        dificultad = control
    return dificultad
def seleccion_categoria(mensaje_menu: str, valor_actual: str):
    control = valor_actual
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
    while seleccion != 8:
        match seleccion:
            case 1:
                categoria = lista_categorias[0]
                break
            case 2:
                categoria= lista_categorias[1]
                break
            case 3:
                categoria = lista_categorias[2]
                break
            case 4:
                categoria = lista_categorias[3]
                break
            case 5:
                categoria = lista_categorias[4]
                break
            case 6:
                categoria = lista_categorias[5]
                break
            case 7:
                categoria = None
                break
        
        seleccion = int(input(mensaje_menu))
    if valor_actual == None and categoria == None:
        categoria = valor_actual

    return categoria

