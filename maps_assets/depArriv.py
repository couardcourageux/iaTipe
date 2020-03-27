import matplotlib.pyplot as plt
import os
import pickle
import numpy as np



def view(path):
    fichier = open(path, 'rb')
    carte = pickle.load(fichier)
    fichier.close()
    print(type(carte))
    plt.matshow(carte)
    plt.colorbar()
    plt.show()


# view("../maps/600x600x0.55_moche/carte")
view("../maps/600x600x0.55/carte")
