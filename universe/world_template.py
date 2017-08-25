#!/usr/bin/env python
# -*- coding: utf-8 -*-


from universe import *

''' Meu programa mundo  (torne isto mais específico) '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

#(LARGURA, ALTURA) = (600, 400)
# tela = pg.display.set_mode((LARGURA, ALTURA))

# try:
#     IMG_GATO = pg.image.load('cat1.png')    #os.path.join('', 'cat1.png'))
# except:
#     IMG_GATO = pg.Surface((100,100),pg.SRCALPHA)  #imagem vazia para o caso de nao funcionar o carregamento


'''==================='''
'''# Definições de dados: '''

''' EstadoMundo é ... (dê um nome melhor para EstadoMundo) '''



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