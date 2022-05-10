import time
from sort_util import is_sorted
from sorting_algs import alg_names, algs, default_sort, quick_sort, merge_sort

name_to_alg = {string:func for string,func in zip(alg_names, algs)}

class sorting_obj:
    def __init__(self, name):
        self.name = name
        if name not in name_to_alg.keys():
            raise ValueError
        self.func = name_to_alg[name]
        self.lengths = []
        self.comparisons = []
        self.times = []
    def run_exp(self,lst):
        out = lst.copy()
        t0 = time.time()
        comparisons = self.func(out)
        if comparisons is None:
            comparisons = 0
        tf = time.time()
        if not self.verify_sorted(out):
            raise ValueError
        self.lengths.append(len(out))
        self.comparisons.append(comparisons)
        self.times.append(tf-t0)
        return self.name, len(out), comparisons, tf-t0, tf
        
    def verify_sorted(self,lst):
        return is_sorted(lst)
    

if __name__ == '__main__':
    default = sorting_obj('python_sort')
    for i in range(10):
        default.run_exp([1,10,-1,-2,3,5,100000,0.233,2,3,1])
    print(default.lengths, default.times)


