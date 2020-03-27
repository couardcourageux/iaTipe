


import math
import random
import numpy as np
import copy
import os
import pickle

import matplotlib.pyplot as plt
from PIL import Image as img


#-----------------------------------------------------------------------------------------------------------------
from paquets.fct_basiques import *
from paquets.rn_bat import *







def add_color(world, chemin, depart, poscible):

    bluedeep,blueSurface,forest, beach,cobble, boat, arriv, dep    = (43, 85, 158) , (92, 165, 214), (57, 107, 6), (199, 183, 64), (103, 105, 95), (000, 000, 000), (255, 0, 113), (255, 235, 0)
    # on def les couleurs dispos


    image = img.new("RGB", (world.shape[0], world.shape[1]))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx, ny, nr, ng, nb = [], [], [], [], []
    for y in range(imgy):
        for x in range(imgx):
            if world[x, y] <= 0:
                putpixel((x, y), bluedeep)

            elif 0 < world[x, y] < 0.05:
                putpixel((x, y), beach)
            elif 0.05 <= world[x, y] < 0.5:
                putpixel((x, y), forest)
            else:
                putpixel((x, y), cobble)

    for i in chemin:
        putpixel((int(i[1]), int(i[0])), boat)

    a, b = depart
    c, d = poscible
    a, b, c, d = int(a), int(b), int(c), int(d)
    putpixel((a, b), dep)
    putpixel((c, d), arriv)

    # image.save("trajet.png", "PNG")
    image.show()

#je dois encore modifier fusion pour que ca classe selon un arguement particulier tout un objet

def fusion(a, b):
    i, j = len(a), len(b)
    output = []
    c, d = 0, 0
    while c < i and d < j:
        if a[c].score > b[d].score:  #cette ligne fait qu'on trie la liste selon les scores des bateaux dans l'ordre decroissant
            output.append(a[c])
            c+=1
        else:
            output.append(b[d])
            d+=1
    output = output + a[c:] + b[d:]
    return output

def trifusion(liste):
    if len(liste) <= 1:
        return liste
    n = len(liste)//2
    return fusion(trifusion(liste[:n]), trifusion(liste[n:]))

def charger_map(name):
    fichier = open("../maps/{}/carte".format(name), "rb")
    map = pickle.load (fichier)
    fichier.close()
    return map





def creer_gen_rn(tailleGen, name, layers):
    a = []  #-> tabl d'1 gen, contenant une pop entiere de reseaux
    for i in range(tailleGen):
        a.append(reseaux(name))
        a[i].initialiser(layers)   
    return a

def set_dep_arriv(carte, dist_max):
    limites = carte.shape
    test = True
    while test:
        depart  = (random.randint(0, limites[0]-1), random.randint(0, limites[1]-1) )
        arrivee = (random.randint(0, limites[0]-1), random.randint(0, limites[1]-1) )
        if carte[depart] < 0 and carte[arrivee] < 0 and 20 <= calc_dist(depart, arrivee) <= dist_max:
            test = False
    
    return (depart, arrivee)

def load_historique(name):  #format tableau
    try:
        fichier = open("reseaux/{}/{}_historique".format(name, name), "rb")
        rn_historique = pickle.load(fichier)
        fichier.close()
        return rn_historique

    except:
        
        fichier = open("reseaux/{}/{}_historique".format(name, name), "wb")
        fichier.close()
        return []


def compile_histo_gen(tab_obj_rn, name_carte):
    histo_local = []
    for rn in tab_obj_rn:
        liste_tempo = copy.deepcopy(rn.boat.historique)
        liste_tempo["score"] = rn.score
        liste_tempo["vivant"] = rn.boat.vivant
        liste_tempo["arrive"] = (False == rn.boat.pas_arrivee)
        liste_tempo["carte"] = name_carte
        histo_local.append(liste_tempo)
    # print(histo_local[0]["dist_objectif"])
    return histo_local

def update_historique(name, tab_obj_rn, name_carte):
            #charge histo rn , tableau
    temp = load_historique(name)
    # if len(temp) != 0:
    #     # print(temp[0])
    historique_une_gen = compile_histo_gen(tab_obj_rn, name_carte)
    temp.append(historique_une_gen)
    
    fichier = open("reseaux/{}/{}_historique".format(name, name), "wb")
    pickle.dump(temp, fichier)
    fichier.close()
    #l'ancien historique est ecrasé, mais on conserve les donnees grace au
    #load histo


def load_rn_last_pop(name):  #renvoie une generation enregistree
    try:
        fichier = open("reseaux/{}/{}_lastGen".format(name, name), "rb")
        rn_gen_pop = pickle.load(fichier)
        fichier.close()
        return rn_gen_pop
    except :
        return []

def save_rn_last_gen(name, gen): #remplace le fichier de derniere gen , save d'une gen
    
    fichier = open("reseaux/{}/{}_lastGen".format(name, name), "wb")
    pickle.dump(gen, fichier)
    fichier.close()

def create_dir(name):  #crée les repertoires appropries pour la suite des op
    try:
        os.makedirs("reseaux/{}".format(name))
    except:
        pass

def statifier(rn_tab, nbMvt):
    output = {"points": 0, "nbMvt":0,"distance": 0, "vivants": 0, "objR": 0}
    for indice in range(len(nbMvt)):
        output["points"] += rn_tab[indice].score
        output["nbMvt"] += nbMvt[indice]
        output["distance"] += rn_tab[indice].boat.dist
        if rn_tab[indice].boat.vivant :
            output["vivants"] += 1 
        if rn_tab[indice].boat.pas_arrivee == False :
            output["objR"] += 1
    
    for c, v in output.items() :
        output[c] = v/len(rn_tab)

    return output

def compilateur(dico_stat_tab):
    output = {"points": 0, "nbMvt":0,"distance": 0, "vivants": 0, "objR": 0}
    for c, v in output.items():
        for dico in dico_stat_tab:
            output[c] += dico[c]
        output[c] = output[c]/len(dico_stat_tab)

    return output


def assembleur_de_donnees(dico_stat_tab):
    output = {"points": [], "nbMvt":[],"distance": [], "vivants": [], "objR": []}
    for c, v in output.items():
        for dico in dico_stat_tab:
            output[c].append(dico[c])

    return output
