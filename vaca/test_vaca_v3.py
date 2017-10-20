import unittest
from vaca_v3 import *


class MeusTestes(unittest.TestCase):
    def testMover_vaca(self):
        # Vaca andando para frente (sem bater na parede)
        self.assertEqual(mover_vaca(Vaca(x=PAREDE_ESQUERDA, dx=3)), Vaca(x=PAREDE_ESQUERDA + 3, dx=3))
        self.assertEqual(mover_vaca(Vaca(LARGURA // 2, 3)), Vaca(LARGURA // 2 + 3, 3))

        # Vaca andando para tras (sem bater na parede)
        self.assertEqual(mover_vaca(Vaca(LARGURA // 2, -3)), Vaca(LARGURA // 2 - 3, -3))

        # Vaca no limite direito, e tendo que voltar
        self.assertEqual(mover_vaca(Vaca(PAREDE_DIREITA, 3)), Vaca(PAREDE_DIREITA - 3, -3))

        # Vaca no limite esquerdo, e tendo que voltar
        self.assertEqual(mover_vaca(Vaca(PAREDE_ESQUERDA, -3)), Vaca(PAREDE_ESQUERDA + 3, 3))

        # Vaca quase atingindo limite direito, e parando no limite
        self.assertEqual(mover_vaca(Vaca(PAREDE_DIREITA - 2, 3)), Vaca(PAREDE_DIREITA, 3))
        self.assertEqual(mover_vaca(Vaca(PAREDE_DIREITA - 1, 3)), Vaca(PAREDE_DIREITA, 3))

        # Vaca quase atingindo limite esquerdo, e parando no limite
        self.assertEqual(mover_vaca(Vaca(PAREDE_ESQUERDA + 2, -3)), Vaca(PAREDE_ESQUERDA, -3))
        self.assertEqual(mover_vaca(Vaca(PAREDE_ESQUERDA + 1, -3)), Vaca(PAREDE_ESQUERDA, -3))

    def testTrata_tecla(self):
        self.assertEqual(trata_tecla_vaca(Vaca(50, 3), pg.K_SPACE), Vaca(50, -3))
        self.assertEqual(trata_tecla_vaca(Vaca(100, -3), pg.K_SPACE), Vaca(100, 3))
        self.assertEqual(trata_tecla_vaca(Vaca(50, 3), pg.K_a), Vaca(50, 3))
        # self.assertNotEqual( trata_tecla(Vaca(100, -3), pg.K_a), Vaca(100, 3))

    def testMover_cc(self):
        # Chupacabra andando para frente (sem bater na parede)
        self.assertEqual(mover_cc(Chupacabra(X_CC,y=PAREDE_CIMA, dy=3)), Chupacabra(X_CC, y=PAREDE_CIMA + 3, dy=3))
        self.assertEqual(mover_cc(Chupacabra(X_CC, ALTURA // 2, 3)), Chupacabra(X_CC, ALTURA // 2 + 3, 3))

        # Chupacabra andando para tras (sem bater na parede)
        self.assertEqual(mover_cc(Chupacabra(X_CC, ALTURA // 2, -3)), Chupacabra(X_CC, ALTURA // 2 - 3, -3))

        # Chupacabra no limite direito, e tendo que voltar
        self.assertEqual(mover_cc(Chupacabra(X_CC, PAREDE_BAIXO, 3)), Chupacabra(X_CC, PAREDE_BAIXO - 3, -3))

        # Chupacabra no limite esquerdo, e tendo que voltar
        self.assertEqual(mover_cc(Chupacabra(X_CC, PAREDE_CIMA, -3)), Chupacabra(X_CC, PAREDE_CIMA + 3, 3))

        # Chupacabra quase atingindo limite direito, e parando no limite
        self.assertEqual(mover_cc(Chupacabra(X_CC, PAREDE_BAIXO - 2, 3)), Chupacabra(X_CC, PAREDE_BAIXO, 3))
        self.assertEqual(mover_cc(Chupacabra(X_CC, PAREDE_BAIXO - 1, 3)), Chupacabra(X_CC, PAREDE_BAIXO, 3))

        # Chupacabra quase atingindo limite esquerdo, e parando no limite
        self.assertEqual(mover_cc(Chupacabra(X_CC, PAREDE_CIMA + 2, -3)), Chupacabra(X_CC, PAREDE_CIMA, -3))
        self.assertEqual(mover_cc(Chupacabra(X_CC, PAREDE_CIMA + 1, -3)), Chupacabra(X_CC, PAREDE_CIMA, -3))




    def testDistancia(self):
        self.assertEqual(distancia(0, 4, 3, 0), 5)
        import math
        self.assertEqual(distancia(1, 2, 3, 4), math.sqrt((3 - 1) ** 2 + (4 - 2) ** 2))







    def testMover_jogo(self):
        self.assertEqual(mover_jogo(
                            Jogo(vaca=Vaca(PAREDE_ESQUERDA, 3),
                              chupacabra=Chupacabra(X_CC, PAREDE_CIMA, 3),
                              game_over=False)),
                         Jogo(vaca=Vaca(PAREDE_ESQUERDA + 3, 3),
                              chupacabra=Chupacabra(X_CC, PAREDE_CIMA + 3, 3),
                              game_over=False) )

        self.assertEqual(mover_jogo(
            Jogo(vaca=Vaca(X_CC, 3),
                 chupacabra=Chupacabra(X_CC, Y_VACA, 3),
                 game_over=False)),
            Jogo(vaca=Vaca(X_CC, 3),
                 chupacabra=Chupacabra(X_CC, Y_VACA, 3),
                 game_over=True))


    def testColidirem(self):
        self.assertFalse(colidirem(VACA_INICIAL, CC_INICIAL))
        self.assertTrue(colidirem(Vaca(X_CC, 3), Chupacabra(X_CC, Y_VACA, 3)))
        self.assertTrue(colidirem(
                        Vaca(X_CC, 3),
                        Chupacabra(X_CC, Y_VACA - IMG_VACA_INO.get_width()//2 + 3, 3)))
            # unittest.main()

