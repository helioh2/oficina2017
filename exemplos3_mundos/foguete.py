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
    IMG_FOGUETE = pg.transform.scale(IMG_FOGUETE, (75,120))
except:
    IMG_FOGUETE = pg.Surface((100,100),pg.SRCALPHA)  #imagem vazia para o caso de nao funcionar o carregamento


L_FOGUETE = IMG_FOGUETE.get_width()
A_FOGUETE = IMG_FOGUETE.get_height()

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
Faz o foguete descer 3 pixels no eixo y, se não estiver no chao
'''
def desce(y):
    if y > ALTURA or y < 0:
        return "Foguete invalido"
    else:
        if y < ALTURA - 3:
            return y + 3
        else:
            return ALTURA


'''
desenha: Foguete -> Imagem
Desenha foguete na tela
!!!
'''
def desenha(y):
    # pg.draw.circle(TELA, (134,171,34), (X, y), 20 )
    TELA.blit(IMG_FOGUETE, (X - L_FOGUETE//2, y - A_FOGUETE +35))


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
