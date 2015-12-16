#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`Soddy` module

:author: BARA Salem_KHAMMAR Ahlam_SASU Daniel

:date: decembre 2015
find the coordinates and radius of circles

in this module a circle is represented by
a tuple of length 3, the first two elements
are the coordinates of the center and the third is the radius

"""

#   dans ce module un cercle est représenté par
#un tuple de longueur 3, les deux premiers éléments
#sont les coordonnées du centre et le troisiéme c'est le rayon

import os
from math import *
import cmath
import sys
import random
sys.setrecursionlimit(50000)

#   pour éviter des valeurs negatives dans les racines
#on a mis une translation maximale qui correspond à la taille du canvas
#en suite pour translater les dessins on fait une soustraction
T=(900,600) # translation 

def create_cercles(cercle,N):
    """
    give the new crown 
    
    :param centre: circles which given the crown 
    :type centre: tuple
    :param N: number of circles inside
    :type N: int
    :return: a list of all circles of the crown
    :rtype: list
    :UC: N >=2
    
    """
    assert(N>2),"number of circles can't be less then 2"
    R=cercle[2]
    # calcule du rayon du petit cercle au milieu
    r=R*((1-sin(pi/N))/(1+sin(pi/N)))
    # les rayons des autres cercles tengents
    r1=R*((sin(pi/N))/(1+sin(pi/N)))
    # commencer à dessiner
    # recupérer tous les cercles tengents
    list_cercles=[]
    # le grand cercle
    list_cercles.append((cercle[0]+T[0],cercle[1]+T[1],R))
    # le cercle du milieu
    list_cercles.append((cercle[0]+T[0],cercle[1]+T[1],r))
    for i in range(0,N):
        new_centre= ((r + r1) * cos((2*i*pi)/N),(r + r1) * sin((2*i*pi)/N))
        # les autres cercles
        list_cercles.append((new_centre[0]+T[0],new_centre[1]+T[1],r1))
    return list_cercles


#########################################################################
###                 creation de la couronne                           ###
#########################################################################


def all_triplets(couronne):
    
    """
    give the list of all triplets from a crown
    
    :param centre: list of circles which forms crown
    :type centre: list
    :return: a list of all triplets
    :rtype: list
    :UC: None
    
    """
    triplets=[]
    list_ten=couronne[1:]
    for i in range(0,len(list_ten)-2):
        triplets.append([list_ten[0],list_ten[i+1],list_ten[i+2]])
        triplets.append([couronne[0],list_ten[i+1],list_ten[i+2]])
    # n'oublions pas le dernier cercle avec le premier
    triplets.append([list_ten[0],list_ten[-1],list_ten[1]])
    triplets.append([couronne[0],list_ten[-1],list_ten[1]])
    return triplets

########################################################################
####                  le calcule mathematique                       ####
########################################################################

def Distance(z1,z2):
    """
    calculates the distance for two points

    :param z1: first point  
    :type z1: complex
    :param z2: second point  
    :type z2: complex
    :return:  distance
    :rtype: int
    :UC:
    """	
    x1=z1.real
    x2=z2.real
    y1=z1.imag
    y2=z2.imag
    return sqrt((y2-y1)**2+(x2-x1)**2)

def cercle_soddy(triplet):
    """
    Calculates the radius of the circle and the center of Soddy , taking in parameter triplet

    :param triplet: list of three circles (triplets)
    :type triplet: list
    :return: circle
    :rtype: tuple
    :UC:
    """
    
    # on récupére les centres des trois cercles
    # on calcule le centre du cercle de soddy sous forme d'un complexe z4
    k1=1/triplet[0][2]
    k2=1/triplet[1][2] 
    k3=1/triplet[2][2] 
    k4=(k1+k2+k3)+(2*sqrt((k1*k2)+(k1*k3)+(k2*k3)))
    z1=complex(triplet[0][0], triplet[0][1])
    z2=complex(triplet[1][0], triplet[1][1])
    z3=complex(triplet[2][0], triplet[2][1])
    z4=(z1*k1+z2*k2+z3*k3+2*cmath.sqrt(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
    # la condition verifie si la distance entre deux cercles est egale à la somme des deux rayons
    if  int(Distance(z4,z1))==int((triplet[0][2]+1/k4)) and int(Distance(z4,z2))==int((triplet[1][2]+1/k4)) and int(Distance(z4,z3))==int((triplet[2][2]+1/k4)):
        return (z4.real,z4.imag,1/k4)
    else:
        k1=-1/triplet[0][2]   # la courbure du cercle qui contient les autres est negative
        k4=(k1+k2+k3)+(2*sqrt((k1*k2)+(k1*k3)+(k2*k3)))
        z4=(z1*k1+z2*k2+z3*k3+2*cmath.sqrt(k1*k2*z1*z2+k2*k3*z2*z3+k1*k3*z1*z3))/k4
        return (z4.real,z4.imag,1/k4)    
        

######################################################################################
###             chercher tous les cercles de soddy de la couronne                 ####
######################################################################################
def give_new_triplet(c1,c2,c3,c4):
    
    """
    Take in parameter three circles and a circle of Soddy and will return a new list of triplet.
    
    :param c1: circle of Soddy
    :type c1: triplet
    :param c2,c3,c4: circles tangents
    :type c2,c3,c4: triplet
    :return: new list of triplets
    :rtype: list
    """
    new=[]
    new.append([c1,c2,c3])
    new.append([c1,c2,c4])
    new.append([c2,c3,c4])
    return new
    
def all_circles_soddy(list_triplet):
    # cette fontion prend une liste de triplets et donne le cercle de soddy de chaque triplet
    # et la nouvelle liste de triplet
    """
    give all circles of soddy to one circle

    :param list_triplet: list of all_triplets 
    :type list_triplet: list
    :return: list of all circles of soddy and list of all new triplets
    :rtype: dict
    :UC:
    """
    
    all_soddy=[]        # tous les nouveaux cercles de soddy
    get_tri=[]          #les nouveaux triplets
    for i in list_triplet:
        if cercle_soddy(i)[2]>=2:       # on rajoute que les cercles de rayon plus grand que 1
            all_soddy.append(cercle_soddy(i))
            get_tri+=give_new_triplet(i[0],cercle_soddy(i),i[1],i[2])
    return {'soddy':all_soddy,'new_triplets':get_tri}
    

def new_draw(list_triplet):
    """
    This function takes a crown and returns all circles to draw inside the circles 

    :param list_triplet:  list of triplets
    :type l : list
    :return: list of new circles to draw
    :rtype: list
    """
    l = all_circles_soddy(list_triplet)['soddy']
    if l==[]:
        return []
    else:
        return l+new_draw(all_circles_soddy(list_triplet)['new_triplets'])

    
#################################################################################
###                 dessiner dans les cercles vides                         #####
#################################################################################

def draw_empty_circles(list_circles,n_circle):
    """
    draw in empty circle

    :param list_circles: a list of circles
    :type: list
    :param n_circle: number of circles in the crown
    :type: int
    :return: new list of circles
    :rtype: list
    """	
    k=[]
    for cer in list_circles:
        if cer[2]>=2:
            #n'oublions pas de mettre à jour la translation
            inter_x=cer[0]-T[0]
            inter_y=cer[1]-T[1]
            create_new=create_cercles(cer,n_circle)
            create_new[0]=(0+T[0],0+T[1],create_new[0][2])
            create_new[1]=(0+T[0],0+T[1],create_new[1][2])
            h=all_triplets(create_new)
            s=new_draw(h)
            for i in create_new[1:]:
                k.append((i[0]+inter_x,i[1]+inter_y,i[2]))
            for v in s:
                k.append((v[0]+inter_x,v[1]+inter_y,v[2]))
    return k
def recursif_two(liste,n_circle,n=0):
    """
    draw in all empty circles

    :param liste: list of circles
    :type: list
    :param n_circle: number of circles
    :type: int
    :return: new list of circles 
    """
    draw=draw_empty_circles(liste,n_circle)
    if n>=3:
        return []
    else:
        return draw+recursif_two(draw,n_circle,n+1)
    
if __name__ == '__main__':
    pass         
    
    
    
    
    
    
