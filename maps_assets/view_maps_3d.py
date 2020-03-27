import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import pickle


fichier = open("../maps/600x600x0.55/carte", 'rb')  #  <- indiquer le chemin ici
montagne = pickle.load(fichier)
fichier.close()

lignes, colonnes = montagne.shape




fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, colonnes)
Y = np.arange(0, lignes)
Xgrid, Ygrid = np.meshgrid(X, Y)
ax.plot_surface(Xgrid, Ygrid, montagne, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.show() 