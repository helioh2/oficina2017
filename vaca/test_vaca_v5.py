import unittest
from vaca_v5 import *


class MeusTestes(unittest.TestCase):
    def testMover_vaca_x(self):
        # Vaca andando para frente (sem bater na parede)
        self.assertEqual(mover_vaca_x(Vaca(PAREDE_ESQUERDA, 3, CHAO, 0)), Vaca(PAREDE_ESQUERDA + 3, 3, CHAO, 0))
        self.assertEqual(mover_vaca_x(Vaca(LARGURA // 2, 3, CHAO, 0)), Vaca(LARGURA // 2 + 3, 3, CHAO, 0))

        # Vaca andando para tras (sem bater na parede)
        self.assertEqual(mover_vaca_x(Vaca(LARGURA // 2, -3, CHAO, 0)), Vaca(LARGURA // 2 - 3, -3, CHAO, 0))

        # Vaca no limite direito, e tendo que voltar
        self.assertEqual(mover_vaca_x(Vaca(PAREDE_DIREITA, 3, CHAO, 0)), Vaca(PAREDE_DIREITA - 3, -3, CHAO, 0))

        # Vaca no limite esquerdo, e tendo que voltar
        self.assertEqual(mover_vaca_x(Vaca(PAREDE_ESQUERDA, -3, CHAO, 0)), Vaca(PAREDE_ESQUERDA + 3, 3, CHAO, 0))

        # Vaca quase atingindo limite direito, e parando no limite
        self.assertEqual(mover_vaca_x(Vaca(PAREDE_DIREITA - 2, 3, CHAO, 0)), Vaca(PAREDE_DIREITA, 3, CHAO, 0))
        self.assertEqual(mover_vaca_x(Vaca(PAREDE_DIREITA - 1, 3, CHAO, 0)), Vaca(PAREDE_DIREITA, 3, CHAO, 0))

        # Vaca quase atingindo limite esquerdo, e parando no limite
        self.assertEqual(mover_vaca_x(Vaca(PAREDE_ESQUERDA + 2, -3, CHAO, 0)), Vaca(PAREDE_ESQUERDA, -3, CHAO, 0))
        self.assertEqual(mover_vaca_x(Vaca(PAREDE_ESQUERDA + 1, -3, CHAO, 0)), Vaca(PAREDE_ESQUERDA, -3, CHAO, 0))

    def testMover_vaca_y(self):

        #QUEDA LIVRE
        self.assertEqual(mover_vaca_y(
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=60, dy=0)),
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=60+G, dy=G))
        self.assertEqual(mover_vaca_y(
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=(60 + G), dy=G)),
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=(60 + G) + G+G, dy=G+G))

        # JA ESTÁ NO CHAO
        self.assertEqual(mover_vaca_y(
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=CHAO, dy=0)),
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=CHAO, dy=0))

        # CHEGANDO NO CHAO
        self.assertEqual(mover_vaca_y(
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=CHAO-2*G, dy=3*G)),
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=CHAO, dy=0))
        self.assertEqual(mover_vaca_y(
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=CHAO - 3 * G, dy=3 * G)),
            Vaca(x=PAREDE_ESQUERDA, dx=0, y=CHAO, dy=0))

    def testTrata_tecla(self):
        self.assertEqual(trata_tecla_vaca(Vaca(50, 0, CHAO, 0), pg.K_LEFT), Vaca(50, -DX, CHAO, 0))
        self.assertEqual(trata_tecla_vaca(Vaca(50, 0,CHAO, 0), pg.K_RIGHT), Vaca(50, DX, CHAO, 0))
        # self.assertEqual(trata_tecla_vaca(Vaca(100, -3), pg.K_SPACE), Vaca(100, 3))
        self.assertEqual(trata_tecla_vaca(Vaca(50, 3, CHAO, 0), pg.K_a), Vaca(50, 3, CHAO, 0))
        # self.assertNotEqual( trata_tecla(Vaca(100, -3), pg.K_a), Vaca(100, 3))
        self.assertEqual(trata_tecla_vaca(Vaca(50, 0, CHAO, 0), pg.K_UP), Vaca(50, 0, CHAO-10, -20))

    def testTrataSoltaTecla(self):
        self.assertEqual(trata_solta_tecla_vaca(Vaca(50, -DX, CHAO, 0), pg.K_LEFT), Vaca(50, 0, CHAO, 0))
        self.assertEqual(trata_solta_tecla_vaca(Vaca(50, DX, CHAO, 0), pg.K_RIGHT), Vaca(50, 0, CHAO, 0))

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
                            Jogo(vaca=Vaca(PAREDE_ESQUERDA, 3, CHAO, 0),
                                 chupacabras=[Chupacabra(X_CC, PAREDE_CIMA, 3)],
                                 game_over=False)),
                         Jogo(vaca=Vaca(PAREDE_ESQUERDA + 3, 3, CHAO, 0),
                              chupacabras=[Chupacabra(X_CC, PAREDE_CIMA + 3, 3)],
                              game_over=False) )

        self.assertEqual(mover_jogo(
            Jogo(vaca=Vaca(X_CC, 3, CHAO, 0),
                 chupacabras=[Chupacabra(X_CC, CHAO, 3)],
                 game_over=False)),
            Jogo(vaca=Vaca(X_CC, 3, CHAO, 0),
                 chupacabras=[Chupacabra(X_CC, CHAO, 3)],
                 game_over=True))


    def testColidirem(self):
        self.assertFalse(colidirem(VACA_INICIAL, CC_INICIAL))
        self.assertTrue(colidirem(Vaca(X_CC, 3, CHAO, 0), Chupacabra(X_CC, CHAO, 3)))
        self.assertTrue(colidirem(
                        Vaca(X_CC, 3, CHAO, 0),
                        Chupacabra(X_CC, CHAO - IMG_VACA_INO.get_width() // 2 + 3, 3)))
            # unittest.main()

