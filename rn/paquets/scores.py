
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



def update_score_move(obj_rn, rotation, varVitesse, map, arrivee):      #prend tjrs en compte la veritable position du bateau
    last_distance = obj_rn.boat.dist
    obj_rn.boat.move(rotation, varVitesse, map, arrivee)                 #fait bouger le bateau
    obj_rn.set_score(max(0, last_distance - obj_rn.boat.dist) )     # si le bateau se rapproche de la cible, le rn gagne des points
    # print(last_distance)


def update_score_move_2(obj_rn, rotation, varVitesse, map, arrivee): 
    last_distance = obj_rn.boat.dist
    obj_rn.boat.move(rotation, varVitesse, map, arrivee)                 #fait bouger le bateau
    obj_rn.set_score(last_distance - obj_rn.boat.dist)


def move(obj_rn, rotation, varVitesse, map, arrivee):
    obj_rn.boat.move(rotation, varVitesse, map, arrivee)


def score(obj_rn, bonus=False, malus=False, moyenneur=False):
    score = obj_rn.score
    if moyenneur:
        score = score/obj_rn.boat.dpl

    if bonus and self.boat.pas_arrivee == True:
        score += 300
    if malus and self.boat.vivant:
        score+= 100

    obj_rn.reset_score()
    obj_rn.set_score(score)

    


