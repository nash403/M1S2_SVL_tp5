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
#       = cas nominal: le(s) clapet(s) est/sont ouvert(s) donc on le(s) ferme.
#       = un des clapet demandé est déjà femé, on renvoie un erreur
# - les calpets 7, 8 et 9 sont fermés : on demande combien de dés le joeur veut lancer
#   ici on a les 2 fonctionalites précédentes (lancer de dé et fermer clapet)


class Box:

	def __init__(self, plateau, tourCtrl, die, es):
		self.plateau = plateau
		self.tourCtrl = tourCtrl
		self.die = die
		self.es = es
		self.init()


	def init(self):
		self.score_joueurs = {'joueur1':0, 'joueur2': 0}
		self.joueur_courant = "joueur1"

	def switch_player(self):
		if self.joueur_courant == "joueur1":
			self.joueur_courant = "joueur2"
		else:
			self.joueur_courant = "joueur1"

	def get_score_joueur(self,joueur):
		return self.score_joueurs[joueur]

	def incremente_score(self,joueur,points):
		if points <= 0:
			raise ScoreFormatError()
		self.score_joueurs[joueur] += points

	def joue(self):
		keys = list(self.score_joueurs.keys())
		for i in range(0,10):
			for joueur in keys:
				self.joueur_courant = joueur
				if self.tourCtrl.handle(self): # jeu terminé
					print(self.joueur_courant)
					self.es.notifie_vainqueur_par_ko(self.joueur_courant)
					return
				else:
					self.incremente_score(self.joueur_courant, self.plateau.valeur_clapets_leves())
		self.es.notifie_vainqueur_par_score(self.score_joueurs)


class ScoreFormatError(Exception):
	pass
