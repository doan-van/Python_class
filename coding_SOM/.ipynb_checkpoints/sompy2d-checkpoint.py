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


if __name__ == "__main__":
    print("Test run: this test for 2-dim input vectors and using negative ED as similarty index")
    #plt.rcParams['figure.figsize'] = (6, 6)
    #plt.style.use('ggplot')


    n_sample = 400
    # Setup randomly input data
    x = np.random.normal( (-.5,-.5), .2, (n_sample,2) )
    x = np.append(x, np.random.normal((-.25,1), .2, (n_sample,2) ), axis=0)
    x = np.append(x, np.random.normal((.5,.5), .2, (n_sample,2) ), axis=0)
    
    
        
    plot=1
        
    n_rows, n_cols = 8, 8
    input2d = x
        
    grid = np.random.uniform(low=input2d.min(), high=input2d.max(), size=[n_rows, n_cols, input2d.shape[-1]] )
    
    #input2d[:,0].max()
    for j in range(n_rows):
        for i in range(n_cols):
            grid[j,i,0] = input2d[:,0].min() + j*( input2d[:,0].max() - input2d[:,0].min())/(n_rows-1)
            grid[j,i,1] = input2d[:,1].min() + i*( input2d[:,1].max() - input2d[:,1].min())/(n_cols-1)

    
    grid_0 = grid.copy()

    



    if plot:
        # plot final results
        fig = plt.figure(figsize=(5,5))
        ax = plt.axes([.1,.1,.8,.8])
        plt.scatter(x[:,0],x[:,1],alpha=.6,color='k',s=15) 
        
        for j in range(n_rows):
            plt.plot(grid[j,:,0],grid[j,:,1],alpha=1,color='r', lw=0.5)  
        for i in range(n_cols):
            plt.plot(grid[:,i,0],grid[:,i,1],alpha=1,color='r', lw=0.5)   
        for j in range(n_rows):
            for i in range(n_cols):
                plt.scatter(grid[j,i,0],grid[j,i,1],alpha=1,color='r',s=20)    



    iterate = 10000


                
                
    learnrate = 0.1
    lambda_lr, max_lr, lambda_nb = 0.25, learnrate, 0.5
    
    
    
    life = iterate * lambda_lr
    
    
    initial = n_rows*lambda_nb
    
    Lr = np.zeros(iterate)   # leaning rate (each step)
    Nbh = np.zeros(iterate)  # Neiborhood function (each step)
    Bmu_2a = np.zeros( (iterate) ) # best matching unit (each step)
    
    index_map = np.zeros( [n_rows, n_cols, input2d.shape[-1]] )
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
        
        
        
        '''
        Bmu_2a[i] = bmu_1d # save best matching unit
        # Step 2-3: Update learning rate and neighborhood function
        dis = index_map - bmu_1d    
        Lr[i] = max_lr * np.exp(-i/life)    
        Nbh[i] = initial * np.exp(-i/life)
        S = np.exp(-dis**2 / (2*Nbh[i]**2))   
        # Step 2-4: Update SOM map
        output2d = output2d + Lr[i]* S[:,np.newaxis] * (data - output2d)
        '''
    
    
                
        if 1:
            if np.mod(i, 500)==0:
                # plot final results
                fig = plt.figure(figsize=(5,5))
                ax = plt.axes([.1,.1,.8,.8])
                plt.scatter(x[:,0],x[:,1],alpha=.6,color='k',s=15) 
                
                plt.scatter(input2d[ind,0],input2d[ind,1],alpha=1,color='g',s=50, marker='s') 
                plt.scatter(grid[bmu[0],bmu[1]][0],grid[bmu[0],bmu[1]][1],alpha=1,color='r',s=100, marker='s') 
                
                for j in range(n_rows):
                    for i in range(n_cols):
                        plt.scatter(grid[j,i,0],grid[j,i,1],alpha=1,color='r',s=20)      
                        
                    
                for j in range(n_rows):
                    plt.plot(grid[j,:,0],grid[j,:,1],alpha=1,color='r', lw=0.5)  
                for i in range(n_cols):
                    plt.plot(grid[:,i,0],grid[:,i,1],alpha=1,color='r', lw=0.5)   
                for j in range(n_rows):
                    for i in range(n_cols):
                        plt.scatter(grid[j,i,0],grid[j,i,1],alpha=1,color='r',s=20)    
                plt.grid(None)
                
                
                

        
        
