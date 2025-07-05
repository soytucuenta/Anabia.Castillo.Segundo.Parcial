def filtrar_listas_de_dic(lista:list, clave:str)->list:
    lista = []

    for elemento in lista:
        if elemento[clave] == clave:
            lista.append(elemento)

    return lista