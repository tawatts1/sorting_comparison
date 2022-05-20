#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:00:00 2022

@author: ted
"""
import random
import numpy as np
import time

from sorting_obj import sorting_obj
from sorting_algs import default_sort, quick_sort, merge_sort, radix_sort, alg_names
from sort_util import get_random_integers


def run_exp(sort_objs, length_range, endpoints):
    jobs = []
    for L in length_range:
        for end in endpoints:
            lst = get_random_integers(start=0, stop=end, size=L)
            for obj in sort_objs:
                jobs.append((obj, lst, str(end)))
    random.shuffle(jobs)
    for obj, lst, k in jobs:
        print(obj.name, k, len(lst))
        try:
            algorithm_,N_,comparisons_,time_,entry_time_ = (str(val) for val in obj.run_exp(lst))
        except RecursionError:
            algorithm_,N_,comparisons_,time_,entry_time_ = (str(val) for val in [obj.name,len(lst),0,0,time.time()])
            print(f'Failure due to recursion limit: {algorithm_}, {N_}, {k}')
        newline = ','.join((algorithm_,N_,k,comparisons_,time_,entry_time_))
        if comparisons_ == '0' and time_ == '0':
            with open('data/failed_results.csv', 'a') as file:
                file.write(newline + '\n')
        else:
            with open('data/results.csv', 'a') as file:
                file.write(newline + '\n')

def run_random_exps(sort_objs,length_range, endpoints):
    jobs = []
    for L in length_range:
        for end in endpoints:
            for obj in sort_objs:
                jobs.append((obj, L, str(end)))
    random.shuffle(jobs)
    for obj, L, k in jobs:
        print(obj.name, k, L)
        run_single_exp(obj,L,k)
        
def run_single_exp(obj, L, k, fname='data/results.csv'):
    lst = get_random_integers(start=0, stop=k, size=L)
    try:
        algorithm_,N_,comparisons_,time_,entry_time_ = (str(val) for val in obj.run_exp(lst))
        out = True
    except RecursionError:
        algorithm_,N_,comparisons_,time_,entry_time_ = (str(val) for val in [obj.name,len(lst),0,0,time.time()])
        out = False

    newline = ','.join((algorithm_,N_,str(k),comparisons_,time_,entry_time_))
    if comparisons_ == '0' and time_ == '0':
        with open('data/failed_results.csv', 'a') as file:
            file.write(newline + '\n')
    else:
        with open(fname, 'a') as file:
            file.write(newline + '\n')
    return out

def traverse_qsort_failure_boundary(min_N, max_N, min_k, max_k):
    # if N is too large and k is too small, it will fail. 
    sort_obj = sorting_obj('quick_sort')
    N_factor = min_N
    k_factor = min_k
    while N_factor < max_N and k_factor < max_k:
        #increase N until an exception, then increase k. 
        print(f'{N_factor},\t{k_factor}')
        if run_single_exp(sort_obj, int(N_factor), int(k_factor)):
            # if no failure, just increase N
            N_factor *= 1.05
        else: # if there was a failure, increase k
            # but first run some more experiments
            for multiplier in [.7, .8, .9, 1.1, 1.2]:
                run_single_exp(sort_obj,int(N_factor*multiplier), int(k_factor))
            k_factor *= 1.05
    print('was N to large? (if not then k was too large.)')
    print(N_factor < max_N)
    
def run_radix(min_N, max_N, min_p, max_p):
    Ns = list(set([int(val) for val in np.linspace(min_N,max_N, 27)]))
    Ns.sort()
    ks = []
    for p in range(min_p,max_p):
        ks.extend([10**p*.95,10**p*1.05])
        ks.extend([10**p*3, 10**p*5, 10**p*8])
        ks.extend([10**p*2, 10**p*1.4])
    ks = [int(val) for val in ks]
    ks.sort()
    obj = sorting_obj('radix_sort')
    jobs = []
    for k in ks:
        for N in Ns:
            jobs.append((N,k))
    random.shuffle(jobs)
    for N,k in jobs:
        print(N,k)
        run_single_exp(obj,N,k)
    return ks,Ns

    
    
if __name__ == '__main__':
    ks,Ns = run_radix(200000,800000,1,10, fname='data/results_radix.csv')
    


