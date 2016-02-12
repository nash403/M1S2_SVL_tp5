# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""

class EtapeCtrl:

    # def peut_lancer_un_de(self):
    #    return not self.plateau.sontTousLeves(7,8,9)

    def handle(self, box):
        if box.plateau.auMoinsUnEstLeve(7, 8, 9):
            nb_lancers = 2
        else:
            saisie = False
            while not saisie:
                try:
                    nb_lancers = box.es.get_nombre_lancers()
                    if nb_lancers <= 2 and nb_lancers > 0:
                        saisie = True
                except ValueError:
                    pass

        somme = box.die.lance(nb_lancers)

        if not box.plateau.est_bloque(somme):
            return False

        box.es.notifie_resultat_des_et_choisir_clapets_a_fermer(somme)
        saisie = False

        while not saisie:
            clapets_a_fermer = box.es.get_clapets_a_fermer()
            if box.plateau.sontTousLeves(clapets_a_fermer):
                saisie = True



        box.plateau.ferme(clapets_a_fermer)

        return True
