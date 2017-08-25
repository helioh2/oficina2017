from universe import *
import pygame as pg


# Preparacao da Tela:

(LARGURA, ALTURA) = (600, 400)
tela = pg.display.set_mode((LARGURA, ALTURA))

'''Vaca
Cria-se uma Vaca do seguinte modo: Vaca(Int, Int)
'''
class Vaca:
    def __init__(self, x, dx):
        self.x = x
        self.dx = dx

#exemplos:
VACA_INICIAL = Vaca(0, 10)


IMG_VACA = pg.image.load("vaca.png")
LARGURA_VACA = IMG_VACA.get_width()
ALTURA_VACA = IMG_VACA.get_height()
Y = ALTURA//2


'''mover: Vaca -> Vaca'''
def mover(vaca):
    if vaca.x > LARGURA - (LARGURA_VACA//2):
        vaca.dx = -vaca.dx
        vaca.x = LARGURA - (LARGURA_VACA//2)
    elif vaca.x < 0 + (LARGURA_VACA//2):
        vaca.dx = -vaca.dx
        vaca.x = (LARGURA_VACA//2)
    vaca.x += vaca.dx
    return vaca

'''desenha: Vaca -> Imagem'''
def desenha(vaca):
    #pg.draw.circle(tela, (255, 0, 0), (gato, ALTURA // 2), 50)
    img = IMG_VACA if vaca.dx >= 0 else pg.transform.flip(IMG_VACA, True, False)
    tela.blit(img, (vaca.x - (LARGURA_VACA//2), Y))

    myfont = pg.font.SysFont("monospace", 15)
    label = myfont.render("x = "+str(vaca.x)+"; dx = "+str(vaca.dx), 1, (255, 0, 0))
    tela.blit(label, (100, 100))


'''trata-tecla: Vaca EventoTecla -> Vaca'''
def trata_tecla(vaca, tecla):
    if tecla == pg.K_SPACE:
        vaca.dx = -vaca.dx
    return vaca



big_bang(VACA_INICIAL, tela=tela, quando_tick=mover, desenhar=desenha, quando_tecla=trata_tecla)
