import json

def cargar_config_json(path: str)->dict:
    """ Carga archivo json con las configuraciones del juego.
    Args:
        path (str): Dirección del json.
    Returns:
        (dict): Diccionario con las configuraciones.
    """
    try:
        with open(path, "r", encoding ='utf8') as archivo: 
            config = json.load(archivo)
            if not config:
                print("Error: El archivo está vacío")
                return None
            return config
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo '{path}'.")
        return None
    except UnicodeDecodeError:
        print(f"Error: Problema de codificación en el archivo '{path}' (no es UTF-8 válido).")
        return None
    except Exception as e:
        print(f"Error inesperado al leer '{path}': {str(e)}")
        return None

def cargar_preguntas_csv(path: str) ->list:
    """ Carga archhivo csv con las preguntas del juego.
    Args:
        path (str): Dirección del csv.
    Returns:
        list: Lista con las preguntas.
    """
    preguntas = []
    try:
        with open (path, "r", encoding ='utf8') as archivo:
            for linea in archivo:
                registro = linea.strip().split(";")
                if registro[0][0] != "p":
                    lista = {}
                    lista["pregunta"] = registro[0]
                    lista["opciones"] = registro[1].split("|")
                    lista["correcta"] = int(registro[2])
                    lista["dificultad"] = registro[3]
                    lista["categoría"] = registro[4]
                    preguntas.append(lista)
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no existe.")
        return []
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo '{path}'.")
        return []
    except UnicodeDecodeError:
        print(f"Error: El archivo '{path}' no tiene codificación UTF-8 válida.")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {str(e)}")
        return []
    return preguntas

def cargar_usuarios_csv(path: str) ->list:
    """ Carga archhivo csv con los usuarios del juego.
    Args:
        path (str): Dirección del csv.
    Returns:
        list: Lista con los usuarios.
    """
    usuarios = []
    try:
        with open (path, "r", encoding ='utf8') as archivo:
            for linea in archivo:
                registro = linea.strip().split(";")
                if registro[0][0] != "u":
                    lista = {}
                    lista["usuario"] = registro[0]
                    lista["ganancia"] = int(registro[1])
                    lista["dificultad"] = registro[2]
                    usuarios.append(lista)
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no existe.")
        return []
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo '{path}'.")
        return []
    except UnicodeDecodeError:
        print(f"Error: El archivo '{path}' no tiene codificación UTF-8 válida.")
        return []
    except Exception as e:
        print(f"Error inesperado al leer el archivo: {str(e)}")
        return []
    return usuarios

def guardar_usuario_csv(usuario_dic, path):
    """ Guarda diccionario de usuario en archivo csv de usuarios.
    Args:
        path (str): Dirección del csv.
    """
    try:
        with open(path, 'a', encoding ='utf8') as archivo:
            mensaje = '{0};{1};{2}'
            mensaje = mensaje.format(
            usuario_dic['usuario'],
            usuario_dic['ganancia'],
            usuario_dic['dificultad'])
            archivo.write(f'{mensaje}\n')
    except PermissionError:
        print("Error: No tienes permisos para modificar el archivo.")
    except Exception as e:
        print(f"Error al guardar usuario: {e}")
    else:
        print("\nUsuario guardado en base de datos!")
