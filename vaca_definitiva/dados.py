
from constantes import *

'''==================='''
'''# Definições de dados: '''

from namedlist import namedlist
Vaca = namedlist("Vaca", "x, dx, y, dy")  #estrutura da Vaca

''' Vaca pode ser criada como: Vaca(Int[PAREDE_ESQUERDA,PAREDE_DIREITA], Int)
interp.: representa a posicao x da vaca, e o deslocamento
a cada tick no eixo x, chamado de dx
Exemplos:
'''
VACA_INICIAL = Vaca(PAREDE_ESQUERDA, 0, 0, 0)
# VACA_MEIO = Vaca(LARGURA//2, 3)
VACA_FIM = Vaca(LARGURA, 3, CHAO, 0)
VACA_VIRANDO = Vaca(LARGURA, -3, CHAO, 0)
VACA_VOLTANDO = Vaca(LARGURA // 2, -3, CHAO, 0)
'''
Template para funções que recebem Vaca:
def fn_para_vaca(v):
    if v.x < 0 or v.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        ... v.x
            v.dx

'''

Chupacabra = namedlist("Chupacabra", "x, y, dy")  #estrutura do Chupacabra

''' Chupacabra pode ser criada como: Chupacabra(Int[PAREDE_ESQUERDA, PAREDE_DIREITA], Int[PAREDE_CIMA, PAREDE_BAIXO], Int)
interp.: representa a posicao x e y do chupacabra, e o deslocamento
a cada tick no eixo y, chamado de dy
Exemplos:
'''
CC_INICIAL = Chupacabra(X_CC, PAREDE_CIMA, 3)
CC_MEIO = Chupacabra(X_CC, ALTURA//2, 3)
CC_FIM = Chupacabra(X_CC, PAREDE_BAIXO, 3)
CC_VIRANDO = Chupacabra(X_CC, PAREDE_BAIXO, -3)
CC_VOLTANDO = Chupacabra(X_CC, ALTURA//2, -3)

CC2 = Chupacabra(int(LARGURA*0.75), ALTURA//2, 3)
CC3 = Chupacabra(LARGURA//4, PAREDE_BAIXO, 3)


'''
Template para funções que recebem Chupacabra:
def fn_para_cc(cc):
    if cc.y < 0 or cc.y > LARGURA:
        return "Erro: cc invalido"
    else:
        ... cc.y
            cc.dy
'''

Jogo = namedlist("Jogo", "vaca, chupacabras, game_over")

''' Jogo eh criado como: Jogo(Vaca, List<Chupacabra>, Boolean)
interp. Um jogo é composto por uma vaca, vários chupacabras,
e uma flag (game_over) que indica se o jogo está acontecendo
ou nao
Exemplos:
'''
JOGO_INICIAL0 = Jogo(VACA_INICIAL, [CC_INICIAL], False)
JOGO_GAME_OVER = Jogo(Vaca(X_CC, 3, CHAO, 0), [Chupacabra(X_CC, CHAO, 3)], True)

JOGO_INICIAL = Jogo(VACA_INICIAL, [CC2, CC_INICIAL, CC3], False)


'''Template para funcao que recebe Jogo:
def fn_para_jogo(jogo):
    ... jogo.vaca
        jogo.chupacabra
        jogo.game_over
'''