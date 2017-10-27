
import unittest

from universe.universe import *

# Preparacao da Tela:

(LARGURA, ALTURA) = (100, 100)
tela = pg.display.set_mode((LARGURA, ALTURA))

'''DEFINIÇÕES DE DADOS:'''

'''
ContagemRegressiva é um Int[0, 10]
interp.: o numero de segundos faltantes
Exemplos:
'''
C1 = 10  #inicio
C2 = 5  #meio
C3 = 0  #fim
'''Template de funcoes que recebem ContagemRegressiva:
def fn_para_contagem_regressiva(cont):
    ... cont    #faz algo com cont
'''


'''FUNÇÕES:'''

'''tick: ContagemRegressiva -> ContagemRegressiva
Diminui contagem regressiva até o zero
'''
def tick(cr):
    if cr > 0:
        cr -= 1
    return cr


'''desenha_contagem: ContagemRegressiva -> Imagem
'''

def desenha_contagem(cr):
    fonte = pg.font.SysFont("monospace", 40)
    ## render: String, Int, Cor
    if cr > 0:
        texto = fonte.render(str(cr), 1, (255, 0, 0))
    else:
        texto = fonte.render("FIM!", 1, (255, 0, 0))

    ## blit: String, (Int, Int)
    tela.blit(texto, (10, ALTURA//2 - 20))


def trata_tecla(cr, tecla):
    if tecla == pg.K_SPACE:
        return 10
    else:
        return cr


'''main: ContagemRegressiva -> ContagemRegressiva'''
def main(cr):
    big_bang(cr,tela=tela,\
             quando_tick=tick,\
             desenhar=desenha_contagem,\
             frequencia=1,
             quando_tecla=trata_tecla)



class MeusTestes(unittest.TestCase):
    def testTick(self):
        self.assertEqual(tick(10), 9)
        self.assertEqual(tick(1), 0)
        self.assertEqual(tick(0), 0)


main(10)