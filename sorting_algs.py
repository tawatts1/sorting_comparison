from sort_util import swap, get_random_integers, is_sorted

def default_sort(lst):
    lst.sort()
    return 0 # return 0 for comparisons

def insertion_sort(lst):
    '''
    Simplest sorting algorithm. Has deterministic number of comparisons - 
    0 + 1 + 2 + 3 + ... + N-1 + N
    and is O(n**2)
    '''
    L = len(lst)
    comparisons = 0
    for i in range(L):
        #minimum = float('inf')
        min_j = i
        for j in range(i+1,L):
            comparisons += 1 # for the line directly below
            if lst[min_j] > lst[j]:
                #minimum = lst[j]
                min_j = j
        if i != min_j:
            swap(lst,i,min_j)
    return comparisons

def quick_sort(lst):
    '''
    uses last element of list as pivot, puts everything smaller to the left,
    puts everything greater to the right, and continues recursively
    '''
    
    def partition(lst, x, y, comparisons):
        i = x-1
        pivot = lst[y]
        for j in range(x,y):
            comparisons[0] += 1
            if lst[j] < pivot:
                i += 1
                swap(lst,i,j)
        swap(lst,i+1,y)
        return i + 1
    def qsort(lst,x,y, comparisons):
        comparisons[0] += 1
        if x < y:
            i = partition(lst,x,y, comparisons)
            qsort(lst,x,i-1, comparisons)
            qsort(lst,i+1,y, comparisons)
    comparisons = [0]
    qsort(lst,0,len(lst)-1, comparisons)
    return comparisons[0]

    


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    lengths = []
    comparisons = []
    for length in range(1,50):
        x = get_random_integers(stop = 1000000, size=length)
        comp = quick_sort(x)
        if not is_sorted(x):
            raise ValueError
        lengths.append(length)
        comparisons.append(comp)

    plt.plot(lengths, comparisons)
    plt.show()

        