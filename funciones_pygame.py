import pygame

def salida_pygame(evento, flag_run):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:#cambiable por si queremos retroceder a un menu despues
            flag_run = False
    elif evento.type == pygame.QUIT:        
        flag_run = False
    return flag_run


#######################
# el boton de ejemplo que dieron en clase

def crear_boton(dimensiones, posicion, ventana,color_texto="Black",color_fondo="Yellow" , imagen = None, fuente = None, texto = None):
    boton = {}
    boton["Ventana"] = ventana
    boton["Dimensiones"] = dimensiones
    boton["Posicion"] = posicion
    boton['ColorTexto'] = color_texto
    boton['ColorFondo'] = color_fondo
    boton["Presionado"] = False
    if imagen != None:
        img = pygame.image.load(imagen)
        boton["Superficie"] = pygame.transform.scale(img, boton["Dimensiones"])
    else:
        if fuente == None:
            fuente = pygame.font.Font("droidsans", 24)
        tipo, tamano = fuente
        fuente = pygame.font.SysFont(tipo, tamano)
        boton["Superficie"] = fuente.render(texto,False, color_texto,color_fondo)
    boton["Rectangulo"] = boton["Superficie"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]
    

    return boton

def dibujar_boton(boton:dict):
    boton["Ventana"].blit(boton["Superficie"], boton["Posicion"])
    pygame.draw.rect(boton["Ventana"],boton["ColorTexto"],boton["Rectangulo"],2)

def boton_presionado(boton:dict, evento):
    if boton['Rectangulo'].collidepoint(evento.pos):
        boton['Presionado'] = True