# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""

# fonctionalites
# * jouer: appelle jouer un tour alternativement pour les 2 joueurs, jusqu'à 10 tours ou victoire de l'un des 2.
# * jouer un tour :
# - cas nominal: les clapets 7, 8, 9 sont ouvert: on lance 2 dés
#   + lancer de dé : on affiche la somme des dés, puis on affiche le plateau
#       = cas nominal: il est possible de fermer des clapets, on demande les clapet à fermer
#       = on ne peut pas fermer de clapet, on affiche le score, tour terminé.
#   + fermer clapet:
#       = cas nominal: le(s) clapet(s) est/sont ouvert(s) donc on le(s) ferme, on renvoie false si tous les clapets ne sont pas fermés, true sinon.
#       = un des clapet demandé est déjà femé, on renvoie un erreur
# - les calpets 7, 8 et 9 sont fermés : on demande combien de dés le joeur veut lancer
#   ici on a les 2 fonctionalites précédentes (lancer de dé et fermer clapet)



import unittest
from io import StringIO as sio
from mockito import *
from box import *

class TestBox(unittest.TestCase):

	def test_creer_une_box_initialise_la_partie(self):
		plateau = mock()
		die = mock()
		es = mock()
		tourCtrl = mock()
		box = Box(plateau, tourCtrl, die, es)

		JOUEUR_1 = "joueur1"
		JOUEUR_2 = "joueur2"
		self.assertEqual(box.joueur_courant, JOUEUR_1)
		self.assertEqual(box.get_score_joueur(JOUEUR_1), 0)
		self.assertEqual(box.get_score_joueur(JOUEUR_2), 0)

	def test_switch_player_change_de_joueur(self):
		plateau = mock()
		die = mock()
		es = mock()
		tourCtrl = mock()
		box = Box(plateau, tourCtrl, die, es)

		JOUEUR_1 = "joueur1"
		JOUEUR_2 = "joueur2"
		self.assertEqual(box.joueur_courant,JOUEUR_1)
		box.switch_player()
		self.assertEqual(box.joueur_courant,JOUEUR_2)
		box.switch_player()
		self.assertEqual(box.joueur_courant,JOUEUR_1)

	def test_incrementer_score_se_fait_correctement(self):
		plateau = mock()
		die = mock()
		es = mock()
		tourCtrl = mock()
		box = Box(plateau, tourCtrl, die, es)

		JOUEUR_1 = "joueur1"
		JOUEUR_2 = "joueur2"

		SCORE_A_AJOUTER_1 = 10
		SCORE_A_AJOUTER_2 = 14

		box.incremente_score(JOUEUR_1,SCORE_A_AJOUTER_1)
		box.incremente_score(JOUEUR_2,SCORE_A_AJOUTER_2)

		self.assertEqual(box.get_score_joueur(JOUEUR_1),SCORE_A_AJOUTER_1)
		self.assertEqual(box.get_score_joueur(JOUEUR_2),SCORE_A_AJOUTER_2)

		box.incremente_score(JOUEUR_1,SCORE_A_AJOUTER_2)
		box.incremente_score(JOUEUR_2,SCORE_A_AJOUTER_1)

		self.assertEqual(box.get_score_joueur(JOUEUR_1),SCORE_A_AJOUTER_1+SCORE_A_AJOUTER_2)
		self.assertEqual(box.get_score_joueur(JOUEUR_2),SCORE_A_AJOUTER_2+SCORE_A_AJOUTER_1)

	def test_incrementer_score_non_superieur_a_zero_genere_une_erreur(self):
		plateau = mock()
		die = mock()
		es = mock()
		tourCtrl = mock()
		box = Box(plateau, tourCtrl, die, es)

		JOUEUR_1 = "joueur1"

		SCORE_A_AJOUTER = -10

		self.assertRaises(ScoreFormatError, box.incremente_score,JOUEUR_1,SCORE_A_AJOUTER)

	def test_joue_notifie_vainqueur_apres_10_tour_de_jeu(self):
		plateau = mock()
		die = mock()
		es = mock()
		tourCtrl = mock()
		box = Box(plateau, tourCtrl, die, es)

		# tourCtrl.handle va retourner 10 fois False
		when(tourCtrl).handle(box).thenReturn(False)
		when(plateau).valeur_clapets_leves().thenReturn(1)

		box.joue()
		verify(tourCtrl,times=20).handle(box) # 10 pour chaque joueurs, donc 20 fois
		verify(es).notifie_vainqueur_par_score(box.score_joueurs)

	def test_joue_notifie_vainqueur_des_que_tous_les_clapets_sont_fermes(self):
		plateau = mock()
		die = mock()
		es = mock()
		tourCtrl = mock()
		box = Box(plateau, tourCtrl, die, es)
		JOUEUR_VAINQUEUR = 'joueur1'
		VALEUR_SANS_IMPORTANCE = 5
		# Dès son premier tour, le premier joueur arrive à tout fermer
		when(tourCtrl).handle(box).thenReturn(True)

		box.joue()
		verify(tourCtrl,times=1).handle(box)
		verify(es).notifie_vainqueur_par_ko(JOUEUR_VAINQUEUR)
