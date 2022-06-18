#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 

import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import sklearn.neighbors
from scaling_obj import scaling_obj
import time

def get_results(fname, method, Nrange=None, krange=None, date_from=None):
    res = pd.read_csv(fname) 
    res = res.where(res['algorithm'] == method).dropna()
    if Nrange:
        res = res.where(res['N'] > Nrange[0]).dropna()
        res = res.where(res['N'] < Nrange[1]).dropna()
    if krange:
        res = res.where(res['k'] > krange[0]).dropna()
        res = res.where(res['k'] < krange[1]).dropna()
    if date_from:
        res = res.where(res['entry_time'] > date_from).dropna()
    return res

def plot_contour(res, key='time', logx = False, logy=False, logcolor=False, cmap='veradis', plot_location=111, sharex=None, labelbottom=True, title=None):
    '''
    
    '''
    df = res.copy()#pd.concat((res, fail))
    
    grid_x, grid_y = np.mgrid[0:1:1000j, 0:1:1000j]
    xy = np.array([[x,y] for x,y in zip(df['N'], df['k'])])    
    
    N_scaler = scaling_obj('lin')
    xy[:,0] = N_scaler.scale(xy[:,0])
    k_scaler = scaling_obj('loglin')
    xy[:,1] = k_scaler.scale(xy[:,1])
    
    gridz = griddata(xy, df[key], (grid_x, grid_y), method='nearest')
    
    ax = plt.subplot(plot_location, sharex=sharex)
    if logcolor:
        plt.contourf(N_scaler.unscale(grid_x), k_scaler.unscale(grid_y), gridz, locator = ticker.LogLocator())
    else:
        plt.contourf(N_scaler.unscale(grid_x), k_scaler.unscale(grid_y), gridz, cmap=cmap)
        
    if logx:
        plt.semilogx()
    if logy:
        plt.semilogy()
        
    if not labelbottom:
        plt.tick_params('x', labelbottom=labelbottom)
    else:
        plt.xlabel('List Length')
        
    plt.xticks(rotation=30)
    cbar = plt.colorbar(location='right')
    cbar.set_label(key)
    cbar.ax.tick_params(rotation=30)
    #plt.plot(xy[:,0],xy[:,1], 'k.')

    plt.ylabel('Sample space length')
    
    if title:
        plt.title(title)
    #plt.scatter(df['N'],df['k'], s=.5, color='black')
    return ax
    

res = get_results('data/merge_results.csv', 'merge_sort', Nrange=(1,8*10**5), krange=(5,10**10))#, date_from = time.time()-24*3600*2)
title = "Merge sort 'comparisons' and runtime\nby list length and sample space size"
ax1 = plot_contour(res, key='comparisons',logy = True, logx=False, cmap='cividis', plot_location=211, labelbottom=False, title=title)
plot1 = plot_contour(res, logy = True, logx=False, key = 'time', cmap='magma', plot_location = 212, sharex=ax1)
plt.savefig('images/merge_efficiency.png', dpi=400)
plt.show()


