import math
import random
import numpy as np
import copy
import os
import pickle

import matplotlib.pyplot as plt
from PIL import Image as img
from threading import Thread
from statistics import mean
from threading import Thread


#-----------------------------------------------------------------------------------------------------------------
from paquets.fct_basiques import *
from paquets.fct_utiles import *
from paquets.rn_bat import *
from paquets.scores import *
from paquets.mutations import *
#-------------------------------------


def execution(carte, tupleDep, tupleArriv, rn_tab, fct_score, moyenneur, bonus, malus):
    numero_gen = rn_tab[0].gen

    copie_de_travail = copy.deepcopy(rn_tab)
    nbMaxMvt =  int(numero_gen + 5 + numero_gen/2 *math.log(numero_gen**2 + 1))  # on definit un nb max de mvt dispos pour les rn
    mvt_tab = []
    for rn in copie_de_travail:

        rn.set_new_boat(tupleDep, tupleArriv)
        mvt_effectues = 0
        while mvt_effectues < nbMaxMvt and rn.boat.vivant and rn.boat.pas_arrivee == False:
            rn.set_entry(carte)
            rn.decider()
                #-> je choisis ici un angle maximal de rotation de pi/3, sur la gauche ou sur la droite du bateau

            rotation = rn.output[0, 0] * math.pi/2
            varVitesse = rn.output[1, 0]   # fais varier la vitesse actuelle du bateau

            fct_score(rn, rotation, varVitesse, carte, tupleArriv)
            mvt_effectues += 1

        if moyenneur:
            score = rn.score
            rn.reset_score()
            rn.set_score(score/mvt_effectues)
        
        if bonus and rn.boat.vivant:
            rn.set_score(100)
        
        if malus and False == rn.boat.pas_arrivee :
            rn.set_score(500)
        mvt_tab.append(mvt_effectues)
        
            

            #on update pas le numero de gen, car on va faire plusieurs entrainements avant la mutation
    
    return copie_de_travail, mvt_tab

class executeur(Thread):
    def __init__(self, rn, nbMaxMvt, carte, tupleDep, tupleArriv, fct_score, moyenneur, bonus, malus):
        Thread.__init__(self)

        self.carte = copy.deepcopy(carte)
        self.rn = copy.deepcopy(rn)
        self.nbMaxMvt = nbMaxMvt
        self.tupleDep = tupleDep
        self.tupleArriv = tupleArriv
        self.fct_score = fct_score
        self.moyenneur = moyenneur
        self.bonus = bonus
        self.malus = malus
        self.mvt_faits = 0

    def run(self):
        self.rn.set_new_boat(self.tupleDep, self.tupleArriv)
        mvt_effectues = 0
        while mvt_effectues < self.nbMaxMvt and self.rn.boat.vivant and self.rn.boat.pas_arrivee:
            self.rn.set_entry(self.carte)
            self.rn.decider()
                #-> je choisis ici un angle maximal de rotation de pi/3, sur la gauche ou sur la droite du bateau

            rotation = self.rn.output[0, 0] * math.pi/2
            varVitesse = self.rn.output[1, 0]   # fais varier la vitesse actuelle du bateau

            self.fct_score(self.rn, rotation, varVitesse, self.carte, self.tupleArriv)
            mvt_effectues += 1

        if self.moyenneur:
            score = self.rn.score
            self.rn.reset_score()
            self.rn.set_score(score/mvt_effectues)
        
        if self.bonus and self.rn.boat.vivant:
            self.rn.set_score(100)
        
        if self.malus and False == self.rn.boat.pas_arrivee :
            self.rn.set_score(500)
            
        self.mvt_faits = mvt_effectues

    def stop(self):
        self.running = False





def exec(carte, tupleDep, tupleArriv, rn_tab, fct_score, moyenneur, bonus, malus):
    numero_gen = rn_tab[0].gen
    last_best = rn_tab[0]
    
    copie_de_travail = copy.deepcopy(rn_tab)
    nbMaxMvt = min( 80, int(numero_gen + 5 + numero_gen/2 *math.log(numero_gen**2 + 1)))  # on definit un nb max de mvt dispos pour les rn
    mvt_tab = []

    thrd = []
    a = executeur( rn_tab[0], nbMaxMvt, carte, tupleDep, tupleArriv, fct_score, moyenneur, bonus, malus )
   
    for rn in copie_de_travail:
        thrd.append( executeur(rn, nbMaxMvt, carte, tupleDep, tupleArriv, fct_score, moyenneur, bonus, malus) )
    
    

    for the_thread in thrd:
        the_thread.start()
    
    for the_thread in thrd:
        the_thread.join()

    copie_de_travail = []
    for the_thread in thrd:
        copie_de_travail.append(the_thread.rn)
        mvt_tab.append(the_thread.mvt_faits)
    
    del thrd
    
        
            

            #on update pas le numero de gen, car on va faire plusieurs entrainements avant la mutation
    
    return copie_de_travail, mvt_tab




def trier_sauvegarde(rn_tab, name, name_carte):
    copie_travail = trifusion(rn_tab)
    update_historique(name, copie_travail, name_carte)



def train(gen, nom, nbgen, fct_score,dist_max, mutation, eps=0.1, keep_last_best=False, nbCopies=1, moyenneur=False, bonus=False, malus=False):
    
    copies_tab = [ copy.deepcopy(gen) for i in range(nbCopies) ]
    stat_tab = []
    
    

    #----------------------------------
    liste_cartes = os.listdir("../maps")
    cartes = {}
    trajets = {}
    for carte_name in liste_cartes:  #on charge toutes les cartes
        cartes[carte_name] = charger_map(carte_name)
        trajets[carte_name] = []
    #----------------------------------

    if keep_last_best :
            # if gen == 0:
            last_best_tab = [copies_tab[i][0] for i in range(len(copies_tab))]

    
    for gen in range(nbgen):
        print("gen : ", gen)
        

        gen_en_cours = [[] for i in range(nbCopies)]

        #on choisit les trajets utiles pour entrainer cette gen
        nbTrajets = random.randint(4, 8)
        for carte_name in liste_cartes:  #on charge toutes les cartes
            cartes[carte_name] = charger_map(carte_name)
            trajets[carte_name] = []


        for i in range(nbTrajets):
            indice_carte = random.randint(0, len(liste_cartes) -1)
            nom_carte = liste_cartes[indice_carte]
            trajets[nom_carte].append( set_dep_arriv( cartes[nom_carte], dist_max ) )
          
        #-----------------
        

        
        score_tab = [ [0 for i in range(len(copies_tab[0]))] for j in range(nbCopies) ]
        rn_tab_tab_tab_tempo = []

        
        

        for carte_name, trajet in trajets.items():

            if len(trajet) > 0:
                for ieme_trajet in range(len(trajet)):
                   
                    print("execution")
                    # rn_tab_tab_tempo = [ execution(cartes[carte_name], trajet[ieme_trajet][0], trajet[ieme_trajet][1], copie_travail, fct_score, moyenneur, bonus, malus) for copie_travail in copies_tab ]
                    rn_tab_tab_tempo = [ exec(cartes[carte_name], trajet[ieme_trajet][0], trajet[ieme_trajet][1], copie_travail, fct_score, moyenneur, bonus, malus) for copie_travail in copies_tab ]
                        
                    for i in range(nbCopies):
                        
                        for j in range(len(rn_tab_tab_tempo[i])):
                            # print(rn_tab_tab_tempo[i][j])
                            score_tab[i][j] += rn_tab_tab_tempo[i][0][j].score /nbTrajets
                            gen_en_cours[i].append(rn_tab_tab_tempo[i][0][j])
                    rn_tab_tab_tab_tempo.append(rn_tab_tab_tempo)
                        

                                        
        #-------------------
        print("execution terminee")
        
        # print(rn_tab_tab_tab_tempo)

    
        #--pour voir stat moyenne---------------
        stat_temporaire = [ compilateur( [statifier(rn_tab_tab_tab_tempo[i][j][0], rn_tab_tab_tab_tempo[i][j][1]) for j in range(nbCopies)] ) for i in range(nbTrajets) ]
        #----------------------------------------
        stat_tab.append(compilateur(stat_temporaire)) 
                

       
            
        

        #-----------------------
        print("mutation en cours")

        copies_tab = copy.deepcopy(gen_en_cours)
        modele_gen_suivante_tab = [ trifusion(copie_temp) for copie_temp in copies_tab ]

        if keep_last_best:
            for i in range(len(modele_gen_suivante_tab)):
                if modele_gen_suivante_tab[i][0].score <= last_best_tab[i].score :
                    modele_gen_suivante_tab[i][0] = copy.deepcopy(last_best_tab[i])
                    print("gen:" , gen , "   ; best_act :", modele_gen_suivante_tab[i][0].score, "   ; bestouf:", last_best_tab[i].score)
                else:
                    last_best_tab[i] = copy.deepcopy(modele_gen_suivante_tab[i][0])
                print("meilleur:", modele_gen_suivante_tab[0][0].score)


        copies_tab = [ mutation(modele_gen_suivante, eps) for modele_gen_suivante in modele_gen_suivante_tab ]
        print(copies_tab[0][0].score, "bestttttt")

       
        print("mutation terminee")

        

    #-----------------------------------------------------------  

    
    return stat_tab
   
            
            
            

                        






