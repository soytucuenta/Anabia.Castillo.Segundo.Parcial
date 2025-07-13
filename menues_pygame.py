import pygame
from funciones_pygame import *
def dibujar_seleccion_usuario(VENTANA,fuente_importada, rectangulo_usuario, color_usuario, texto_usuario, boton_usuario):
    pygame.draw.rect(VENTANA, color_usuario, rectangulo_usuario,3)  # Dibuja el rectángulo del input box
    superficie_seleccion_usuario = fuente_importada.render(texto_usuario, True, color_usuario)
    VENTANA.blit(superficie_seleccion_usuario, (rectangulo_usuario.x + 5, rectangulo_usuario.y + 5))  # Dibuja el texto dentro del input box
    dibujar_boton(boton_usuario)