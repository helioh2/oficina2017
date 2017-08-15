import unittest

''' ##### Inicio das definições de dados ##### '''

'''
Velocidade é um Float
interp.: velocidade de um automóvel em km/h
Exemplos:
'''
V_PARADO = 0.0
V_NO_LIMITE = 80.0
V_CORRENDO_QUE_NEM_DOIDO = 160.0

'''Tempĺate p/ funcao que recebe uma Velocidade:
def fn_para_velocidade(v):
    ... v  #faz alguma coisa com v
'''

'''
Tempo é um Int positivo (>=0)
interp.: contagem em segundos desde o inicio do jogo
Exemplos:
'''
T_INICIAL = 0
T_ATUAL = 100

'''Tempĺate p/ funcao que recebe um Tempo:
def fn_para_tempo(t):
    ... t  #faz alguma coisa com t
'''

'''
Distancia é um Float
interp.: distancia em km
Exemplos:
'''
D_NAO_ANDOU = 0.0
D_PERTO = 2.0
D_LONGE = 60.0

'''Tempĺate p/ funcao que recebe uma Distancia:
def fn_para_distancia(d):
    ... d  #faz alguma coisa com d
'''

''' ##### Fim das definições de dados ##### '''


''' #### Inicio das funcoes ##### '''

'''
calcula_distancia: Velocidade, Tempo -> Distancia
Calcula a distancia percorrida dada a velocidade e o tempo
'''
##
##def calcula_distancia(v,t):
##    pass

def calcula_distancia(v,t):
    return v * (t / 3600)


'''
distancia_meia_hora: Velocidade -> Distancia
Calcula distancia percorrida a uma velocidade dada por 30 minutos
'''

##def distancia_meia_hora(v):
##    pass

'''Template utilizado:
def fn_para_velocidade(v):
    ... v  #faz alguma coisa com v
'''

def distancia_meia_hora(v):
    return calcula_distancia(v, 30*60)
    

''' #### Fim das funcoes ##### '''



''' #### Inicio dos testes ##### '''

class Test(unittest.TestCase):

    def testCalcula_distancia(self):
        self.assertEqual( calcula_distancia(20,5*3600), 100 )
        self.assertEqual( calcula_distancia(30,10*3600), 300 )

    def testDistancia_meia_hora(self):
        self.assertEqual( distancia_meia_hora(80), 40 )
        self.assertEqual( distancia_meia_hora(120), 60 )


unittest.main()  #não excluir

''' #### Fim dos testes ##### '''
