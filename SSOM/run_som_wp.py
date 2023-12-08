#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:30:47 2023

@author: doan
"""

from sompy import som
# plot results
import cartopy.crs as ccrs
import xarray as xr


ds = xr.open_dataset('input_data/SLP_DJF_2d.nc')
x0 = ds['slp'].values

X = x0.reshape(x0.shape[0], -1)

somout = som(X, 3, iterate = 5000, sim='ed') 
clus = somout['bmu_proj_fin']
y = somout['som']
y2d = y.reshape(y.shape[0], x0.shape[1], x0.shape[2])












