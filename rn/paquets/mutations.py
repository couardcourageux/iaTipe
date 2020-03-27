
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
#-------------------------

def mutate(rn_obj, eps=0.1):  #modif d'un indiv
    output_obj = copy.deepcopy(rn_obj)
    output_obj.gen = rn_obj.gen + 1
    output_obj.reset_score()
    
    for cle in output_obj.topologie:
        lignes, colonnes = output_obj.topologie[cle].shape
        for i in range(lignes):
            for j in range(colonnes):
                output_obj.topologie[cle][i, j] = output_obj.topologie[cle][i, j] * random.uniform(1-eps, 1+eps)
    return output_obj


#toute la pop
def mutate_1(rn_tab, eps=0.1):      
    output = [None for i in range(len(rn_tab))]
    for i in range(len(output)):
        output[i] = mutate(rn_tab[i], eps)
    
    return output



#1/2 de la pop
def mutate_2(rn_tab, eps=0.1):
    output = []
    for i in range( int(len(rn_tab)/2)):
        for j in range(2):
            output.append( mutate(rn_tab[i], eps))
        
    # print(output)
    return output



#1/4 de la pop
def mutate_3(rn_tab, eps=0.1):
    output = []
    for i in range( int((len(rn_tab)/4))):
        for j in range(4):
            output.append( mutate(rn_tab[i], eps))
        
    return output


#meilleur individu
def mutate_4(rn_tab, eps=0.1):
    output = []
    for i in range(len(rn_tab)):
        output.append( mutate(rn_tab[0], eps))
    return output

#hasard sur 1/4
def mutate_5(rn_tab, eps=0.1):
    output = []
    
    for i in range( len(rn_tab) ):
       
        output.append(mutate( rn_tab[random.randint(0, int(len(rn_tab)/4))] , eps))
        
    return output
    



