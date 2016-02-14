# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""

class EtapeCtrl:

    def get_nombre_lancers(self,box):
        if box.plateau.auMoinsUnEstLeve(7,8,9):
            return 2
        else:
            while True:
                try:
                    nb_lancers = box.es.get_nombre_lancers()
                    if nb_lancers <= 2 and nb_lancers > 0:
                        return nb_lancers
                except ValueError:
                    pass

    def get_clapets_a_fermer(self,box):
        while True:
            clapets_a_fermer = box.es.get_clapets_a_fermer()
            if box.plateau.sont_tous_leves(clapets_a_fermer):
                return clapets_a_fermer

    def handle(self, box):
        nb_lancers = self.get_nombre_lancers(box)

        somme = box.die.lance(nb_lancers)
        box.es.notifie_resultat_de(somme)
        joueurBloque = box.plateau.est_bloque(somme) # True si le joueur est bloqué
        if joueurBloque:
            box.es.notifie_joueur_bloque()
            return joueurBloque

        box.plateau.ferme(self.get_clapets_a_fermer(box))

        return joueurBloque
