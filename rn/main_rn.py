# np.arctan() * 2/math.pi    # on utilise ici arctan comme fonction de decision des neurones, et on borne les valeurs entre -1 et 1

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
from paquets.fct_utiles import *
from paquets.rn_bat import *
from paquets.scores import *
from paquets.mutations import *


import paquets.train_test as tt


import paquets.train_main as tm
#-----------------------------------------------------------------------------------------------------------------


    
def main():
    
    
    gen_00 = creer_gen_rn(50, "test", [42, 30, 20, 2])

    # create_dir("jessica")


    #test engagés sur les mth de mutations--------------------------------------------------------



    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_1,0.1, True, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai140", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_2,0.1, True, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai141", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50,  mutate_3,0.1, True, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai142", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_4,0.1, True, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai143", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_5,0.1, True, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai144", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    #---------------------------


    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_1,0.1, False, 1 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai150", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_2,0.1, False, 1 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai151", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50,  mutate_3,0.1, False, 1 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai152", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_4,0.1, False, 1 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai153", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_5,0.1, False, 1 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai154", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    

#------------------------------------------------------------------------------------------------

    #tests sur les mth  de scores--------------------

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_3 ,0.1, False, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai200", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_4 ,0.1, False, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai210", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_5 ,0.1, False, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai220", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()


    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_3 ,0.1, False, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai201", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_4 ,0.1, False, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai211", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_5 ,0.1, False, 5 )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai221", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

#--------------------------

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_3 ,0.1, True, 2, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai203", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_4 ,0.1, True, 2, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai213", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_5 ,0.1, True, 2, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai223", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()



    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_3 ,0.1, True, 2, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai202", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()


    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_4 ,0.1, True, 2, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai212", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_5 ,0.1, True, 2,  bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai222", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()


    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_3 ,0.1, True, 2 , moyenneur=True)
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai204", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()


    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_4 ,0.1, True, 2 , moyenneur=True)
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai214", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_5 ,0.1, True, 2 , moyenneur=True)
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai224", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()



    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_3 ,0.1, True, 2,  moyenneur=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai205", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()


    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_4 ,0.1, True, 2,  moyenneur=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai215", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()


    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_5 ,0.1, True, 2,  moyenneur=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai225", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_3 ,0.1, True, 2,  moyenneur=True, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai207", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_4 ,0.1, True, 2,  moyenneur=True, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai217", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move_2,50, mutate_5 ,0.1, True, 2,  moyenneur=True, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai227", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_3 ,0.1, True, 2,  moyenneur=True, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai206", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_4 ,0.1, True, 2,  moyenneur=True, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai216", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    # stat_mth1 = tm.train(gen_00, "jessica", 90, update_score_move,50, mutate_5 ,0.1, True, 2,  moyenneur=True, bonus=True, malus=True )
    # #gen, nom, nbgen, score, mutation, eps=0.1, moyenneur=False)
    # stat_mth1 = assembleur_de_donnees(stat_mth1)
    # stat_mth1["desciption"] = "score mth 1, eps=0.1, mutate_1, 20genx80pop sur 5 essais"
    # fichier = open("data/essai226", "wb")
    # pickle.dump(stat_mth1, fichier)
    # fichier.close()

    
    

    

    # def train(gen, nom, nbgen, fct_move, score_fct,dist_max, mutation, eps=0.1, stat=False, nbCopies=5, moyenneur=False, bonus=False, malus=False):




    #
    # ->   il faut que je mette en place les test avec les nouvelles 
    # ->         mth d'entrainement qui separent les scores du mvt
    #

    
    

    # fichier = open("data/essai1", "rb")
    # rn_historique = pickle.load(fichier)
    # fichier.close()
    # print("")
    # print(rn_historique)
    # save_rn_last_gen("jessica", gen_next)

    # # rn2.initialiser()
    # # print((rn2.score, rn2.boat, len(rn2.topologie)))

    # a = load_rn_last_pop("jessica")
    
    
    # historique = load_historique("jessica")
    # print(gen_next[0].gen)
    # for c, v in historique[3][0].items():
    #     print(c,  v)
    

    pass

if __name__ == "__main__":
    main()



## Modifier train pour qu'il modifie une generation deja existante