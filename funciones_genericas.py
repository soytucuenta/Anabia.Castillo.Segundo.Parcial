import copy

def incrementar_clave_especifica(diccionario_usuario:dict, clave:str):
    diccionario_usuario[clave] += 1

def sumar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] += valor

def restar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] -= valor

def multiplicar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] *= valor
def mostrar_lista_diccionarios(lista:list, mensaje:str=None):
    for diccionario in lista:
        mostrar_diccionario_individual(diccionario, mensaje)
def dividir_en_clave(diccionario:dict, clave:str, valor:int):
    if valor != 0:
        diccionario[clave] /= valor

def reemplazar_en_clave(diccionario:dict, clave:str, valor):
    diccionario[clave] = valor
def sincronizar_diccionario(diccionario:dict, lista_usuarios:list, clave_busqueda:str):
    """
    Sincroniza un diccionario de usuario con una lista de usuarios, actualizando el usuario en la lista si existe.
    Args:
        diccionario (dict): Diccionario del usuario a sincronizar.
        lista_usuarios (list): Lista de usuarios donde se buscará el usuario a actualizar.
        clave_busqueda (str): Clave del diccionario que se usará para buscar al usuario en la lista.
    """
    for i in range(len(lista_usuarios)):
        if lista_usuarios[i][clave_busqueda] == diccionario[clave_busqueda]:
            lista_usuarios[i] = copy.deepcopy(diccionario)
            return
    lista_usuarios.append(copy.deepcopy(diccionario))

def buscar_maximo_lista(lista:list):
    if len(lista) == 0:
        maximo = 0
    else:
        maximo = lista[0]
        for i in range(len(lista)):
            if lista[i] > maximo:
                maximo = lista[i]
    return maximo
def buscar_maximo(maximo_anterior:int, nuevo_valor:int):
    """
    Compara un valor nuevo con un máximo anterior y devuelve el mayor de los dos.
    Args:
        maximo_anterior (int): El valor máximo anterior.
        nuevo_valor (int): El nuevo valor a comparar.
    Returns:
        int: El mayor entre el máximo anterior y el nuevo valor.
    """
    salida = maximo_anterior
    if nuevo_valor > maximo_anterior:
        salida = nuevo_valor
    return salida
def promediar_lista(lista:list):
    for i in range(len(lista)):
        acumulador += lista[i]
    promedio = acumulador / len(lista)
    return promedio

def mostrar_diccionario_individual(diccionario:dict,mensaje:str=None):
    if type(mensaje) == str:
        print(mensaje)
    for dato in diccionario:
        print(f"{dato}: {diccionario[dato]}")

"""---------------------DEPRECATED---------------------"""
def listar_claves_lista_dicc(lista_diccionarios, termino_busqueda):
    busqueda = []
    for diccionario in lista_diccionarios:
        for clave in diccionario:
            if clave.lower() == termino_busqueda.lower():
                busqueda.append(diccionario[termino_busqueda])
                break

    resultado = eliminar_strings_duplicados(busqueda)
    return resultado
def eliminar_strings_duplicados(lista:list):
    lista_auxiliar = []
    for i in range(len(lista)):
        encontrado = False
        string_actual = lista[i]
        for j in range(len(lista)):
            if string_actual == lista[j] and encontrado == False:
                lista_auxiliar.append(string_actual)
                encontrado = True
                break
    return set(lista_auxiliar)


def inicializar_usuarios(lista_dicc_usuarios)-> dict:

    datos_usuario = {"id": 0,"nombre": None, "ganancias": 0 , "participaciones": 0,"mejor racha": 0, "ranking": 0}
    datos_usuario["nombre"] = input("ingrese nombre de usuario: ")
    datos_usuario ["id"] = len(lista_dicc_usuarios) + 1 
    datos_usuario['ganancias'] = 0
    datos_usuario["participaciones"] = 0
    datos_usuario['mejor racha'] = 0
    datos_usuario['ranking'] = 0
    lista_dicc_usuarios.append(datos_usuario)
    return datos_usuario


