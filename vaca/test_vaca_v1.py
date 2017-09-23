import unittest
from vaca_v1 import *


class MeusTestes(unittest.TestCase):
    def testAndar(self):
        # Vaca andando para frente (sem bater na parede)
        self.assertEqual( andar( Vaca(x=PAREDE_ESQUERDA, dx=3) ), Vaca(x=PAREDE_ESQUERDA+3, dx=3) )
        self.assertEqual( andar( Vaca(LARGURA//2, 3) ), Vaca(LARGURA//2 + 3,3) )

        # Vaca andando para tras (sem bater na parede)
        self.assertEqual(andar(Vaca(LARGURA//2, -3)), Vaca(LARGURA//2-3, -3))

        # Vaca no limite direito, e tendo que voltar
        self.assertEqual( andar( Vaca(PAREDE_DIREITA, 3)), Vaca(PAREDE_DIREITA-3, -3))

        # Vaca no limite esquerdo, e tendo que voltar
        self.assertEqual(andar( Vaca(PAREDE_ESQUERDA, -3) ), Vaca(PAREDE_ESQUERDA+3, 3) )

        # Vaca quase atingindo limite direito, e parando no limite
        self.assertEqual( andar(Vaca(PAREDE_DIREITA-2, 3) ), Vaca(PAREDE_DIREITA, 3) )
        self.assertEqual( andar(Vaca(PAREDE_DIREITA-1, 3) ), Vaca(PAREDE_DIREITA, 3))

        # Vaca quase atingindo limite esquerdo, e parando no limite
        self.assertEqual(andar(Vaca(PAREDE_ESQUERDA + 2, -3) ), Vaca(PAREDE_ESQUERDA, -3))
        self.assertEqual(andar(Vaca(PAREDE_ESQUERDA + 1, -3) ), Vaca(PAREDE_ESQUERDA, -3))

    def testTrata_tecla(self):
        self.assertEqual(trata_tecla(Vaca(50,3), pg.K_SPACE) , Vaca(50, -3) )
        self.assertEqual(trata_tecla(Vaca(100, -3), pg.K_SPACE), Vaca(100, 3))
        self.assertEqual(trata_tecla(Vaca(50, 3), pg.K_a), Vaca(50, 3))
        # self.assertNotEqual( trata_tecla(Vaca(100, -3), pg.K_a), Vaca(100, 3))

# unittest.main()