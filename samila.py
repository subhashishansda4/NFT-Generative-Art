# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:31:03 2022

@author: VAGUE
"""

# source - https://github.com/sepandhaghighi/samila

import random
import math
import matplotlib.pyplot as plt
from samila import GenerativeImage, Projection

def f1(x, y):
    n = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return n

def f2(x, y):
    n = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return n

g = GenerativeImage(f1, f2)
# g.generate(start=-90, step=0.01, stop=0)
g.generate(seed = 69)
print(g.seed)
g.plot(color="red", bgcolor="black", projection = Projection.RECTILINEAR)