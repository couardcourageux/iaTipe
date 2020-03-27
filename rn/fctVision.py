import math
import random

def vision(pos, map, distVue):  #pos = (y, x)
    nbRayons = int(2*math.pi/(math.acos((1-distVue**2)/(-distVue**2))))
    angle_inter_rayons = 2*math.pi/nbRayons
    vue = []
    for i in range(nbRayons):
        posRegardee = pos[0] + distVue*math.sin(i*angle_inter_rayons), pos[1] + distVue*math.cos(i*angle_inter_rayons)
        if posRegardee[0] < 0 or posRegardee[0] >= map.shape[0] or posRegardee[1] < 0 or posRegardee[1] >= map.shape[1]:
            # la case est en dehors de la map
            vue.append(random.uniform(0.5,1))
        else:
            vue.append(map[posRegardee[0], map[posRegardee[1]]])

    return vue



#-----> radar, ne prend en compte que les points sur le perimetre du radar
