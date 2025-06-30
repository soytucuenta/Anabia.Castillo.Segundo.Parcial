import copy
usuarios = [
    {"nombre": "Juan", "edad": 30, "profesion": "Ingeniero", "dificultad": 5, "participaciones": 3, "ganancias": 1200, "tiempo": 95},
    {"nombre": "Maria", "edad": 25, "profesion": "Disenadora", "dificultad": 6, "participaciones": 2, "ganancias": 850, "tiempo": 72},
    {"nombre": "Luis", "edad": 40, "profesion": "Contador", "dificultad": 7, "participaciones": 5, "ganancias": 2100, "tiempo": 110},
    {"nombre": "Ana", "edad": 35, "profesion": "Doctora", "dificultad": 8, "participaciones": 6, "ganancias": 3400, "tiempo": 88},
    {"nombre": "Pedro", "edad": 28, "profesion": "Abogado", "dificultad": 4, "participaciones": 1, "ganancias": 300, "tiempo": 67},
    {"nombre": "Lucia", "edad": 32, "profesion": "Arquitecta", "dificultad": 6, "participaciones": 4, "ganancias": 1600, "tiempo": 102},
    {"nombre": "Carlos", "edad": 45, "profesion": "Profesor", "dificultad": 7, "participaciones": 3, "ganancias": 1300, "tiempo": 54},
    {"nombre": "Sofia", "edad": 22, "profesion": "Estudiante", "dificultad": 3, "participaciones": 1, "ganancias": 150, "tiempo": 39},
    {"nombre": "Diego", "edad": 38, "profesion": "Chef", "dificultad": 5, "participaciones": 2, "ganancias": 750, "tiempo": 77}
]


usuario_default = {"nombre": "default","edad": 18, "profesion": "Desocupado", "dificultad": 7, "participaciones": 0, "ganancias":0}

def buscar_usuario(nombre, lista_usuarios, bienvenida=False):
    usuario = "default"
    for usuario_busqueda in lista_usuarios:
        if usuario_busqueda["nombre"].lower() == nombre.lower():
            usuario = usuario_busqueda
            if bienvenida:
                print(f"Bienvenido {usuario['nombre']}")
    return usuario



def copiar_usuario_por_nombre(nombre_a_buscar, usuarios):
    datos_usuario = None
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre_a_buscar.lower():
            datos_usuario= copy.deepcopy(usuario)  
    return datos_usuario

