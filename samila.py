# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:31:03 2022

@author: VAGUE
"""

# source - https://github.com/sepandhaghighi/samila
# dark-cos and black
# light-sin and white
import random
import math
from samila import GenerativeImage, Projection

def f1(x, y):
    n = random.uniform(-1,1) * x**2  - math.cos(y**2) + abs(y-x)
    return -n

def f2(x, y):
    n = random.uniform(0,1) * y**4 - math.cos(x**2) + 2*x
    return n

DEFAULT_SEED = 1018273

g = GenerativeImage(f1,f2)
g.generate(seed=DEFAULT_SEED, start=-math.pi, stop=math.pi, step=0.01)
print(g.seed)
g.plot(size = (7.8,7.8), color="white", bgcolor="black", projection = Projection.RECTILINEAR)

g.save_image(file_adr="temp.png", depth=5)