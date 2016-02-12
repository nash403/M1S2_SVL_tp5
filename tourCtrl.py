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
            if box.plateau.sont_tous_baisses():
                return True # jeu gagné
            else:
                self.etapeCtrl.handle(box)
                #if
