from universe import *
import pygame as pg


# Preparacao da Tela:

(LARGURA, ALTURA) = (600, 400)
tela = pg.display.set_mode((LARGURA, ALTURA))

'''Gato eh inteiro '''
#exemplos:
GATO_INICIAL = 0
GATO_MEIO= LARGURA//2
GATO_FIM = LARGURA//2

IMG_GATO = pg.image.load("cat1.png")

Y = ALTURA//2


'''mover: Gato -> Gato'''
def mover(gato):
    return gato + 1

'''desenha: Gato -> Imagem'''
def desenha(gato):
    #pg.draw.circle(tela, (255, 0, 0), (gato, ALTURA // 2), 50)
    tela.blit(IMG_GATO, (gato, Y))


'''trata-tecla: Gato EventoTecla -> Gato'''
def trata_tecla(gato, tecla):
    if tecla == pg.K_SPACE:
        return 0
    else:
        return gato


def trata_mouse(gato, x, y):
    return x

big_bang(GATO_INICIAL, tela=tela, quando_tick=mover, frequencia=100, desenhar=desenha, quando_tecla=trata_tecla, quando_mouse=trata_mouse)
