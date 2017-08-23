import unittest


'''
Float -> Float
Retorna o dobro do valor
'''
##def dobro(n):
##    pass

def dobro(n):
    return n*2

class MeusTestes(unittest.TestCase):
    
    def testDobro(self):
        self.assertEqual(dobro(2), 4)
        self.assertEqual(dobro(0), 0)
        self.assertEqual(dobro(-1), -2)


    #...
    ''' <<template>>
    def test_<nome_funcao>(self):
        self.assertEqual(<chamada_da_funcao>, <resultado_esperado>)
    '''


# unittest.main()  #não excluir se rodar no idle. Tirar se rodar no Pycharm



'''
CorSemaforo -> CorSemaforo
Retorna a proxima cor do semaforo de acordo com a atual
'''
#stub:
def proxima_cor(cor):
    pass

#template:
'''
def fn_para_cor_semaforo(cor):
    if cor == "vermelho":
        ...
    elif cor == "amarelo":
        ...
    elif cor == "vermelho":
        ...  
'''    







