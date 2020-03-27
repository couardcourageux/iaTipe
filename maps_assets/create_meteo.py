import random as rd
import pickle 
import math
import numpy as np

#----------------------------

def create_wind(map_shape, force, angle):
    carte vent = np.array([ [ [ 0, 0 ] for j in range(map_shape[1])] ])