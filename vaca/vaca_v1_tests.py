from vaca_v1 import *
import unittest

class MeusTestes(unittest.TestCase):
    def testAndar(self):
        # Vaca andando para frente (sem bater na parede)
        self.assertEqual(andar( Vaca(0,3) ), Vaca(3,3) )
        self.assertEqual(andar( Vaca(50, 3), Vaca(53,3)))

        # Vaca andando para tras (sem bater na parede)
        self.assertEqual(andar(Vaca(50, -3), Vaca(47, -3)))

        # Vaca no limite direito, e tendo que voltar
        self.assertEqual(andar( Vaca(LARGURA, 3), Vaca(LARGURA-3, -3)))

        # Vaca no limite esquerdo, e tendo que voltar
        self.assertEqual(andar( Vaca(0, -3), Vaca(3, 3) ))

        # Vaca quase atingindo limite direito, e parando no limite
        self.assertEqual(andar(Vaca(LARGURA-2, 3), Vaca(LARGURA, 3) ))
        self.assertEqual(andar(Vaca(LARGURA-1, 3), Vaca(LARGURA, 3)))

        # Vaca quase atingindo limite esquerdo, e parando no limite
        self.assertEqual(andar(Vaca(0 + 2, -3), Vaca(0, -3)))
        self.assertEqual(andar(Vaca(0 + 1, -3), Vaca(0, -3)))


# unittest.main()