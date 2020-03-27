import math
import random
import numpy as np
import copy
import os
import pickle

import matplotlib.pyplot as plt
from PIL import Image as img



def calc_dist(a, b):
    return math.sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2  )

def update_pos(pos, angle, distance):   #(y, x)
    return ( pos[0] + distance * math.sin(angle), pos[1] + distance * math.cos(angle))
