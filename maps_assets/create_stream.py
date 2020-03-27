import pickle
import random
import math
import numpy as np
import matplotlib.pyplot as plt



# fichier = open("../maps/400x400x0.50/carte", 'rb')
# carte = pickle.load(fichier)
# fichier.close()

# carte2 = np.array([[0 for i in range( 400)] for j in range(400)])

carte_peu_detaillee = np.array([ [ 0 for i in range(200) ] for j in range(200) ])

def cree_modele_courants(carte):
    class file_attente:
        def __init__(self):
            self.corps = []
            self.pointeur = 0
            self.vide = True

        def add(self, elt):
            self.corps.append(elt)
            self.vide = False

        def retire(self):
            if self.vide:
                print("erreur, liste vide")
            else:
                ouput = self.corps[self.pointeur]
                self.pointeur+=1
                if self.pointeur == len(self.corps) -1:
                    self.vide = True
                return ouput

    ny, nx =  carte.shape

    maxForce = 10
    maxAngle = 2*math.pi

    forces = np.array([[0 for i in range(nx)] for j in range(ny)], dtype=float)
    directions = np.array([[0 for i in range(nx)] for j in range(ny)], dtype=float)
    deja_traite= np.array([[False for i in range(nx)] for j in range(ny)])
    

    for y in range(ny):
        for x in range(nx):
            if carte[y, x] > 0:
                deja_traite[y, x] = True

    liste_attente = file_attente()

    def impact_voisins(yy, xx):
        liste_voisins = []
        for i in range(max(0, yy-1), min(ny, yy+2)):
            for j in range(max(0, xx-1), min(nx, xx+2)):
                liste_voisins.append((i, j))
        random.shuffle(liste_voisins)

        for couple in liste_voisins:
            y, x = couple
            if deja_traite[y, x]:
                pass
            else:
                for i in range(max(0, y-1), min(ny, y+2)):
                    for j in range(max(0, x-1), min(nx, x+2)):

                        tot, count_local = 0, 0
                        if deja_traite[i, j]:
                            tot += directions[i, j] * random.uniform(0.7, 1.3)
                            count_local += 1
                        if count_local != 0:
                            directions[y, x] = (tot/count_local)
                            directions[y, x] = directions[y, x]%maxAngle
                        
                            deja_traite[y, x] = True
                            liste_attente.add((y, x))


                        tot, count_local = 0, 0
                        if deja_traite[i, j]:
                            tot += forces[i, j] * random.uniform(0.7, 1.3)
                            count_local += 1
                        if count_local != 0:
                            forces[y, x] = (tot/count_local)
                            deja_traite[y, x] = True
                        

    for i in range(nx):
        y, x = random.randint(0,ny-1 ), random.randint(0, nx-1)
        forces[y, x] = random.uniform(0, maxForce)
        directions[y, x] = random.uniform(0, maxAngle)
        deja_traite[y, x] = True
        liste_attente.add((y, x))



    while liste_attente.vide == False:
        y, x = liste_attente.retire()
        # print("ok")
        impact_voisins(y, x)

    return directions, forces





def montre_moi(directions, forces):
    plt.matshow(forces)
    plt.colorbar()
    plt.show()

    ny, nx = directions.shape

    stream_y = np.array([[math.sin(directions[j, i])*forces[j, i] for i in range(nx)] for j in range(ny)], dtype=float)
    stream_x = np.array([[math.cos(directions[j, i])*forces[j, i] for i in range(nx)] for j in range(ny)], dtype=float)

    base_y, base_x = np.array([i for i in range(ny)]), np.array([i for i in range(nx)])

    stream = plt.streamplot(base_x, base_y, stream_x, stream_y, cmap=forces)
    plt.colorbar()
    plt.show()


direc, forc = cree_modele_courants(carte_peu_detaillee)
direc2, dorc2 = cree_modele_courants(carte_peu_detaillee)

montre_moi(direc, forc)
montre_moi(direc2, dorc2)

# plt.matshow(directions )
# plt.matshow(forces)
# plt.colorbar()
# plt.show()