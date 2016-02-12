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



# classe principale Box
# + Plateau
#   + Clapet
# + Die
# + ES

import unittest
from io import StringIO as sio
from mockito import *
from box import *

class TestBox(unittest.TestCase):

    def test_initialiser_partie(self):
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



    # def test_demander_saisie_nombre_de_des_renvoie_le_nombre_demande(self):
    #     plateau = mock()
    #     die = mock()
    #     es = mock()
    #     box = mock(plateau, die, es)
    #
    #     etapeCtrl = EtapeCtrl()
    #     etapeCtrl.
    #
    #
    #     SAISIE_USER = "2\n"
    #
    #     self.assertEqual(box.)
