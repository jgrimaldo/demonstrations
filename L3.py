#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:01:53 2019

@author: grimaldo
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rr

means = []
Ls = np.linspace(0, 100)
for L in Ls:
    n = 100000
    acc = 0.0
    for i in range(n):
        v1 = rr.uniform(0.0, L)
        v2 = rr.uniform(0.0, L)
        acc += np.abs(v1 - v2)
        
    mean = acc / n
    means.append(mean)
    
plt.scatter(Ls, means, color='blue', alpha=0.5, zorder=1, label='Mean after 100000 trials')
plt.plot(Ls, Ls/3.0, color='black', label='L/3')
plt.legend()
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel("Interval length for uniform distribution")
plt.ylabel("Mean distance between two samples in uniform distribution")
plt.show()