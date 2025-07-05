def operar_en_clave_especifica(lista_diccionarios: list,nombre: str, diccionario_individual: dict, operacion, clave_cambiante: str, dato_entrante: int | float | str | list = None):
    """
    Realiza una operación sobre una clave específica de un diccionario dado y actualiza la clave correspondiente en una lista de diccionarios.

    Args:
        nombre (str): La clave utilizada para identificar el diccionario dentro de la lista (por ejemplo, un identificador único o nombre).
        diccionario_individual (dict): El diccionario sobre el cual se realizará la operación.
        lista_diccionarios (list): Una lista de diccionarios entre los cuales se actualizará el diccionario coincidente.
        operacion (callable): Una función que se aplica a la clave especificada en el diccionario. Debe aceptar dos o tres argumentos dependiendo de si dato_entrante es proporcionado.
        clave_cambiante (str): La clave en el diccionario cuyo valor será operado y actualizado.
        dato_entrante (int | float | str | list, opcional): Un argumento adicional para pasar a la función de operación. Por defecto es None.

    Comportamiento:
        - Si dato_entrante es None, llama a operacion(diccionario_individual, clave_cambiante).
        - De lo contrario, llama a operacion(diccionario_individual, clave_cambiante, dato_entrante).
        - Después de la operación, actualiza el valor de clave_cambiante en el diccionario coincidente dentro de lista_diccionarios (coincidencia por el valor de nombre, sin distinguir mayúsculas/minúsculas).
    """

    if dato_entrante == None:
        operacion(diccionario_individual, clave_cambiante)
    else:
        operacion(diccionario_individual, clave_cambiante, dato_entrante)
    for elemento in lista_diccionarios:
        if elemento[nombre].lower() == diccionario_individual[nombre].lower():
            elemento[clave_cambiante] = diccionario_individual[clave_cambiante]
            
def incrementar_clave_especifica(diccionario_usuario:dict, clave:str):
    diccionario_usuario[clave] += 1

def sumar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] += valor

def restar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] -= valor

def multiplicar_en_clave(diccionario:dict, clave:str, valor:int):
    diccionario[clave] *= valor

def dividir_en_clave(diccionario:dict, clave:str, valor:int):
    if valor != 0:
        diccionario[clave] /= valor

def reemplazar_en_clave(diccionario:dict, clave:str, valor):
    diccionario[clave] = valor

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
