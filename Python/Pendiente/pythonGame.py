import pygame
import sys
import random


# Inicializar Pygame
pygame.init()

QUIERO_SEGUIR_JUGANDO = True

# Configurar vent ana
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Un rectángulo que no sale de la ventana")

# Colores
BLANCO = (255, 255, 255)
COLOR1 = (255, 0, 0)
COLOR2 = (0, 255, 255)


def rendomColor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


# Rectángulo 1 (rojo)
"""En el rectángulo:
rect.x: posición x en el lienzo, es la primera posición
rect.y: posición y en el lienzo, es la segunda posición
rect.w: anchura del rectángulo, es la tercera posición
rect.h: altura del rectángulo, es la cuarta posición

En el caso del rect1:
rect1.x = 100
rect1.y = 100
rect1.w = 50
rect1.h = 50
"""

# Rectángulo 2 (azul)
"""
rect2
react2.x = 100
rect2.y = 100
react2.w = 50
rect2.h = 50
"""


rect1 = pygame.Rect(100, 100, 100, 50)
react2 = pygame.Rect(100, 100, 100, 50)

# cambio
cambio = 1

# Reloj (No marques las horas)
reloj = pygame.time.Clock()
FPS = 60


# Bucleado principalmente
while QUIERO_SEGUIR_JUGANDO:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()  # pues eso, me voy
            sys.exit()  # ¡anda!... pues salimos ya.

    teclas = pygame.key.get_pressed()
    # print(f" Por favor dime que el tipo de la tecla es un/una:   {type(teclas)} !!!")
    # print(f"  y no es como el reloj que si que es de tipo: {type(reloj)}, ¿verdad?")

    # Movimiento del rectángulo rojo (jugador 1)
    if teclas[pygame.K_PLUS]:
        FPS += 20

    if teclas[pygame.K_MINUS]:
        FPS -= 20

    if teclas[pygame.K_c]:
        COLOR1 = rendomColor()
        COLOR2 = rendomColor()

    if teclas[pygame.K_a]:
        # Cambiaremos rect1.x si rect1.x previo es mayor que cero
        if rect1.x > 0:
            rect1.x -= cambio
    if teclas[pygame.K_d]:
        # Cambiaremos rect1.x más su ancho es menor que ANCHO_D_CADERAS
        if (rect1.x + rect1.w) < ANCHO:
            rect1.x += cambio
    if teclas[pygame.K_w]:
        # Cambiaremos rect1.y si su valor es mayor que 0
        if rect1.y > 0:
            rect1.y -= cambio
    if teclas[pygame.K_s]:
        # Cambiaremos la coordiadora y si su valor más la alta es menor que ALTO
        if (rect1.y + rect1.h) < ALTO:
            rect1.y += cambio

    if teclas[pygame.K_h]:
        if react2.x > 0:
            react2.x -= cambio
    if teclas[pygame.K_k]:
        if (react2.x + react2.w) < ANCHO:
            react2.x += cambio
    if teclas[pygame.K_u]:
        if react2.y > 0:
            react2.y -= cambio
    if teclas[pygame.K_j]:
        if (react2.y + react2.h) < ALTO:
            react2.y += cambio

    if rect1.colliderect(react2):
        COLOR1 = rendomColor()
        COLOR2 = rendomColor()

    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, COLOR1, rect1)
    pygame.draw.rect(ventana, COLOR2, react2)
    pygame.display.flip()

    reloj.tick(FPS)
