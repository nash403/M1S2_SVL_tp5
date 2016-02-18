# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""

import unittest
from io import StringIO as sio
from mockito import *
from plateau import *

class TestPlateau(unittest.TestCase):
	def test_valeur_clapets_leves_egal_4(self):
		clapet1 = mock()
		clapet2 = mock()
		clapet3 = mock()
		clapet4 = mock()
		clapet5 = mock()
		clapet6 = mock()
		clapet7 = mock()
		clapet8 = mock()
		clapet9 = mock()

		clapet1.leve = True
		clapet2.leve = False
		clapet3.leve = True
		clapet4.leve = False
		clapet5.leve = False
		clapet6.leve = False
		clapet7.leve = False
		clapet8.leve = False
		clapet9.leve = False

		LISTE_CLAPETS = [clapet1, clapet2, clapet3, clapet4, clapet5, clapet6, clapet7, clapet8, clapet9]
		
		plateau = Plateau(LISTE_CLAPETS)
		self.assertEqual(plateau.valeur_clapets_leves(), 4)

	def test_clapets_ne_sont_pas_tous_baisses_donc_retourne_false(self):

		clapet1 = mock()
		clapet2 = mock()
		clapet3 = mock()
		clapet4 = mock()
		clapet5 = mock()
		clapet6 = mock()
		clapet7 = mock()
		clapet8 = mock()
		clapet9 = mock()

		clapet1.leve = True
		clapet2.leve = False
		clapet3.leve = True
		clapet4.leve = False
		clapet5.leve = False
		clapet6.leve = False
		clapet7.leve = False
		clapet8.leve = False
		clapet9.leve = False

		LISTE_CLAPETS = [clapet1, clapet2, clapet3, clapet4, clapet5, clapet6, clapet7, clapet8, clapet9]
		
		plateau = Plateau(LISTE_CLAPETS)
		self.assertEqual(plateau.sont_tous_baisses(), False)

	def test_clapets_sont_tous_baisses_donc_retourne_true(self):

		clapet1 = mock()
		clapet2 = mock()
		clapet3 = mock()
		clapet4 = mock()
		clapet5 = mock()
		clapet6 = mock()
		clapet7 = mock()
		clapet8 = mock()
		clapet9 = mock()

		clapet1.leve = False
		clapet2.leve = False
		clapet3.leve = False
		clapet4.leve = False
		clapet5.leve = False
		clapet6.leve = False
		clapet7.leve = False
		clapet8.leve = False
		clapet9.leve = False

		LISTE_CLAPETS = [clapet1, clapet2, clapet3, clapet4, clapet5, clapet6, clapet7, clapet8, clapet9]
		
		plateau = Plateau(LISTE_CLAPETS)
		self.assertEqual(plateau.sont_tous_baisses(), True)

	def test_clapets_sont_tous_leves_donc_retourne_true(self):

		clapet1 = mock()
		clapet2 = mock()
		clapet3 = mock()
		clapet4 = mock()
		clapet5 = mock()
		clapet6 = mock()
		clapet7 = mock()
		clapet8 = mock()
		clapet9 = mock()

		clapet1.leve = True
		clapet2.leve = False
		clapet3.leve = True
		clapet4.leve = False
		clapet5.leve = False
		clapet6.leve = False
		clapet7.leve = False
		clapet8.leve = False
		clapet9.leve = False

		LISTE_CLAPETS = [clapet1, clapet2, clapet3, clapet4, clapet5, clapet6, clapet7, clapet8, clapet9]
		LISTE_CLAPETS_LEVES = [1, 3]
		plateau = Plateau(LISTE_CLAPETS)
		self.assertEqual(plateau.sont_tous_leves(LISTE_CLAPETS_LEVES), True)

	def test_clapets_ne_sont_pas_tous_leves_donc_retourne_false(self):

		clapet1 = mock()
		clapet2 = mock()
		clapet3 = mock()
		clapet4 = mock()
		clapet5 = mock()
		clapet6 = mock()
		clapet7 = mock()
		clapet8 = mock()
		clapet9 = mock()

		clapet1.leve = True
		clapet2.leve = False
		clapet3.leve = True
		clapet4.leve = False
		clapet5.leve = False
		clapet6.leve = False
		clapet7.leve = False
		clapet8.leve = False
		clapet9.leve = False

		LISTE_CLAPETS = [clapet1, clapet2, clapet3, clapet4, clapet5, clapet6, clapet7, clapet8, clapet9]
		LISTE_CLAPETS_LEVES = [1, 2, 3]
		plateau = Plateau(LISTE_CLAPETS)
		self.assertEqual(plateau.sont_tous_leves(LISTE_CLAPETS_LEVES), False)

	def test_clapets_ne_sont_pas_tous_leves_donc_retourne_false(self):

		clapet1 = mock()
		clapet2 = mock()
		clapet3 = mock()
		clapet4 = mock()
		clapet5 = mock()
		clapet6 = mock()
		clapet7 = mock()
		clapet8 = mock()
		clapet9 = mock()

		clapet1.leve = True
		clapet2.leve = False
		clapet3.leve = True
		clapet4.leve = False
		clapet5.leve = False
		clapet6.leve = False
		clapet7.leve = False
		clapet8.leve = False
		clapet9.leve = False

		LISTE_CLAPETS = [clapet1, clapet2, clapet3, clapet4, clapet5, clapet6, clapet7, clapet8, clapet9]
		CLAPETS_A_FERMER = [1, 3]

		plateau = Plateau(LISTE_CLAPETS)
		plateau.ferme(CLAPETS_A_FERMER)

		self.assertEqual(clapet1.leve, False)
		self.assertEqual(clapet3.leve, False)


	def test_peut_encore_jouer_donc_return_false(self):

		clapet1 = mock()
		clapet2 = mock()
		clapet3 = mock()
		clapet4 = mock()
		clapet5 = mock()
		clapet6 = mock()
		clapet7 = mock()
		clapet8 = mock()
		clapet9 = mock()

		clapet1.leve = True
		clapet2.leve = False
		clapet3.leve = True
		clapet4.leve = True
		clapet5.leve = False
		clapet6.leve = False
		clapet7.leve = False
		clapet8.leve = False
		clapet9.leve = False

		LISTE_CLAPETS = [clapet1, clapet2, clapet3, clapet4, clapet5, clapet6, clapet7, clapet8, clapet9]
		SOMME = 5
		
		plateau = Plateau(LISTE_CLAPETS)

		self.assertEqual(plateau.est_bloque(SOMME), False)

	def test_ne_peut_plus_jouer_donc_return_true(self):

		clapet1 = mock()
		clapet2 = mock()
		clapet3 = mock()
		clapet4 = mock()
		clapet5 = mock()
		clapet6 = mock()
		clapet7 = mock()
		clapet8 = mock()
		clapet9 = mock()

		clapet1.leve = True
		clapet2.leve = False
		clapet3.leve = True
		clapet4.leve = False
		clapet5.leve = False
		clapet6.leve = False
		clapet7.leve = False
		clapet8.leve = False
		clapet9.leve = False

		LISTE_CLAPETS = [clapet1, clapet2, clapet3, clapet4, clapet5, clapet6, clapet7, clapet8, clapet9]
		SOMME = 5
		
		plateau = Plateau(LISTE_CLAPETS)

		self.assertEqual(plateau.est_bloque(SOMME), True)


