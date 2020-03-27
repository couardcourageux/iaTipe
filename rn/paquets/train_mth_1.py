import math
import random
import numpy as np
import copy
import os
import pickle

import matplotlib.pyplot as plt
from PIL import Image as img
from threading import Thread


#-----------------------------------------------------------------------------------------------------------------
from paquets.fct_basiques import *
from paquets.fct_utiles import *
from paquets.rn_bat import *
from paquets.scores import *
from paquets.mutations import *
#-------------------------------------


def train_general(name, population, carte, fct_score):
    a = copy.deepcopy(gen)
    j = a[0].gen  #numero de la gen suivante, qu'on cherche à faire
    nbMaxMvt = int(j+ j/2 *math.log(j**2 + 1))  # on definit un nb max de mvt dispos pour les rn
        # nbMaxMvt = 20
    for r in a :            #-> pour chaque rn

        r.set_new_boat(depart, arrivee)     # on donne à chque rn un bateau, placé au point de depart
        mvt = 0
        while mvt < nbMaxMvt and r.boat.vivant and r.boat.pas_arrivee:  #on le fait fonctionner tant qu'il ne depasse pas nbMaxMvt et tant qu'il est en vie
            r.set_entry(carte)
            r.decider()
                #-> je choisis ici un angle maximal de rotation de pi/3, sur la gauche ou sur la droite du bateau

            rotation = r.output[0, 0] * math.pi/2
            varVitesse = r.output[1, 0]   # fais varier la vitesse actuelle du bateau

            fct_score(r, rotation, varVitesse,carte, arrivee)
            mvt += 1

                #si le bateau est mort, on divise son score, pour eviter le grind d'un rn qui fonce dans un mur mieux que les autres
            if r.boat.vivant == False:
                r.set_score(-4*(r.score / 5))
        r.lvl_up()
    return a 

    

class coach(Thread):
    def __init__(self, carte,  population, name, fct_score):
        Thread.__init__(self)

        self.carte = carte
        self.population = population
        self.name = name
        self.fct = fct_score
        self.output = None

    def run(self):
        self.output = train_general(self.name, self.population , self.carte, self.fct)


def train_main(carte,NbMaxGen, population, name, fct_score):
    cartes_copies = [carte[:] for i in range(10)]
    pas = int(len(population) / 10)
    pop_travail = copy.deepcopy(population)
    for i in range(NbMaxGen):
        thr = []
        for j in range(9):
            thr.append(coach(cartes_copies[j], pop_travail[j*pas:(j+1)*pas], name, fct_score))
        thr.append(coach(cartes_copies[9], pop_travail[9*pas:], name, fct_score))

        for j in range(10):
            thr[i].start()

        for j in range(10):
            thr[i].join()

        pop_travail = []
        for j in range(10):
            pop_travail = pop_travail + thr[i].output

        pop_travail = trifusion(pop_travail)
        update_historique(name, pop_travail)

        #endroit de mutation

    return pop_travail



def train(NbMaxGen,gen, carte, list_name, listTrain_mth):
    #historique : [[0.historique, 1.historique...]....]
    depart, arrivee = set_dep_arriv()
    tabAcces_map = [[copy.deepcopy(carte) for i in range(10)] for j in range(len(listTrain_mth))]
    for i in range(len(listTrain_mth)):
        train_main(carte, NbMaxGen, gen, list_name[i], listTrain_mth[i] )

