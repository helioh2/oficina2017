#!/usr/bin/env python
# -*- coding: utf-8 -*-


from universe import *


'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
tela = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_GATO = pg.image.load('cat1.png')    #os.path.join('', 'cat1.png'))
except:
    IMG_GATO = pg.Surface((100,100),pg.SRCALPHA)  #imagem vazia para o caso de nao funcionar o carregamento

Y = ALTURA//2 - IMG_GATO.get_height()//2


''' ##### Inicio das definições de dados ##### '''

'''
Gato é um Int positivo (>=0)
interp. coordenada x do gato na tela
Exemplos:
'''
GATO_INICIAL = 0
GATO_MEIO= LARGURA//2
GATO_FIM = LARGURA//2
'''Template para funcoes que recebem Gato:
def fn_para_gato(g):
    ... g    #faz algo com o g
'''

''' ##### Fim das definições de dados ##### '''


'''#### Inicio das funçeõs: #####'''

'''mover: Gato -> Gato'''
def mover(gato):
    return gato + 1

'''desenha: Gato -> Imagem'''
def desenha(gato):
    tela.blit(IMG_GATO, (gato, Y))


'''trata-tecla: Gato EventoTecla -> Gato'''
def trata_tecla(gato, tecla):
    if tecla == pg.K_SPACE:
        return 0
    else:
        return gato


def trata_mouse(gato, x, y, ev):
    if ev == pg.MOUSEBUTTONDOWN:
        return x
    else:
        return gato


def main(gato):
    big_bang(0, \
             tela=tela, frequencia=28, \
             quando_tick=mover, \
             desenhar=desenha, \
             quando_tecla=trata_tecla, \
             quando_mouse=trata_mouse)


# main(0)  #deixar comentado. excluir só quando chamar

