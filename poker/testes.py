import unittest
from poker import *
from dados import *


class TestePoker(unittest.TestCase):

    def testPoker(self):
        self.assertEqual( poker([STRAIGHT1, FLUSH]), FLUSH)
        self.assertEqual(poker([STRAIGHT1, FLUSH, FULL_HOUSE]), FULL_HOUSE)

    def testRank_mao(self):
        self.assertEqual( rank_mao(FLUSH), 6)
        self.assertEqual(rank_mao(STRAIGHT_FLUSH), 9)
        self.assertEqual(rank_mao(QUADRA), 8)
        self.assertEqual(rank_mao(FULL_HOUSE), 7)
        self.assertEqual(rank_mao(STRAIGHT1), 5)

    def testPega_valores(self):
        self.assertEqual( pega_valores(STRAIGHT_FLUSH), [7,8,9,10,11]  )
        self.assertEqual(pega_valores(FLUSH), [1, 2, 4, 7, 11])


unittest.main()

