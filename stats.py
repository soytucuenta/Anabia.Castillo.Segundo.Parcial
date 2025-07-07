from leer_escribir_archivos import cargar_usuarios
from usuarios import ordenar_ranking

lista_dicc_usuarios = cargar_usuarios('csv/usuarios.csv')
def mostrar_por_ranking(lista_dicc_usuarios:list):
    """
    Muestra la lista de usuarios ordenada por ranking.
    Args:
        lista_dicc_usuarios (list): Lista de diccionarios de usuarios.
    """
    lista_dicc_usuarios = ordenar_ranking(lista_dicc_usuarios)
    print("Usuarios ordenados por ranking:")
    for usuario in lista_dicc_usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Ganancias: {usuario['ganancias']}, Participaciones: {usuario['participaciones']}, Mejor racha: {usuario['mejor racha']}, Ranking: {usuario['ranking']}")


def mostrar_usuarios_top(lista_dicc_usuarios:list,cantidad):
    lista_dicc_usuarios = ordenar_ranking(lista_dicc_usuarios)
    lista_top = []
    for usuario in lista_dicc_usuarios:
        if usuario['ranking'] >= cantidad:
            lista_top.append(usuario)
            break
    

"""---------TESTING---------"""
#mostrar_por_ranking(lista_dicc_usuarios)
mostrar_usuarios_top(lista_dicc_usuarios,10)