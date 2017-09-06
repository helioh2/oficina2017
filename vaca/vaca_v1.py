#!/usr/bin/env python
# -*- coding: utf-8 -*-


from universe import *

''' Meu programa da vaquinha 1.0 '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_VACA_INO = pg.image.load('vaca-ino.png')    #os.path.join('', 'cat1.png'))
    IMG_VACA_VORTANO = pg.transform.flip(IMG_VACA_INO, True, False)
except:
    IMG_VACA_INO = pg.Surface((100,100),pg.SRCALPHA)  #imagem vazia para o caso de nao funcionar o carregamento
    IMG_VACA_VORTANO = pg.Surface((100,100),pg.SRCALPHA)
    print("ERRO: Imagens nao foram carregadas.")


'''==================='''
'''# Definições de dados: '''

from collections import namedtuple
Vaca = namedtuple("Vaca", "x, dx")

''' Vaca pode ser criada como: Vaca(Int[0,LARGURA], Int)
interp.: representa a posicao a x da vaca, e o deslocamento
a cada tick no eixo x, chamado de dx
Exemplos:
'''
VACA_INICIAL = Vaca(0, 3)
VACA_MEIO = Vaca(LARGURA//2, 3)
VACA_FIM = Vaca(LARGURA, 3)
VACA_VIRANDO = Vaca(LARGURA, -3)
VACA_VOLTANDO = Vaca(LARGURA//2, -3)


'''===================='''
''' Funções: '''

'''
tock: EstadoMundo -> EstadoMundo
Produz o próximo ...
!!!
def tock(estado):
    pass
'''

'''
desenha: EstadoMundo -> Imagem
Desenha...
!!!
def desenha(estado):
    pass
'''

'''
trata_tecla: EstadoMundo, EventoTecla -> EstadoMundo
Quando teclar ... produz ... <apagar caso não precise usar>
!!!
Template:

def trata_tecla(estado, tecla):
    if tecla == pg.K_SPACE:
        ... estado
    else:
        ... estado
'''

'''
trata_mouse: EstadoMundo, Int, Int, EventoMouse -> EstadoMundo:
Quando fazer ... nas posições x y no mouse produz ...   <apagar caso não precise usar>
!!!
Template:

def trata_mouse(estado, x, y, ev):
    if ev == pg.MOUSEBUTTONDOWN:
        ... estado
    elif ev == pg.MOUSEBUTTONUP:
        ... estado
    elif ev == pg.MOUSEMOTION:
        ... estado
    else:
        ... estado

'''

''' ================= '''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com ... 
def main(inic):
    big_bang(inic, tela=tela, frequencia=XX, \
             quando_tick=tock, \
             desenhar=desenha, \
             quando_tecla=..., \
             quando_mouse=..., \
             parar_quando=...)           


'''