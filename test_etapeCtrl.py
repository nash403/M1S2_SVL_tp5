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

    def test_nb_lancers_si_clapet_7_8_9_pas_tous_baisses_egal_2(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau

        etapeCtrl = EtapeCtrl()

        when(plateau).auMoinsUnEstLeve(7, 8, 9).thenReturn(True)

        self.assertEqual(etapeCtrl.get_nombre_lancers(box),2)

    def test_nb_lancers_si_clapet_7_8_9_tous_baisses_egal_1_ou_2(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.es = es

        etapeCtrl = EtapeCtrl()

        VALEUR_SAISIE = 1

        when(plateau).auMoinsUnEstLeve(7, 8, 9).thenReturn(False)
        when(es).get_nombre_lancers().thenReturn(VALEUR_SAISIE)

        self.assertEqual(etapeCtrl.get_nombre_lancers(box),VALEUR_SAISIE)

    def test_nb_lancers_si_clapet_7_8_9_tous_baisses_egal_1_ou_2_et_on_redemande_tant_que_saisie_differente(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.es = es

        etapeCtrl = EtapeCtrl()

        VALEUR_SAISIE = 1
        MAUVAISE_SAISIE = 3

        when(plateau).auMoinsUnEstLeve(7, 8, 9).thenReturn(False)
        when(es).get_nombre_lancers().thenRaise(ValueError).thenReturn(MAUVAISE_SAISIE).thenReturn(VALEUR_SAISIE)

        self.assertEqual(etapeCtrl.get_nombre_lancers(box),VALEUR_SAISIE)

        verify(es,times=3).get_nombre_lancers()

    def test_get_clapet_a_fermer_redemande_tant_que_un_des_clapets_demandes_est_deja_baisse(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.es = es

        etapeCtrl = EtapeCtrl()

        CLAPETS_1 = [2,4]
        CLAPETS_2 = [3,3]
        CLAPETS_3 = [1,5]

        when(es).get_clapets_a_fermer().thenReturn(CLAPETS_1).thenReturn(CLAPETS_2).thenReturn(CLAPETS_3)
        when(plateau).sont_tous_leves(CLAPETS_1).thenReturn(False)
        when(plateau).sont_tous_leves(CLAPETS_2).thenReturn(False)
        when(plateau).sont_tous_leves(CLAPETS_3).thenReturn(True)

        self.assertEqual(etapeCtrl.get_clapets_a_fermer(box),CLAPETS_3)
        verify(es,times=3).get_clapets_a_fermer()
        verify(plateau).sont_tous_leves(CLAPETS_1)
        verify(plateau).sont_tous_leves(CLAPETS_2)
        verify(plateau).sont_tous_leves(CLAPETS_3)

    def test_si_le_joueur_n_est_pas_bloque_on_renvoie_False_et_on_a_ferme_les_clapets(self):
        plateau = mock()
        die = mock()
        es = mock()
        box = mock()

        box.plateau = plateau
        box.es = es
        box.die = die

        etapeCtrl = EtapeCtrl()

        CLAPETS_A_FERMER = [1,5]
        RESULTAT_DE = 6
        NB_LANCERS = 2

        when(plateau).auMoinsUnEstLeve(7,8,9).thenReturn(True)
        self.assertEqual(etapeCtrl.get_nombre_lancers(box),NB_LANCERS)
        when(die).lance(NB_LANCERS).thenReturn(RESULTAT_DE)
        when(plateau).est_bloque(RESULTAT_DE).thenReturn(False)
        when(es).get_clapets_a_fermer().thenReturn(CLAPETS_A_FERMER)
        when(plateau).sont_tous_leves(CLAPETS_A_FERMER).thenReturn(True)

        self.assertEqual(etapeCtrl.handle(box), False)

        verify(es).notifie_resultat_de(RESULTAT_DE)
        verify(plateau).ferme(CLAPETS_A_FERMER)
