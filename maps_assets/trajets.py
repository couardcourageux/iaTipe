import os 
import pickle

import numpy as np


def chargement_carte(path):
    fichier = open(path+ "/carte")
    output = pickle.load(fichier, 'rb')
    fichier.close()
    return output

def chargement_trajets(path):
    fichier = open(path+ "/trajets")
    output = pickle.load(fichier , 'rb')
    fichier.close()
    return output


def save_trajets(path, content):
    fichier = open(path+"/trajets")
    pickle.dump(content, fichier)
    fichier.close()

def trajets(path, nb):
    carte = chargement_carte(path)
    for i in range(nb):
        pass
