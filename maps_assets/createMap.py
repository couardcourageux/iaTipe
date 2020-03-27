import pickle
import random
import math
import numpy as np
import matplotlib.pyplot as plt

import os
# import view_asset as va

from threading import Thread
from PIL import Image as img


# ________________________________________________________________

def maxi_indice(x, liste):                                  #liste est triee apr ordre croissant
    for i in range(len(liste)):
        if liste[i] >= x:
            return i
    return len(liste)

def create_map(lignes, colonnes, proportion):

    output = np.array([[-1 for i in range(colonnes)] for j in range(lignes)],  dtype=float) #creation map vide
    nbMaxNonNav = (colonnes*lignes) * (1 - proportion)          # on determine le nb de non nav pour avoir la bonne proportion



    fichier = open("../assets/datasheet", 'rb')        #on charge le datasheet des assets pour avoir la liste des assets
    dicoAssets = pickle.load(fichier)
    fichier.close()





    ratioPoss, assetsSelec = [], []            # on repertorie toutes les tailles possibles, danqs l'ordre croissant
    for c in dicoAssets:
        if c != "last":
            if len(ratioPoss) == 0:
                ratioPoss.append(c)
            else:
                temp = []
                while len(ratioPoss) > 0 and ratioPoss[-1] > c:
                    temp.append( ratioPoss.pop( len(ratioPoss) - 1 ) )
                ratioPoss.append(c)
                while len(temp) != 0:
                    ratioPoss.append(temp.pop(len(temp) - 1))




    nbActuel = 0
    while nbActuel <= nbMaxNonNav:                               # on selectionne des assets au hasard tant que leur nb de non nav ne fait pas depasser le nb max

        listeResult = ratioPoss[:maxi_indice(nbMaxNonNav - nbActuel, ratioPoss)+1]

        if len(listeResult) != 0:
            choisi = random.choice(listeResult)
            nbActuel += choisi
            assetsSelec.append(random.choice(dicoAssets[choisi]))
        else:
            nbActuel = nbMaxNonNav + 1

    print(assetsSelec)
    for i in range(len(assetsSelec)):                               #pour chaque asset choisi

        fichier = open("../assets/asset_" + str(assetsSelec[i]), 'rb')
        assetCourant = pickle.load(fichier)                                     #on le charge, on prend sa taille
        fichier.close()

        # va.add_color(va.view(assetsSelec[i]))

        l, c = assetCourant.shape
        xdep, ydep = random.randint(0, colonnes- 1 ), random.randint(0, lignes - 1)        # on tire un point d'application au hasard sur l'output
        for x in range(c):

            for y in range(l):
                # print(" {} sur {} traites".format(x*y, l*c))
                if 0 <= xdep+x < colonnes and 0 <= ydep+y < lignes:
                    output[ydep +y, xdep+ x] +=  assetCourant[y, x]                 #on place l'asset
        print("il reste {} assets".format(len(assetsSelec) - i))





    return output


def lissage(map, nbThread):
    sortie = np.array([[0 for i in range(map.shape[1])] for j in range(map.shape[0])],  dtype=float)          # on lance l'algo de bruit moyenneur


    class lisseur(Thread):

        def __init__(self, map, a, b, test=False):

            Thread.__init__(self)

            self.map = map
            self.output = np.array([[0 for  j in range(map.shape[1]) ] for  i in range(a, b)], dtype=float)
            self.a = a
            self.b = b
            self.test = test

        def run(self):
            count = 0
            for l in range(self.a, self.b):
                for c in range(self.map.shape[1]):

                    if self.test:
                        count+=1
                        print(count/((self.b - self.a )*(self.map.shape[1])))


                    totalLocal, nbDePtsPrisEnCompte = 0, 0
                    dist  = random.randint(15, 25)
                    for y in range(max(0, l- dist ), min(self.map.shape[0], l+ dist+1)):

                        for x in range(max(0, c - dist), min(self.map.shape[1], c + dist + 1)):

                            totalLocal += self.map[y, x]
                            nbDePtsPrisEnCompte += 1

                    self.output[l-self.a, c] = ( 1 + random.choice([-1, 1])* random.uniform( 1/50, 1/100)) * totalLocal/nbDePtsPrisEnCompte

    thrd = {}
    ration = map.shape[0]/nbThread
    listePartage = [int(ration*i) for i in range(nbThread)]
    listePartage.append(map.shape[0])


    for i in range(nbThread):
        if i == 0:
            thrd[i] = lisseur(np.copy(map), listePartage[i], listePartage[i+1], True)
        else:
            thrd[i] = lisseur(np.copy(map), listePartage[i], listePartage[i+1])

    for i in range(nbThread):
        thrd[i].start()

    for i in range(nbThread):
        thrd[i].join()


    sortie = np.copy(thrd[0].output)
    for i in range(1, nbThread):
        sortie = np.concatenate((sortie, thrd[i].output), axis=0)

    return sortie



def saveMap(lignes, colonnes , proportions, nbThread, name):

    try:
        os.mkdir("../maps/" + name)
    except OSError as e:
        print(os.strerror(e.errno))
        return True

    map = lissage(create_map(lignes, colonnes, proportions), nbThread)
    #map = create_map(lignes, colonnes, proportions)


    name = "../maps/" + name
    fichier = open(name+"/carte", 'wb')
    pickle.dump(map, fichier)
    fichier.close()

    fichier = open(name+"/trajets", 'wb')
    pickle.dump({}, fichier)
    fichier.close()


for i in range(10):
    saveMap(1000,1000,0.40,20,"1000x1000x0.40_{}".format(i))
