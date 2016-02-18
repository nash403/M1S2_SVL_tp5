Auteurs : Honoré Nintunze et Antonin Durey

TP réalisé sans problème particulier.

La classe Box est le coeur de l'application.
C'est la méthode joue de la classe Box qui fait tout (joue 10 tours pour chacun des 2 joueurs, sauf si l'un des 2 joueurs a fermé tous les clapets sur un seul tour)

La classe TourCtrl déroule un tour de jeu : plusieurs étapes jusqu'à être bloqué

La classe EtapeCtrl déroule une étape de jeu : un lancer de dé et fermeture des clapets voulus si on est pas bloqué

La classe Plateau stocke les informations du Plateau et permet de savoir si certains clapets sont levés/baissés...

La classe EntreeSortie gère les Entrées et Sorties du jeu

Ces 5 classes ont été testés

La classe Die représentant le lancer de dé n'a pas été testé car il ne s'agit que d'obtenir un nombre aléatoire entre 2 et 12 compris
La classe Clapet n'a pas été testé car elle ne contient que l'information représentant le fait qu'un clapet est levé/baissé


