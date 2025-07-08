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

def crear_boton(dimensiones, posicion, ventana, color_borde, imagen = None, fuente = None, texto = None):#constructor
    boton = {}
    boton["Ventana"] = ventana
    boton["Dimensiones"] = dimensiones
    boton["Posicion"] = posicion
    boton["ColorBorde"] = color_borde
    boton["Presionado"] = False
    if imagen != None:
        img = pygame.image.load(imagen)
        boton["Superficie"] = pygame.transform.scale(img, boton["Dimensiones"])
    else:
        tipo, tamano = fuente
        fuente = pygame.font.SysFont(tipo, tamano)
        boton["Superficie"] = fuente.render(texto,False, "Red","Orange")
    boton["Rectangulo"] = boton["Superficie"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]
    

    return boton

def dibujar_boton(boton:dict):
    boton["Ventana"].blit(boton["Superficie"], boton["Posicion"])
    pygame.draw.rect(boton["Ventana"],boton["ColorBorde"],boton["Rectangulo"],2)
