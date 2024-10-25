#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:04:11 2023

@author: doan
"""


import os, sys
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from numpy import random as rand
import matplotlib.colors as mcolors
import pandas as pd

    
df = pd.read_csv('test_data.csv', index_col=0)
input2d = df.values



n_sample =  input2d.shape[0]
n_dim = input2d.shape[1]

n_rows, n_cols = 20, 20

grid = np.random.uniform(low=0, high=1, size=[n_rows, n_cols, n_dim] )

# plot the initial condition
plt.imshow(grid) 


iterate = 3000

lambda_lr, max_lr, lambda_nb = 0.25, 0.1, 0.5
life = iterate * lambda_lr
initial = n_rows*lambda_nb


Lr = np.zeros(iterate)   # leaning rate (each step)
Nbh = np.zeros(iterate)  # Neiborhood function (each step)


index_map = np.zeros( [n_rows, n_cols, 2 ] )
for j in range(n_rows):
    for i in range(n_cols):
        index_map[j,i] = j,i
            


for i in range(iterate):
    # STEP 2-1: select input vector (randomly)
    ind = rand.randint(0, input2d.shape[0])
    sample = input2d[ind]
    
    # STEP 2-2: find best matching unit        
    print(ind)
    
    bmu = np.unravel_index(np.argmin(np.linalg.norm(grid - sample, axis=2)), grid.shape[:2])
    
    distance = np.linalg.norm(index_map - bmu, axis = 2)
    lrn_rate    = max_lr * np.exp(-i/life)    
    neighb_func = initial * np.exp(-i/life)
    S = np.exp(-distance**2 / (2*neighb_func**2))           
    
    
    grid = grid + lrn_rate* S[:,:,np.newaxis] * (sample - grid)
    

    #if np.mod(i, 100)==0:
    if i in [1, 10, 20, 50,  75, 100, 500, 1000, 1500, 2000, 2500, 3000, 4000, iterate-1]:
        plt.imshow(grid) 
        plt.text(0,0, 'Step: '+str(i), va = 'top')   
        plt.show()             
            
                

        
        
