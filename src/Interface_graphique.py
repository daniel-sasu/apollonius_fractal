#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`Graphical` module

:author: BARA Salem_KHAMMAR Ahlam_SASU Daniel

:date: decembre, 2015

module that manages the drawing

"""
import os
from tkinter import *
from math import *
import sys
from Fractales import *
import random
#####################################################################
###      lancement en lignes de commandes                        ####
#####################################################################
list_data=sys.argv
if len(list_data)==1:
    #si y'a pas de parametre on demande d'entrer las données
    N=int(input('entrez un nombre svp'))
    R=int(input('entrez un rayon svp'))
    
else:
    N=int(list_data[1])  
    R=int(list_data[2])
l=create_cercles((0,0,R),N)  # création de la première couronne 
#####################################################################
####				Dessins 			 ####
#####################################################################

def dessiner_cercles(l,couleur):
    """
    Draw all circles wich given in l with translation
    
    :param l: list of all circles 
    :type l: list
    :param coleur: choice the color of the draw
    :type coleur: color
    :UC:
    """
    #on centre les dessins
    for i in l:
        cercle.create_oval(i[0]-i[2]-450,i[1]-i[2]-300,i[0]+i[2]-450,i[1]+i[2]-300,width=1,outline=couleur)
######################################################################
#####            on commence étape par étape                     #####
######################################################################
def step_1():
    """
    we make this function because command in button dont
    take function with param
    Draws the big circle with other circles tangent
    """
    dessiner_cercles(l,"Black")
    
def step_2():
    """
    Draws the cirles of soddy
    """
    h=all_triplets(l)
    j=new_draw(h)
    dessiner_cercles(j,"Black")
    
def step_3():
    
    """
    draws Once inside ampty circles  

    """
    
    h=all_triplets(l)
    j=new_draw(h)
    b=draw_empty_circles(l+j,N)
    dessiner_cercles(b,"Black")

    
def step_4():

    """
    give the final result

    """
    h=all_triplets(l)
    j=new_draw(h)
    l1=recursif_two(l[1:]+j,N,0)
    dessiner_cercles(l1,"Black")

def draw_random():
    """
    give the final result randomly
    """
    alea=random.randint(3,20)
    h=all_triplets(l)
    j=new_draw(h)
    l2=recursif_two(l[1:]+j,alea,0)
    dessiner_cercles(l+l2,'black')

        
from datetime import datetime
maintenant = datetime.now()
temps=str(maintenant.day)+"-"+str(maintenant.month)+"-"+str(maintenant.year)+" "+str(maintenant.hour)+":"+str(maintenant.minute)

#####################################################################
####             quelques paramétres                             ####
#####################################################################
def save():
    """
    save the result
    """
    from PIL import Image
    cercle.postscript(file="../images/circles.eps", colormode='color')
    img = Image.open("../images/circles.eps")
    img.save("../images/"+temps+".png", "png")

def undo():

    """
    delete the drawing

    """
    cercle.delete('all')



        
###################################################################
####                         TKINTER                           ####
###################################################################
# creation de la fenetre tk
fenetre = Tk()
fenetre.title("La baderne d’Apollonius fractale")
fenetre.configure(bg='Black')
# creation du canvas
cercle = Canvas(fenetre,bg='white',height=600,width=900)
cercle.pack(side=LEFT, padx=5, pady=5)
#création des boutons
bout1 = Button(fenetre, bg='white', bd='5', activebackground='Black', activeforeground='White', text='Première Etape', command=step_1)
bout1.pack(side=TOP, padx=10, pady=5)

bout2 = Button(fenetre, bg='white', bd='5', activebackground='Black', activeforeground='White', text='Deuxième Etape', command=step_2)
bout2.pack(side=TOP, padx=10, pady=5)

bout3 = Button(fenetre, bg='white', bd='5', activebackground='Black', activeforeground='White', text='Troisième Etape', command=step_3)
bout3.pack(side=TOP, padx=10, pady=5)

bout4 = Button(fenetre, bg='white', bd='5', activebackground='Black', activeforeground='White', text='Dernière Etape', command=step_4)
bout4.pack(side=TOP, padx=10, pady=5)

bout5bis= Button(fenetre, bg='white', bd='5', activebackground='Black', activeforeground='White', text='Aléatoirement', command=draw_random)
bout5bis.pack(side=TOP, padx=10, pady=5)

bout5 = Button(fenetre, bg='red', bd='5', activebackground='Black', activeforeground='White', text='Quitter', command=fenetre.quit)
bout5.pack(side=BOTTOM, padx=5, pady=5)

bout7 = Button(fenetre, bg='blue', bd='5', activebackground='Black', activeforeground='White', text='Sauver', command=save)
bout7.pack(side=BOTTOM, padx=5, pady=5)

bout6 = Button(fenetre, bg='yellow', bd='5', activebackground='Black', activeforeground='White', text='Effacer', command=undo)
bout6.pack(side=BOTTOM, padx=5, pady=5)

fenetre.mainloop()
fenetre.destroy()
 
#os.system('pause')
if __name__ == '__main__':
    pass 

