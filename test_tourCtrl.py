# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""

import unittest
from io import StringIO as sio
from mockito import *
from tourCtrl import *

class TestTourCtrl(unittest.TestCase):


    def test_a_chaque_etape_on_baisse_clapet_jusque_victoire(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.die = die
        box.es = es

        etapeCtrl = mock()

        tourCtrl = TourCtrl(etapeCtrl)

        when(plateau).sont_tous_baisses().thenReturn(False).thenReturn(False).thenReturn(False).thenReturn(False).thenReturn(True)

        tourCtrl.handle(box)


        verify(etapeCtrl,times=5).handle(box)
