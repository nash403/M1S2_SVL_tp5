# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""

import unittest
from io import StringIO
from mockito import *
from tourCtrl import *
from es import *

class TestES(unittest.TestCase):

	def test_entree_retourne_la_saisie_valide(self):
		flot_entree = StringIO("1\n")
		flot_sortie = mock()
		es = EntreeSortie(flot_entree, flot_sortie)
		self.assertEqual(es.get_nombre_lancers(), 1)


	def test_entree_retourne_la_saisie_non_valide(self):
		flot_entree = StringIO("\n")
		flot_sortie = mock()
		es = EntreeSortie(flot_entree, flot_sortie)
		self.assertRaises(ValueError, es.get_nombre_lancers)

	def test_entree_retourne_la_saisie_errone(self):
		flot_entree = StringIO("texte\n")
		flot_sortie = mock()
		es = EntreeSortie(flot_entree, flot_sortie)
		self.assertRaises(ValueError, es.get_nombre_lancers)


	def test_notifie_vainqueur_par_ko(self):
		flot_entree = mock()
		flot_sortie = StringIO()
		es = EntreeSortie(flot_entree, flot_sortie)
		JOUEUR_VAINQUEUR = 'joueur1'
		es.notifie_vainqueur_par_ko(JOUEUR_VAINQUEUR)
		self.assertEqual(es.flot_sortie.getvalue(), 'joueur1 a gagné par ko')


	def test_notifie_vainqueur_par_score(self):
		flot_entree = mock()
		flot_sortie = StringIO()
		es = EntreeSortie(flot_entree, flot_sortie)
		SCORE_JOUEURS = {'joueur1':'18', 'joueur2':'20'}
		es.notifie_vainqueur_par_score(SCORE_JOUEURS)
		self.assertEqual(es.flot_sortie.getvalue(), 'joueur1 a gagné en ayant le moins de points')


