
import unittest

''' PROBLEMA: faça uma função que, dado um numero,
retorne o dobro do numero '''

'''
dobro: Float -> Float
Recebe um numero e retorna o dobro
'''

# prototipo bobo (stub)
##def dobro(n):
##      pass

def dobro(n):
      return 2*n

###exemplos
##dobro(2)  #-> 4
##dobro(3)  # -> 6


class MeuTeste(unittest.TestCase):

      def testDobro(self):

            self.assertEqual( dobro(2.0), 2*2.0 )
            self.assertEqual( dobro(-1.5), 2*(-1.5) )


unittest.main()   # não excluir


