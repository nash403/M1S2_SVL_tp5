# -*- coding: utf-8 -*-
"""
TP SVL jeu Canoga
Auteurs : Honore Nintunze et Antonin Durey
"""

import unittest
from io import StringIO as sio
from mockito import *
from etapeCtrl import *

class TestEtapeCtrl(unittest.TestCase):



    # def test_ne_peut_pas_lancer_un_de(self):
    #     plateau = mock()
    #     die = mock()
    #     es = mock()
    #     tourCtrl = mock()
    #     box = Box(plateau, tourCtrl, die, es)
    #
    #     # Il faut au moins un des clapets levé pour être obligé de lancer les 2 dés
    #     when(plateau).auMoinsUnEstLeve(7,8,9).thenReturn(True)
    #
    #     self.assertEqual(box.peut_lancer_un_de(), False)
    #
    # def test_peut_lancer_un_de(self):
    #     plateau = mock()
    #     die = mock()
    #     es = mock()
    #     tourCtrl = mock()
    #     box = Box(plateau, tourCtrl, die, es)
    #
    #     # Il faut au moins un des clapets levé pour être obligé de lancer les 2 dés
    #     when(plateau).auMoinsUnEstLeve(7, 8, 9).thenReturn(False)
    #
    #     self.assertEqual(box.peut_lancer_un_de(), True)



    def test_jouer_une_etape_2_des_on_ferme_les_clapets_demandes(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.die = die
        box.es = es

        etapeCtrl = EtapeCtrl()


        CLAPETS_A_FERMER = [3, 4]
        SOMME_DES = 7

        CLAPETS_TOUS_FERMES = False

        when(plateau).auMoinsUnEstLeve(7,8,9).thenReturn(True)
        when(die).lance(2).thenReturn(SOMME_DES)

        when(es).get_clapets_a_fermer().thenReturn(CLAPETS_A_FERMER)

        when(plateau).est_bloque(SOMME_DES).thenReturn(False);
        when(plateau).sontTousLeves(CLAPETS_A_FERMER).thenReturn(True)
        when(plateau).ferme(CLAPETS_A_FERMER).thenReturn(CLAPETS_TOUS_FERMES)

        etapeCtrl.handle(box)

        verify(es).notifie_resultat_des_et_choisir_clapets_a_fermer(SOMME_DES)
        verify(die).lance(2)
        verify(plateau).ferme(CLAPETS_A_FERMER)

    def test_jouer_une_etape_2_des_et_tous_les_clapets_sont_fermes(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.die = die
        box.es = es

        etapeCtrl = EtapeCtrl()

        CLAPETS_A_FERMER = [7]
        SOMME_DES = 7

        CLAPETS_TOUS_FERMES = True

        when(plateau).auMoinsUnEstLeve(7,8,9).thenReturn(True)
        when(die).lance(2).thenReturn(SOMME_DES)

        when(es).get_clapets_a_fermer().thenReturn(CLAPETS_A_FERMER)

        when(plateau).est_bloque(SOMME_DES).thenReturn(False);
        when(plateau).sontTousLeves(CLAPETS_A_FERMER).thenReturn(True)
        when(plateau).ferme(CLAPETS_A_FERMER).thenReturn(CLAPETS_TOUS_FERMES)

        etapeCtrl.handle(box)

        verify(es).notifie_resultat_des_et_choisir_clapets_a_fermer(SOMME_DES)
        verify(die).lance(2)
        verify(plateau).ferme(CLAPETS_A_FERMER)

    def test_jouer_une_etape_2_des_clapets_a_femer_non_conformes_une_fois(self):
        # On teste le cas où la première saisie est erroné, mais la seconde est bonne
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.die = die
        box.es = es

        etapeCtrl = EtapeCtrl()

        CLAPETS_A_FERMER_FAUX = [3,4]
        CLAPETS_A_FERMER_VRAI = [7]
        SOMME_DES = 7

        CLAPETS_TOUS_FERMES = True

        when(plateau).auMoinsUnEstLeve(7,8,9).thenReturn(True)
        when(die).lance(2).thenReturn(SOMME_DES)

        when(es).get_clapets_a_fermer().thenReturn(CLAPETS_A_FERMER_FAUX).thenReturn(CLAPETS_A_FERMER_VRAI)

        when(plateau).est_bloque(SOMME_DES).thenReturn(False);
        when(plateau).sontTousLeves(CLAPETS_A_FERMER_FAUX).thenReturn(False)
        when(plateau).sontTousLeves(CLAPETS_A_FERMER_VRAI).thenReturn(True)

        when(plateau).ferme(CLAPETS_A_FERMER_VRAI).thenReturn(CLAPETS_TOUS_FERMES)

        etapeCtrl.handle(box)

        verify(es).notifie_resultat_des_et_choisir_clapets_a_fermer(SOMME_DES)
        verify(die).lance(2)
        verify(plateau).ferme(CLAPETS_A_FERMER_VRAI)

    def test_jouer_une_etape_1_de_on_ferme_les_clapets_demandes(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.die = die
        box.es = es

        etapeCtrl = EtapeCtrl()

        CLAPETS_A_FERMER = [2, 1]
        SOMME_DES = 3
        NOMBRE_LANCERS_DES = 1

        CLAPETS_TOUS_FERMES = False

        when(plateau).auMoinsUnEstLeve(7,8,9).thenReturn(False)
        when(es).get_nombre_lancers().thenReturn(NOMBRE_LANCERS_DES)
        when(die).lance(NOMBRE_LANCERS_DES).thenReturn(SOMME_DES)

        when(es).get_clapets_a_fermer().thenReturn(CLAPETS_A_FERMER)

        when(plateau).est_bloque(SOMME_DES).thenReturn(False);
        when(plateau).sontTousLeves(CLAPETS_A_FERMER).thenReturn(True)
        when(plateau).ferme(CLAPETS_A_FERMER).thenReturn(CLAPETS_TOUS_FERMES)

        etapeCtrl.handle(box)

        verify(es).notifie_resultat_des_et_choisir_clapets_a_fermer(SOMME_DES)
        verify(die).lance(NOMBRE_LANCERS_DES)
        verify(plateau).ferme(CLAPETS_A_FERMER)

    def test_jouer_une_etape_nombre_de_faux_la_premiere_fois_puis_1_de_on_ferme_les_clapets_demandes(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.die = die
        box.es = es

        etapeCtrl = EtapeCtrl()

        CLAPETS_A_FERMER = [2, 1]
        SOMME_DES = 3
        NOMBRE_LANCERS_DES_FAUX = 5
        NOMBRE_LANCERS_DES_VRAI = 1

        CLAPETS_TOUS_FERMES = False

        when(plateau).auMoinsUnEstLeve(7,8,9).thenReturn(False)
        when(es).get_nombre_lancers().thenReturn(NOMBRE_LANCERS_DES_FAUX).thenReturn(NOMBRE_LANCERS_DES_VRAI)
        when(die).lance(NOMBRE_LANCERS_DES_VRAI).thenReturn(SOMME_DES)

        when(es).get_clapets_a_fermer().thenReturn(CLAPETS_A_FERMER)

        when(plateau).est_bloque(SOMME_DES).thenReturn(False);
        when(plateau).sontTousLeves(CLAPETS_A_FERMER).thenReturn(True)
        when(plateau).ferme(CLAPETS_A_FERMER).thenReturn(CLAPETS_TOUS_FERMES)

        etapeCtrl.handle(box)

        verify(es).notifie_resultat_des_et_choisir_clapets_a_fermer(SOMME_DES)
        verify(die).lance(NOMBRE_LANCERS_DES_VRAI)
        verify(plateau).ferme(CLAPETS_A_FERMER)

    def test_jouer_une_etape_nombre_de_pas_un_entier_la_premiere_fois_puis_1_de_on_ferme_les_clapets_demandes(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.die = die
        box.es = es

        etapeCtrl = EtapeCtrl()

        CLAPETS_A_FERMER = [2, 1]
        SOMME_DES = 3
        NOMBRE_LANCERS_DES_VRAI = 1

        CLAPETS_TOUS_FERMES = False

        when(plateau).auMoinsUnEstLeve(7,8,9).thenReturn(False)
        when(es).get_nombre_lancers().thenRaise(ValueError).thenReturn(NOMBRE_LANCERS_DES_VRAI)
        when(die).lance(NOMBRE_LANCERS_DES_VRAI).thenReturn(SOMME_DES)

        when(es).get_clapets_a_fermer().thenReturn(CLAPETS_A_FERMER)

        when(plateau).est_bloque(SOMME_DES).thenReturn(False);
        when(plateau).sontTousLeves(CLAPETS_A_FERMER).thenReturn(True)
        when(plateau).ferme(CLAPETS_A_FERMER).thenReturn(CLAPETS_TOUS_FERMES)

        etapeCtrl.handle(box)

        verify(es).notifie_resultat_des_et_choisir_clapets_a_fermer(SOMME_DES)
        verify(die).lance(NOMBRE_LANCERS_DES_VRAI)
        verify(plateau).ferme(CLAPETS_A_FERMER)
