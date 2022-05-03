import time
from sort_util import is_sorted


class sorting_algorithm:
    def __init__(self, name, func):
        self.name = name
        self.func = func
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
        self.lengths.append(len(lst))
        self.comparisons.append(comparisons)
        self.times.append(tf-t0)
        
    def verify_sorted(self,lst):
        return is_sorted(lst)
    

if __name__ == '__main__':
    from sorting_algs import default_sort
    default = sorting_algorithm('python sort', default_sort)
    for i in range(10):
        default.run_exp([1,10,-1,-2,3,5,100000,0.233,2,3,1])
    print(default.lengths, default.times)


