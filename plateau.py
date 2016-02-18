# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""



class Plateau:
	

	def __init__(self, liste_clapets):
		self.liste_clapets = liste_clapets

	def valeur_clapets_leves(self):
		valeur = 0		
		for i in range(len(self.liste_clapets)):
			clapet = self.liste_clapets[i]			
			if clapet.leve:
	 			valeur += i+1 # i+1 because list ind are from 0 to 8 but clapets values are from 1 to 9
		return valeur

	def sont_tous_baisses(self):
		for clapet in self.liste_clapets:
			if clapet.leve:
	 			return False
		return True

	def sont_tous_leves(self, liste_clapets_a_verifier):
		for i in liste_clapets_a_verifier:
			clapet = self.liste_clapets[i-1] # i-1 because clapet n°1 is at pos 0...
			if not clapet.leve:
	 			return False
		return True

	def ferme(self, liste_clapets_a_fermer):
		for i in liste_clapets_a_fermer:
			self.liste_clapets[i-1].leve = False # i-1 because clapet n°1 is at pos 0...

	def est_bloque(self, somme):
		for i in range(1, int(somme/2)):
			if self.liste_clapets[i-1].leve and self.liste_clapets[somme-i-1].leve: # i-1 because...
				return False
		return True
			
