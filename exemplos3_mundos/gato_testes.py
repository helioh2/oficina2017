#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gato import *

import unittest

class MeusTestes(unittest.TestCase):
    def testMover(self):
        self.assertEqual(mover(2), 5)
        self.assertEqual(mover(100), 103)

    def testTrata_tecla(self):
        self.assertEqual(  trata_tecla(100, pg.K_SPACE), 0  )
        self.assertEqual(  trata_tecla(100, pg.K_a), 100)

    # ...
    ''' <<template>>
    def test_<nome_funcao>(self):
        self.assertEqual(<chamada_da_funcao>, <resultado_esperado>)
    '''


# unittest.main()

