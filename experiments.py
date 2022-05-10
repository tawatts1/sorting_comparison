#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:00:00 2022

@author: ted
"""
import random
import numpy as np

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
        algorithm_,N_,comparisons_,time_,entry_time_ = (str(val) for val in obj.run_exp(lst))
        newline = ','.join((algorithm_,N_,k,comparisons_,time_,entry_time_))
        with open('data/results.csv', 'a') as file:
            file.write(newline + '\n')


if __name__ == '__main__':
    sorting_obj_dict = {name:sorting_obj(name) for name in alg_names}
    #sorting_obj_dict.pop('default_sort')
    #sorting_obj_dict.pop('insertion_sort')
    sorting_objs = [sorting_obj_dict[name] for name in sorting_obj_dict.keys()]
    ranges = [int(val) for val in np.geomspace(100,10**4,10)]
    ks = (10**2,10**3, 10**6)
    run_exp(sorting_objs, ranges, ks)


