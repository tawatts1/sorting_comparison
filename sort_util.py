from numpy.random import randint

def swap(lst,i,j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def is_sorted(lst):
    return all([lst[i]<=lst[i+1] for i in range(len(lst)-1)])

def get_random_integers(start=0,stop=1000,size=10):
    '''returns list of integers of length size, with values from 
    [start,stop)'''
    return randint(low=start,high=stop,size=size)


    


