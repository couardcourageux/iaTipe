import pickle
import random
import math
import numpy as np
import matplotlib.pyplot as plt

import os



from PIL import Image as img


#-------------------------------------------------------

def distance(x1, y1, x2, y2):    #renvoie la distance cartesienne entre 2 points
    return math.sqrt( ( x1 -  x2 )**2 + ( y1 - y2 )**2 )

def montagne2(h, x, a, b):      #def la hauteur du point en fct de la hauteur du pt haut et de sa dist a lui
    return (h/(1+1/h*(x**1.5)) + 2*max(h-(x/h)*a, 0) + max( h - max((b- h/x)*a, 3*x/h), 0  )) /4



def createMountain():
    lignes = random.randint(120, 360)
    colonnes = random.randint(max(120, int(lignes/2)),min(360, int(3*lignes/2)))

    montagne = np.array([[0 for i in range(colonnes)] for j in range(lignes)] , dtype=float)


    nbpth = random.randint(1, int(lignes*colonnes/(math.pi*(35**2)))+1)   # la surface d'action max consideree d'un pt haut
    ptH = []                                                          # on ajoute 1 pour eviter une liste vide

    for i in range(nbpth):      # on cree nbpth pt hauts
        x, y, h = random.randint(35, colonnes-36), random.randint(35, lignes-36), random.randint(12, 30)
        ptH.append({"x":x, "y":y, "h":h})
        montagne[y, x] += h



    for pt in ptH:

        for i in range(lignes):
            for j in range(colonnes):

                a = random.uniform(3, 9)
                b = random.uniform(0.2*a, 0.8*a)

                if i != pt["y"] or j != pt["x"]:
                    montagne[i, j] += montagne2(pt["h"], distance(i, j, pt["y"], pt["x"]), a, b)

    montagne = 1/len(ptH)*  montagne   # on moyenne les hauteurs de chaque point par le nombre points hauts

    h_max = 0
    for i in range(lignes):
        for j in range(colonnes):
            h_max = max(h_max, montagne[i, j])

    montagne = 2/h_max * montagne

    percent = 0
    for i in range(lignes):
        for j in range(colonnes):
            if montagne[i, j] >= 0:
                percent += 1


    return montagne, percent



def create_dataBase(nbAssets):
    numeroCourant = 0
    try:
        fichier = open("../assets/datasheet", 'rb')
        saveData = pickle.load(fichier)
        fichier.close()

        numeroCourant = saveData["last"]


    except :
        fichier = open("../assets/datasheet", 'wb')
        pickle.dump({"last":0}, fichier)
        saveData = {"last":0}
        fichier.close()


    for i in range(nbAssets):

        mapcourante = createMountain()
        nbNonNav = int(mapcourante[1])
        key = saveData.get(nbNonNav, "undef")
        if key == "undef":
            saveData[nbNonNav] = [numeroCourant]
        else:
            saveData[nbNonNav].append(numeroCourant)

        file = open("../assets/asset_" + str(numeroCourant), "wb")
        pickle.dump(mapcourante[0], file)
        file.close()

        numeroCourant += 1


    saveData["last"] = numeroCourant
    fichier = open("../assets/datasheet", 'wb')
    pickle.dump(saveData, fichier)
    fichier.close()



create_dataBase(1300)


