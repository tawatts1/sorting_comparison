from sort_util import swap, get_random_integers, is_sorted

def default_sort(lst):
    lst.sort()

def insertion_sort(lst):
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

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    lengths = []
    comparisons = []
    for length in range(1,50):
        x = get_random_integers(stop = 1000000, size=length)
        comp = insertion_sort(x)
        if not is_sorted(x):
            raise ValueError
        lengths.append(length)
        comparisons.append(comp)

    plt.plot(lengths, comparisons)
    plt.show()

        