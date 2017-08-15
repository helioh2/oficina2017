import unittest

''' PROBLEMA: Fazer uma função que recebe uma palavra e pluraliza
a palavra. Ex: 'carro' -> 'carros'
'''

'''
plural: String -> String
Recebe uma palavra e retorna o plural dela
'''

##def plural(p):
##      pass

def plural(p):
      #return p + "s" if p[-1] != "s" else p
      if p[-1] == "s":
            return p
      else:
            return p + "s"



class MeuTeste(unittest.TestCase):

      def testPlural(self):

            self.assertEqual( plural('carro'), 'carros' )
            self.assertEqual( plural('casas'), 'casas' )
            self.assertEqual( plural('lápis'), 'lápis' )


unittest.main()   # não excluir



