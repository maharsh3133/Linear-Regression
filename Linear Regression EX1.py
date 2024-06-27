# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:44:05 2023

@author: maharsh
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.random.default_rng(seed=2).uniform(-1,1,100)

y=[12*i -4 for i in x]
print(y)

plt.scatter(x, y,alpha=0.5)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("X vs Y without noise")
plt.show()

noise= np.random.normal(loc=0.0, scale=1, size=100)
print(noise)
y=y+noise
print(y)

plt.scatter(x, y,alpha=0.5)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("X vs Y with noise")
plt.show()