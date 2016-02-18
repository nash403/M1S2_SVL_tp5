# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""


import sys

class EntreeSortie:

	def __init__(self, flot_entree=sys.stdin, flot_sortie=sys.stdout):
		self.flot_entree = flot_entree
		self.flot_sortie = flot_sortie

	def get_nombre_lancers(self):
		return int(self.flot_entree.readline())

	def notifie_vainqueur_par_ko(self, joueur):
		self.flot_sortie.write(joueur + ' a gagné par ko')


	def notifie_vainqueur_par_score(self, score_joueurs):
		keys = sorted(list(score_joueurs.keys()))
		score_gagnant = -1
		joueur_gagnant = None
		for joueur in keys:
			score_courant = score_joueurs[joueur]
			if score_gagnant == -1 or score_gagnant > score_courant:
				score_gagnant = score_courant
				joueur_gagnant = joueur
		self.flot_sortie.write(joueur_gagnant + ' a gagné en ayant le moins de points')

