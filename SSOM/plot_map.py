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
import sys



'''
proj =  ccrs.PlateCarree()

fig = plt.figure(figsize=(4, 4))
ax = plt.axes([.05,0.05,.9,.9], projection= proj )

ax.set_extent([126,150,25, 50])
ax.coastlines(resolution='10m',lw=.5, color='gray')

ax.stock_img()



ax.scatter(df.longitude, df.latitude, color='k', marker='o')
'''












# plot using function
def plot_map_scatter(lon, lat, extent):
    proj =  ccrs.PlateCarree()

    fig = plt.figure(figsize=(4, 4))
    ax = plt.axes([.05,0.05,.9,.9], projection= proj )
    ax.set_extent(extent)
    ax.coastlines(resolution='10m',lw=.5, color='gray')
    ax.stock_img()
    ax.scatter(lon, lat, color='g', marker='o',)    
    return fig, ax








df = pd.read_csv('input_data/AMeDAS_stations.csv', index_col=0)

extent = [126,150,25, 50]
lon, lat = df.longitude, df.latitude
fig, ax = plot_map_scatter(lon, lat, extent)



#extent = [100,150,25, 50]
#fig, ax = plot_map_scatter(lon, lat, extent)










# add text
ax.text(.2, .8, 'AMeDAS location', 
        fontsize = 20, 
        transform = ax.transAxes,
        )

# grid
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=2, color='gray', alpha=0.5, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = False
gl.xlines = True
gl.xlocator = mticker.FixedLocator([-180, -45, 0, 45, 135, 140])
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlabel_style = {'size': 30, 'color': 'red'}
gl.xlabel_style = {'color': 'red', 'weight': 'bold'}






