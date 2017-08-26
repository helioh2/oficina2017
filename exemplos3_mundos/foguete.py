#!/usr/bin/env python
# -*- coding: utf-8 -*-


from universe import *

''' Programa do Foguete '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (400, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_FOGUETE = pg.image.load('foguete.png')    #os.path.join('', 'cat1.png'))
except:
    IMG_FOGUETE = pg.Surface((100,100),pg.SRCALPHA)  #imagem vazia para o caso de nao funcionar o carregamento

#X = 200  #numero magico
X = LARGURA // 2

'''==================='''
'''# Definições de dados: '''

''' Foguete é Int[0,ALTURA] 
interp. representa a posicao y do foguete em pixels
Exemplos:
'''
F_INICIAL = 0
F_MEIO = ALTURA//2
F_FINAL = ALTURA
'''Template:
def fn_para_foguete(y):
    if y > ALTURA or y < 0:
        return "Foguete invalido"
    else:
        ... y
'''



'''===================='''
''' Funções: '''

'''
desce: Foguete -> Foguete
Faz o foguete descer 3 pixels no eixo y
!!!
'''
def desce(y):
    pass


'''
desenha: Foguete -> Imagem
Desenha...
!!!
'''
def desenha(y):
    pass


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

''' Foguete -> Foguete '''
''' inicie o mundo com main()'''
def main():
    big_bang(F_INICIAL, tela=TELA,
             quando_tick=desce, \
             desenhar=desenha)


main()
