import pygame
import sys

pygame.init()

#Creando ventana, icono, nombre y fondo
size = (768, 368)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AngeLaos")
icono = pygame.image.load("angelaos.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")
screen.blit(fondo,(0,0))

#Paleta de colores
blanco = (255,255,255)
negro = (0,0,0)
amarillo = (255,255,0)
azul = (0,0,255)
rojo = (255,0,0)
verde = (0,255,0)
rosa = (255,0,255)
color_random = (153,12,52)
color_random1 = (231,54,123)

#figuras
# screen.fill(blanco)
# rectangulo = pygame.draw.rect(screen, negro,(100,50,100,50))
# linea = pygame.draw.line(screen,rosa,(100,104),(199,104),1)
# circulo = pygame.draw.circle(screen,color_random1,(122,250),20,15)

#Bucle de la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()