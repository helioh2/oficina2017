#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

'''DEFINICOES DE DADOS'''

'''
Velocidade é um Float (>=0)
interp. a velocidade em m/s
Exemplos:
'''
V_INICIAL = 0.0
V_ACELERANDO = 20.0
V_CORRENDO_FEITO_LOUCO = 160.0
''' Template de função que recebe Velocidade
def fn_para_velocidade(v):
    if type(v) is float and v >= 0:
       ... v   #faz alguma coisa com v
    else:
       return "dados invalidos"
'''

'''
Velocidade, Tempo -> Distancia
'''



'''
CorSemaforo é uma String, uma dessas:
- "vermelho"
- "amarelo"
- "verde"
interp. uma string representando a cor atual de um semaforo
dispensa exemplos
'''
'''
def fn_para_cor_semaforo(cs):
    if cs == "vermelho":
        ...
    elif cs == "amarelo":
        ...
    elif cs == "verde":
        ...
'''


'''
CorSemaforoMelhor é um desses:
- 1 (vermelho)
- 2 (amarelo)
- 3 (verde)
'''

'''
Passaro é um desses tipos:
    - False
    - Int (>=0)
interp. um passaro é False quando está morto (game over),
se for Int, é a posição y na tela.
exemplos:
'''
P_MORTO = False
P_MEIO_DA_TELA = 250
P_ENCIMA = 10
''' Template:
def fn_para_passaro(p):
   if not p:
       ...
   elif type(p) is int and p >= 0:
       ...
          
'''





'''FUNCOES:'''

'''
proxima_cor: CorSemaforo -> CorSemaforo
Recebe uma cor de semaforo e retorna a proxima
'''

##def proxima_cor(cs):
##    pass


def proxima_cor(cs):
    if cs == "vermelho":
        return "verde"
    elif cs == "amarelo":
        return "vermelho"
    elif cs == "verde":
        return "amarelo"










class Test(unittest.TestCase):
    def test_proxima_cor(self):
        self.assertEqual( proxima_cor("vermelho"), "verde")
        self.assertEqual(proxima_cor("verde"), "amarelo")
        self.assertEqual(proxima_cor("amarelo"), "vermelho")

    #...
''' <<template>>
def test_<nome_funcao>(self):
    self.assertEqual(<chamada_da_funcao>, <resultado_esperado>)
    self.assertEqual(<chamada_da_funcao>, <resultado_esperado>)
    ...
'''

unittest.main()  #não excluir
