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

PAREDE_CIMA = IMG_CC_INO.get_height()//2
PAREDE_BAIXO = ALTURA - IMG_CC_INO.get_height()//2


'''==================='''
'''# Definições de dados: '''

from namedlist import namedlist
Vaca = namedlist("Vaca", "x, dx")  #estrutura da Vaca

''' Vaca pode ser criada como: Vaca(Int[PAREDE_ESQUERDA,PAREDE_DIREITA], Int)
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

Chupacabra = namedlist("Chupacabra", "y, dy")  #estrutura do Chupacabra

''' Chupacabra pode ser criada como: Chupacabra(Int[PAREDE_CIMA, PAREDE_BAIXO], Int)
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

Jogo = namedlist("Jogo", "vaca, chupacabra, game_over")

''' Jogo eh criado como: Jogo(Vaca, Chupacabra, Boolean)
interp. Um jogo é composto por uma vaca, um chupacabra,
e uma flag (game_over) que indica se o jogo está acontecendo
ou nao
Exemplos:
'''
JOGO_INICIAL = Jogo(VACA_INICIAL, CC_INICIAL, False)
JOGO_GAME_OVER = Jogo(Vaca(X_CC, 3), Chupacabra(Y_VACA, 3), True)

'''Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.chupacabra
        jogo.game_over
'''




'''===================='''
''' Funções: '''

'''
mover_vaca: Vaca -> Vaca
Produz a próxima vaca (ou seja, fazer ela andar)
'''
def mover_vaca(vaca):
    if vaca.x < 0 or vaca.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        #calcula novo dx
        if (vaca.x == PAREDE_DIREITA and vaca.dx > 0) \
                or (vaca.x == PAREDE_ESQUERDA and vaca.dx < 0):  #se vaca bateu na parede
            vaca.dx = - vaca.dx
        #usar depurador (debugger)

        #calcula novo x
        vaca.x = vaca.x + vaca.dx

        if vaca.x > PAREDE_DIREITA:
            vaca.x = PAREDE_DIREITA
        elif vaca.x < PAREDE_ESQUERDA:
            vaca.x = PAREDE_ESQUERDA

        return vaca



'''
mover_cc: Chupacabra -> Chupacabra
Mover o chupacabra no eixo y usando o dy
'''
def mover_cc(chupacabra):
    if chupacabra.y < 0 or chupacabra.y > ALTURA:
        return "Erro: vaca invalida"
    else:
        #calcula novo dy
        if (chupacabra.y == PAREDE_BAIXO and chupacabra.dy > 0) \
                or (chupacabra.y == PAREDE_CIMA and chupacabra.dy < 0):  #se vaca bateu na parede
            chupacabra.dy = - chupacabra.dy
        #usar depurador (debugger)

        #calcula novo y
        chupacabra.y = chupacabra.y + chupacabra.dy

        if chupacabra.y > PAREDE_BAIXO:
            chupacabra.y = PAREDE_BAIXO
        elif chupacabra.y < PAREDE_CIMA:
            chupacabra.y = PAREDE_CIMA

        return chupacabra



'''
colidirem: Vaca, Chupacabra -> Boolean
Verifica se a vaca e o chupacabra colidiram
'''
def colidirem(vaca, chupacabra):
    raio1 = IMG_VACA_INO.get_width()
    raio2 = IMG_CC_VORTANO.get_width()
    if distancia(vaca.x, Y_VACA, X_CC, chupacabra.y) <= raio1 + raio2:
        return True
    #else
    return False


'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
!!!
'''
def mover_jogo(jogo):
    if not colidirem(jogo.vaca, jogo.chupacabra):
        jogo.vaca = mover_vaca(jogo.vaca)
        jogo.chupacabra = mover_cc(jogo.chupacabra)   # funcao auxiliar (helper)
    else:
        jogo.game_over = True
    return jogo


'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na tela
'''
def desenha_vaca(vaca):
    if vaca.dx < 0:
        TELA.blit(IMG_VACA_VORTANO,
                  (vaca.x - IMG_VACA_VORTANO.get_width() // 2,
                   Y_VACA - IMG_VACA_VORTANO.get_height() // 2))
    else:
        TELA.blit(IMG_VACA_INO,
                  (vaca.x - IMG_VACA_INO.get_width() // 2,
                   Y_VACA - IMG_VACA_INO.get_height() // 2))


'''
desenha_chupacabra: Chupacabra -> Imagem
Desenha o chupacabra
'''
def desenha_chupacabra(chupacabra):
    TELA.blit(IMG_CC_VORTANO,
              (X_CC - IMG_CC_VORTANO.get_width() // 2,
               chupacabra.y - IMG_CC_VORTANO.get_height() // 2))


'''
desenha_jogo: Jogo -> Imagem
Desenha o jogo
'''
def desenha_jogo(jogo):
    desenha_vaca(jogo.vaca)
    desenha_chupacabra(jogo.chupacabra)


'''
trata_tecla_vaca: Vaca, EventoTecla -> Vaca
Quando teclar espaço, inverte a direção da vaca
'''
def trata_tecla_vaca(vaca, tecla):
    if tecla == pg.K_SPACE:
        vaca.dx = - vaca.dx
    return vaca


'''
trata_tecla: Jogo, EventoTecla -> Jogo
Trata tecla geral
'''
def trata_tecla(jogo, tecla):
    jogo.vaca = trata_tecla_vaca(jogo.vaca, tecla)
    return jogo



''' ================= '''
''' Main (Big Bang):
'''

''' Jogo -> Jogo '''
''' inicie o mundo com main(JOGO_INICIAL) '''

def main(inic):
    big_bang(inic, tela=TELA,
             quando_tick=mover_jogo,
             desenhar=desenha_jogo,
             quando_tecla=trata_tecla)

# main(JOGO_INICIAL)

