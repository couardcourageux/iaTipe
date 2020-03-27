import pickle
import random
import math
import numpy as np
import matplotlib.pyplot as plt

import os



from PIL import Image as img


def view(x):
    fichier = open(x, 'rb')  #  <- indiquer le chemin ici
    montagne = pickle.load(fichier)
    fichier.close()

    lignes, colonnes = montagne.shape

    output = np.array([[0 for i in range(colonnes)] for j in range(lignes)],  dtype=float)

    for i in range(lignes):
        for j in range(colonnes):

            totalLocal, nbDePtsPrisEnCompte = 0, 0

            a = random.randint(15, 25)

            for y in range(max(0, i- a ), min(lignes, i+ a+1)):

                for x in range(max(0, j - a), min(colonnes, j + a + 1)):
                    totalLocal += montagne[y, x]
                    nbDePtsPrisEnCompte += 1
                    output[i, j] = ( 1 + random.choice([-1, 1])* random.uniform( 1/50, 1/100)) * totalLocal/nbDePtsPrisEnCompte
    return output


# ---------  juste pour show la map


def add_color(path):

    fichier = open(path, 'rb')  #  <- indiquer le chemin ici
    world = pickle.load(fichier)
    fichier.close()


    bluedeep = (43, 85, 158)
    blueSurface = (92, 165, 214)
    forest = (57, 107, 6)
    beach = (199, 183, 64)
    cobble = (103, 105, 95)

    image = img.new("RGB", (world.shape[0], world.shape[1]))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx, ny, nr, ng, nb = [], [], [], [], []
    for y in range(imgy):
        for x in range(imgx):
            if world[x, y] <= 0:
                putpixel((x, y), bluedeep)

            elif 0 < world[x, y] < 0.05:
                putpixel((x, y), beach)
            elif 0.05 <= world[x, y] < 0.5:
                putpixel((x, y), forest)
            else:
                putpixel((x, y), cobble)
    # image.save("montagne.png", "PNG")
    image.show()


add_color( "../maps/1000x1000x0.40_2/carte"   )   # path en argument

add_color( "../maps/1000x1000x0.40_3/carte"   ) 
add_color( "../maps/1000x1000x0.40_4/carte"   ) 


# add_color(output)
#
#
# plt.matshow(output)
#
# plt.colorbar()
# plt.show()
