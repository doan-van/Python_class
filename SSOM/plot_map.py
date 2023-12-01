#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:28:18 2023

@author: doan
"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy
import pandas as pd


proj =  ccrs.PlateCarree()

fig = plt.figure(figsize=(4, 4))
ax = plt.axes([.05,0.05,.9,.9], projection= proj )


ax.set_extent([126,150,25, 50])
ax.coastlines(resolution='10m',lw=.5, color='gray')

ax.stock_img()
df = pd.read_csv('input_data/AMeDAS_stations.csv', index_col=0)

ax.scatter(df.longitude, df.latitude, color='r', marker='^')


















