# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""

class TourCtrl:

    def __init__(self, etapeCtrl):
        self.etapeCtrl = etapeCtrl

    def handle(self, box):
        box.plateau.reset()
        fin = False
        while not fin:
            fin = self.etapeCtrl.handle(box) # False si le tour n'est pas fini donc si on est pas bloqué
            if box.plateau.sont_tous_baisses():
                return True # jeu gagné
        return False # le tour est fini sans vainqueur
