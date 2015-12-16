:BARA Salem|KHAMMAR Ahlam|Sasu Daniel

:date: 19 novembre 2015



###################################################################################################
###      		LA Baderne d'Apollonius fractale  				        ###
###################################################################################################
#### lancement et methodes utilisé  ######

Pour le projet, nous avons utilisé 2 différents modules dans le
dossier src:
    Fractales pour tout les cercles
    Interface_graphique qui dessinent les cercles grace a tkinter
    

Pour le lancer directement dans le terminal, on se place dans le dossier src et
on tape la commande suivante:
 python3 Interface_graphique.py N R

 N correspond aux nombres de cercles que nous voulons affichés
 R correspond au rayon du cercle
 
-->dans ces modules un cercle est représenté par un tuple de longueur 3,
   les deux premiers éléments sont les coordonnées du centre et le troisiéme c'est le rayon.

-->pour éviter des valeurs negatives dans les racineson a mis une translationmaximale qui correspond à la taille du canvas,
   en suite pour translater les dessins on fait une soustraction
-->pour sauvegarder les resultats on a utilisé un module PIL, ce module n'existe pas sur python 3,il faut l'installer

###################################################################################################
###      		presentation et fonctionnnement du programme  				###
###################################################################################################

Le but du projet est d’engendrer des dessins de fractales construits à partir de cercles tangents,
et de contrôler la génération de ces figures pour en explorer toutes les possibilités.
     ###  La technique de construction ###
     on peut partir d’un cercle centré à l’origine
     1-Etant donné un cercle et un entier n , disposer dans ce cercle une couronne de n*cercles, entourant un *n+1 ème cercle central.
	-on crée la couronne avec la fonction create_circles, et on cherche les triplets prodtuis avec all_triplets
     2-Etant donnés trois cercles tangents deux à deux, trouver le plus petit cercle tangents à ces cercles.
     3-construire une baderne d’Apollonius classique, la première récursivité
     4-reconstruire la baderne dans un cercle vides qu’il faut encore remplir.
     5-remplir chaque cercle vide créé à l’étape précédente par une nouvelle baderne,la deuxième récursivité.

###################################################################################################
###      		Les difficultés rencontées  						###
###################################################################################################
--> calculer le cercles de soddy,savoir si les cercles sont tengents interieurement ou exterieurement.
--> Trouver le point d'arret du dessin recusrsif.




