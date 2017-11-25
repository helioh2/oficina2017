import unittest
from poker import *
from dados import *


class TestePoker(unittest.TestCase):

    def testPoker(self):
        self.assertEqual(poker([straight_flush2, quadra1]), straight_flush2)
        self.assertEqual(poker([full_house1, quadra1]), quadra1)
        self.assertEqual(poker([straight_flush2, full_house1]), straight_flush2)
        # self.assertEqual(poker([straight_flush2, straight_flush2]), None)

        self.assertEqual(poker[(flush1, straigh1)], flush1)
        self.assertEqual(poker[(straigh1, um_par1)], straigh1)
        self.assertEqual(poker[(trinca1, doi_pares1)], trinca1)
        self.assertEqual(poker[(um_par1, doi_pares1)], doi_pares1)
        self.assertEqual(poker[(doi_pares1, flush1)], flush1)
        self.assertEqual(poker[(carta_alta1, um_par1)], um_par1)
        self.assertEqual(poker[(um_par1, carta_alta1)], um_par1)
        self.assertEqual(poker[(straight_flush2, trinca1)], straight_flush2)
        self.assertEqual(poker[(straight_flush2, carta_alta1)], straight_flush2)

    def testRank_mao(self):
        self.assertEqual( rank_mao(FLUSH), 6)
        self.assertEqual(rank_mao(STRAIGHT_FLUSH), 9)
        self.assertEqual(rank_mao(QUADRA), 8)
        self.assertEqual(rank_mao(FULL_HOUSE), 7)
        self.assertEqual(rank_mao(STRAIGHT1), 5)

    def testPega_valores(self):
        self.assertEqual( pega_valores(STRAIGHT_FLUSH), [7,8,9,10,11]  )
        self.assertEqual(pega_valores(FLUSH), [1, 2, 4, 7, 11])

    def testFlush(self):
        self.assertTrue(flush(['P','P','P','P','P']))
        self.assertFalse(flush(['P', 'P', 'P', 'P', 'O']))

    def testStraight(self):
        self.assertTrue(straight([13, 12, 11, 10, 9]))
        self.assertFalse(straight([13, 11, 11, 10, 9]))

    def testQuadra(self):
        self.assertTrue(mesmo_tipo([9, 9, 9, 9, 3], 4))
        self.assertFalse(mesmo_tipo([9, 9, 9, 8, 3], 4))
        self.assertFalse(mesmo_tipo([9, 9, 9, 3, 3], 4))

    def testTrinca(self):
        self.assertTrue(mesmo_tipo([9, 9, 9, 5, 3], 3))
        self.assertFalse(mesmo_tipo([9, 9, 2, 5, 3], 3))

    def testDoisPares(self):
        self.assertTrue(dois_pares([9,9,2,2,5]))
        self.assertFalse(dois_pares([9,9,2,4,5]))

    def testUmPar(self):
        self.assertTrue(mesmo_tipo([9,9,2,1,5], 2))
        self.assertFalse(mesmo_tipo([4,9,2,1,5], 2))



unittest.main()

