#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 13:41:27 2022

@author: ted
"""

import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
import sklearn.neighbors

def get_succ_fail():
    res = pd.read_csv('data/results.csv')
    fail = pd.read_csv('data/failed_results.csv')
    
    res = res.where(res['algorithm'] == 'quick_sort').dropna()
    res = res.where(res['N'] < 400000).dropna()
    res = res.where(res['k'] < 400).dropna()
    fail = fail.where(fail['algorithm'] == 'quick_sort').dropna()
    fail = fail.where(fail['N'] < 400000).dropna()
    fail = fail.where(fail['k'] < 400).dropna()
    return res,fail

def plot_categories(res,fail):
    '''
    This plots a simple scatter plot where I show the succesfully sorted length-sample size
    pairs in blue, and the failures in red. 
    '''
    plt.scatter(res['N'], res['k'], label='Succesful sorts', s=1, color='blue')
    plt.scatter(fail['N'], fail['k'], label= 'Failed sorts', s=1, color='red')
    plt.legend()
    plt.xticks(rotation=30)
    plt.ylabel('Sample space length')
    plt.xlabel('List length')
    plt.title('Quick sort failure by list length and\nsample space length')
    plt.savefig('images/qsort_failure_boundary.png',dpi=300)
    plt.show() 

def plot_contour(res):
    '''
    This plots the contours using list length and sample space as x and y, 
    and number of comparisons during sorting as the z or color axis. 
    Note that by a sample space of size 100, I mean all elements of the random
    list were drawn from the integers 0,1,...98,99
    
    The special thing about this plot is that I use interpolation. To do this,
    I scale the data down by dividing it by the max. Then I use scipy griddata
    and un-scale the data before I plot it. 
    '''
    df = res.copy()#pd.concat((res, fail))
    
    minx, maxx = min(df['N']), max(df['N'])
    miny, maxy = min(df['k']), max(df['k'])
    for key in ['k','N']:
        df[key] = df[key]/max(df[key])
    grid_x, grid_y = np.mgrid[0:1:200j, 0:1:200j]
    xy = np.array([[x,y] for x,y in zip(df['N'], df['k'])])
    
    gridz = griddata(xy, df['comparisons'], (grid_x, grid_y), method='cubic')
    plt.contourf(grid_x*maxx, grid_y*maxy, gridz, locator = ticker.LogLocator())
    plt.plot(xy[:,0],xy[:,1], 'k.', ms=1)
    plt.xticks(rotation=30)
    cbar = plt.colorbar()
    cbar.set_label('Number of comparisons')
    cbar.ax.tick_params(rotation=30)

    plt.xlabel('List length')
    plt.ylabel('Sample space length')
    plt.title('Quick sort efficiency by list length and\nsample space length')
    plt.savefig('images/qsort_efficiency_near_failure.png', dpi=300)
    plt.show()


res,fail = get_succ_fail()
plot_categories(res,fail)
plot_contour(res)