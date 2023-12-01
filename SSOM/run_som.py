import sys, os
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sompy import som
# plot results
import cartopy.crs as ccrs




df = pd.read_csv('input_data/warming_70years_japan.csv', index_col=0)
X = df.values





somout = som(X, 5, iterate = 5000, sim='ed') 
clus = somout['bmu_proj_fin']
y = somout['som']



proj =  ccrs.PlateCarree()

fig = plt.figure(figsize=(4, 4))
ax = plt.axes([.05,0.05,.9,.9], projection= proj )


ax.set_extent([126,150,25, 50])
ax.coastlines(resolution='10m',lw=.5, color='gray')

ax.stock_img()
da = pd.read_csv('input_data/AMeDAS_stations.csv', index_col=0)


colors = ['b', 'r', 'g', 'orange', 'tomato']
    
cols = np.array(len(da) * ['k'])
for ic, c in enumerate( np.unique(clus) ): 
    cols = np.where( clus == c,  colors[ic], cols)
                
ax.scatter(da.longitude, da.latitude, color=cols, marker='^')








# do k-means
from sklearn.cluster import KMeans

k_means = KMeans(init="k-means++", n_clusters=5, n_init=10)
k_means.fit(X)
clus = k_means.labels_






        
        
        
        
        
        
        
        
    



