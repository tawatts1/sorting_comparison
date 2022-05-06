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
        if x < y:
            i = partition(lst,x,y, comparisons)
            qsort(lst,x,i-1, comparisons)
            qsort(lst,i+1,y, comparisons)
    comparisons = [0]
    qsort(lst,0,len(lst)-1, comparisons)
    return comparisons[0]

def merge_sort(lst):
    '''
    This merge sort is worse than regular merge sort because it uses
    '''
    def msort(lst, comparisons):
        if len(lst) > 1:
            mid = len(lst) // 2
            
            left = lst[:mid] # full copy of left side
            right = lst[mid:] #full copy of right side
            msort(left, comparisons)
            msort(right, comparisons)
            
            l_i = r_i = 0
            len_left = len(left)
            len_right = len(right)
            while l_i < len_left and r_i < len_right:
                comparisons[0] += 1
                if left[l_i] < right[r_i]:
                    lst[l_i + r_i] = left[l_i]
                    l_i += 1
                else:
                    lst[l_i + r_i] = right[r_i]
                    r_i += 1
            if l_i != len_left:
                lst[l_i + r_i:] = left[l_i:]
            elif r_i != len_right:
                lst[l_i + r_i:] = right[r_i:]
    comparisons = [0]
    msort(lst, comparisons)
    return comparisons[0]


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    lengths = []
    comparisons = []
    for length in range(1,50):
        x = list(get_random_integers(stop = 10**4, size=length))
        comp = merge_sort(x)
        if not is_sorted(x):
            raise ValueError
        lengths.append(length)
        comparisons.append(comp)

    plt.plot(lengths, comparisons)
    plt.show()

        