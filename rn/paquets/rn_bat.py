import math
import random
import numpy as np
import copy
import os
import pickle

import matplotlib.pyplot as plt
from PIL import Image as img

from paquets.fct_basiques import *


class reseaux():
    def __init__(self, name):
        self.name, self.state , self.gen, self.score = name, "desactive", 0, 0
        # le num de gen sert a reperer ou on en est dans l'entrainement, le score sert à sélectionner les individus à chaque génération, il est reinitialiser à chaque deb de selection



        a, b = -1, 1    #[a, b] est l'intervalle d'initialisation des poids des liaisons

        self.entry = []
        #self.dimension = []
        self.topologie = {}
        self.output = []




    def initialiser(self, topologie=[]):
        if len(topologie) != 0:
            topo_tempo = {}
            for i in range(len(topologie)-1):
                topo_tempo[i] = np.random.rand(topologie[i+1], topologie[i])

            a = -1
            b = 1

            for i in topo_tempo:
                self.topologie[i] = (b-a) * topo_tempo[i] + a       #les poids randomises des liaisons sont tous initialisés

        self.entry = np.array([ [0 ] for i in range(topologie[0])], dtype=float)

        self.output = np.array([[0 ] for i in range(topologie[-1])], dtype=float)
        self.state = "initialise"
        self.boat = None

    def set_score(self, nb):
        self.score += nb
    
    def reset_score(self):
        self.score = 0

        
    def lvl_up(self):
        self.gen +=1

    def export_param(self):
        obj_rn_tempo = reseaux(self.name)
        obj_rn_tempo.gen = self.gen
        obj_rn_tempo.topologie = copy.deepcopy(self.topologie)
        obj_rn_tempo.entry = copy.deepcopy(self.entry)
        obj_rn_tempo.output = copy.deepcopy(self.output)
        
        for i in range(self.entry.shape[0]):
            for j in range(self.entry.shape[1]):
                obj_rn_tempo.entry[i, j] = 0
        for i in range(self.output.shape[0]):
            for j in range(self.output.shape[1]):
                obj_rn_tempo.output[i, j] = 0


        obj_rn_tempo.score = 0
        obj_rn_tempo.state = "initialise"
        obj_rn_tempo.boat=None
        return obj_rn_tempo


    def set_entry(self, map): #prend rempli l'entry du rn avec un vecteur d'entree

            #fonction auxiliaire
        def vision( map, distVue):  #pos = (y, x)               #     -> distvue ocnditionne la taille du tableau d'entree, donc depend de topologie
            nbRayons = int(2*math.pi/(math.acos((1-distVue**2)/(-distVue**2)))) +1

            #print(nbRayons)

            angle_inter_rayons = 2*math.pi/nbRayons
            vue = []
            for i in range(nbRayons):
                posRegardee = int(self.boat.pos[0] + distVue*math.sin(i*angle_inter_rayons)), int(self.boat.pos[1] + distVue*math.cos(i*angle_inter_rayons))
                if posRegardee[0] < 0 or posRegardee[0] >= map.shape[0] or posRegardee[1] < 0 or posRegardee[1] >= map.shape[1]:
                    # la case est en dehors de la map
                    vue.append(random.uniform(0.5,1))
                else:
                    #print(posRegardee)

                    vue.append(map[posRegardee[0], posRegardee[1]])

            return vue
            #-----------------


        retourVision = vision(map, distVue=9) #on doit calc a la main le nb de rayons, dont depend la taille de l'entree
        for i in range(len(retourVision)):
            self.entry[i, 0] = retourVision[i]
        self.entry[40, 0] = self.boat.angle
        self.entry[41, 0] = self.boat.dist

    def decider(self):      # retourne dans self.out la sortie du neurone rapport a son entree courante. les calculs sont faits avec les poids des reseaux
        tempo = np.copy(self.entry)
        for i in range(len(self.topologie)):
            # print(self.topologie[i].shape)
            # print(tempo.shape)


            #dans la ligne d'apres, on effectue a chaque tour de boucle une evaluation par la fonction de decision choisie pour le reseau


            tempo = np.arctan(np.dot(self.topologie[i], tempo))
            #ici par defaut, il n'y en a aucune

        self.output = copy.deepcopy(tempo)

    def set_new_boat(self, posInit, posCible, vitMax=5):
        self.boat = bateau(posInit, posCible, vitMax)





class bateau():

    def __init__(self, posInit, posCible, vitMax):
        self.pos = posInit     #(y, x)
        self.angle = 0
        self.vitesse = 0
        self.vitMax = vitMax

        self.dpl = 0

        self.historique = {"angle":[self.angle], "position":[posInit], "dist_objectif":[calc_dist(self.pos, posCible)]}    #servira a exploiter les donnees des reseaux
        self.dist = calc_dist(posInit, posCible)

        self.vivant = True
        self.pas_arrivee = True

    def set_dist(self, posCible):
        self.dist = calc_dist(self.pos, posCible)
       

    def set_reussite(self):
        self.pas_arrivee = (False == (self.dist <= 0.5))

    def move(self, varAngle, varVitesse, map, posCible):
        self.angle = (self.angle +  varAngle) % (2*math.pi)
        # dans le modele, un bateau peut reculer, donc avoir une vitesse negative, et il est bien sur capé, sa marche avant est plus rapide que sa marche arriere
        # du a la forme de la coque  , on considera ici arbitrairement que la marche arriere ne peut exceder le 4 de la marche avant

        if self.vitesse + varVitesse >= 0:
            self.vitesse = min(self.vitesse + varVitesse, 1)
        else:
            self.vitesse = max(self.vitesse + varVitesse, (-1/4))


        i = 0
        while i <= ( self.vitesse * self.vitMax ) and self.vivant:
            posPassage = update_pos(self.pos, self.angle, i)
            if 0 > posPassage[0] or  posPassage[0] >= map.shape[0] or 0 > posPassage[1] or posPassage[1] >= map.shape[1] or map[int(posPassage[0]), int(posPassage[1])]  >= 0:
                self.vivant = False
                self.pos = posPassage
            i +=0.05      #pas suffisant pour ne rater aucune collision possible  lors du mouvement du bateau

        if self.vivant:
            self.pos = update_pos(self.pos, self.angle, self.vitesse * self.vitMax )
        
        self.set_dist(posCible)#update de la distance
        self.dpl += 1
        self.set_reussite()
    

        self.historique["angle"].append(self.angle)
        self.historique["position"].append(self.pos)
        self.historique["dist_objectif"].append(self.dist)
