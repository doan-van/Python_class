#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:57:06 2023

@author: doan
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Fixing random state for reproducibility
np.random.seed(19680801)




n_sample = [2000, 500, 500, 500]
# Setup randomly input data
x1 = np.array([[0.99 , 0., 0.], # r
       [0.0, 0.95, 0.],  # g
       [0.0, 0.0, 0.95],  # b
       [1,1,.0]])


a = []
for i in range(4):
    x2 = x1[i]
    x = np.random.normal( (x2[0],x2[1],x2[2] ) , .2, (n_sample[i],3) )
    a = np.append(a,x)



a1 = (a-np.min(a))/(np.max(a)-np.min(a))
b = a1.reshape( np.sum(n_sample),3)
pd.DataFrame(b).to_csv('test_data.csv')



fig = plt.figure()
ax = fig.add_subplot(projection='3d')



ax.scatter( b[:,0], b[:,1],b[:,2], marker='o', c = b )
ax.view_init(10, 30) 

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()











