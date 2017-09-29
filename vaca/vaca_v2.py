#!/usr/bin/env python
# -*- coding: utf-8 -*-


from universe import *

''' Meu programa da vaquinha 2.0 (com um chupacabra) '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_VACA_INO = pg.image.load('vaca-ino.png')    #os.path.join('', 'cat1.png'))
    IMG_VACA_VORTANO = pg.transform.flip(IMG_VACA_INO, True, False)
    IMG_CC_VORTANO = pg.image.load('chupacabra.jpg')
    IMG_CC_INO = pg.transform.flip(IMG_CC_VORTANO, True, False)
except:
    IMG_VACA_INO = pg.Surface((100,100),pg.SRCALPHA)  #imagem vazia para o caso de nao funcionar o carregamento
    IMG_VACA_VORTANO = pg.Surface((100,100),pg.SRCALPHA)
    IMG_CC_VORTANO = pg.Surface((100,100),pg.SRCALPHA)
    IMG_CC_INO = pg.Surface((100,100),pg.SRCALPHA)
    print("ERRO: Imagens nao foram carregadas.")

Y_VACA = ALTURA // 2
X_CC = LARGURA // 2

PAREDE_ESQUERDA = 0 + IMG_VACA_INO.get_width()//2
PAREDE_DIREITA = LARGURA - IMG_VACA_INO.get_width()//2
PAREDE_CIMA = IMG_VACA_INO.get_height()//2
PAREDE_BAIXO = ALTURA - IMG_VACA_INO.get_height()//2


'''==================='''
'''# Definições de dados: '''

from namedlist import namedlist
Vaca = namedlist("Vaca", "x, dx")  #estrutura da Vaca

''' Vaca pode ser criada como: Vaca(Int[0,LARGURA], Int)
interp.: representa a posicao x da vaca, e o deslocamento
a cada tick no eixo x, chamado de dx
Exemplos:
'''
VACA_INICIAL = Vaca(PAREDE_ESQUERDA, 3)
# VACA_MEIO = Vaca(LARGURA//2, 3)
VACA_FIM = Vaca(LARGURA, 3)
VACA_VIRANDO = Vaca(LARGURA, -3)
VACA_VOLTANDO = Vaca(LARGURA//2, -3)
'''
Template para funções que recebem Vaca:
def fn_para_vaca(v):
    if v.x < 0 or v.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        ... v.x
            v.dx

'''

from namedlist import namedlist
Chupacabra = namedlist("Chupacabra", "y, dy")  #estrutura da Vaca

''' Chupacabra pode ser criada como: Chupacabra(Int[0,ALTURA], Int)
interp.: representa a posicao y do chupacabra, e o deslocamento
a cada tick no eixo y, chamado de dy
Exemplos:
'''
CC_INICIAL = Chupacabra(PAREDE_CIMA, 3)
CC_MEIO = Chupacabra(ALTURA//2, 3)
CC_FIM = Chupacabra(PAREDE_BAIXO, 3)
CC_VIRANDO = Chupacabra(PAREDE_BAIXO, -3)
CC_VOLTANDO = Chupacabra(ALTURA//2, -3)
'''
Template para funções que recebem Chupacabra:
def fn_para_cc(cc):
    if cc.y < 0 or cc.y > LARGURA:
        return "Erro: cc invalido"
    else:
        ... cc.y
            cc.dy
'''



'''===================='''
''' Funções: '''

'''
mover_vaca: Vaca -> Vaca
Produz a próxima vaca (ou seja, fazer ela andar)
'''
def mover_vaca(v):
    if v.x < 0 or v.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        #calcula novo dx
        if (v.x == PAREDE_DIREITA and v.dx > 0) \
                or (v.x == PAREDE_ESQUERDA and v.dx < 0):  #se vaca bateu na parede
            v.dx = - v.dx
        #usar depurador (debugger)

        #calcula novo x
        v.x = v.x + v.dx

        if v.x > PAREDE_DIREITA:
            v.x = PAREDE_DIREITA
        elif v.x < PAREDE_ESQUERDA:
            v.x = PAREDE_ESQUERDA

        return v



'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na tela
!!!
'''
def desenha_vaca(v):
    if v.dx < 0:
        TELA.blit(IMG_VACA_VORTANO,
                  (v.x - IMG_VACA_VORTANO.get_width() // 2,
                   Y_VACA - IMG_VACA_VORTANO.get_height() // 2))
    else:
        TELA.blit(IMG_VACA_INO,
                  (v.x - IMG_VACA_INO.get_width() // 2,
                   Y_VACA - IMG_VACA_INO.get_height() // 2))


'''
trata_tecla_vaca: Vaca, EventoTecla -> Vaca
Quando teclar espaço, inverte a direção da vaca
'''
def trata_tecla_vaca(v, tecla):
    if tecla == pg.K_SPACE:
        v.dx = - v.dx
    return v



''' ================= '''
''' Main (Big Bang):
'''

''' EstadoMundo -> EstadoMundo '''
''' inicie o mundo com main(VACA_INICIAL) '''

def main(inic):
    big_bang(inic, tela=TELA,
             quando_tick=mover_vaca,
             desenhar=desenha_vaca,
             quando_tecla=trata_tecla_vaca)

main(VACA_INICIAL)

