import unittest
from foguete import *


class MeuTeste(unittest.TestCase):
    def testDesce(self):
        self.assertEqual( desce(0), 0+3)
        self.assertEqual( desce(ALTURA//2), ALTURA//2 + 3)
        self.assertEqual( desce(ALTURA), ALTURA)
        self.assertEqual( desce(ALTURA-2), ALTURA)
        self.assertEqual(desce(ALTURA-1), ALTURA)
        self.assertEqual(desce(ALTURA - 3), ALTURA)


# unittest.main()  # não excluir