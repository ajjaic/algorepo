import random

def insert_sort_inplace(arr):
    """
    Sort all the elements in a list in place.
    As the elements are picked off from one end
    of the list, they are put in sorted order,
    at the other end.

    RUNTIME: Best - O(n), Avg - O(n^2),
             Worst - O(n^2)
    """

    arrlen = len(arr)

    for i in range(1, arrlen):
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def insert_sort_inplace_variation(arr):
    """
    Same as 'insert_sort_inplace'. Difference
    being that, newly inserted elements are
    inserted from the end of the sorted part of
    the list.

    RUNTIME: Best - O(n), Avg - O(n^2),
             Worst - O(n^2)
    """
    arrlen = len(arr)

    for i in range(1, arrlen):
        for j in range(i-1, -1, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j #inner loop uses 'i' at point of
                      #initialization. #outerloop
                      #re-initializes 'i'
                j -= 1
            else:
                break


    return arr

#A useless algorithm.
#Not as bad as bogosort and bozosort though
def bubble_sort_inplace(arr):
    """
    Traverse the list as many times as the
    number of elements. In each traversal,
    the largest element bubbles up to the top.

    RUNTIME: Best - O(n), Avg - O(n^2),
             Worst - O(n^2)
    """
    arrlen = len(arr)

    for i in range(arrlen-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def selection_sort_inplace(arr):
    """
    Every iteration through the list, find
    the smallest element and swap it with
    the last index in the sorted part of the
    list.

    RUNTIME: Best - O(n^2), Avg - O(n^2),
             Worst - O(n^2)
    """

    arrlen = len(arr)

    for i in range(0, arrlen - 1):
        cm = i
        for j in range(i+1, arrlen):
            if arr[j] < arr[cm]:
                cm = j
        arr[i], arr[cm] = arr[cm], arr[i]

    return arr

def pivot_partition(arr, lefti, righti, pivoti):
    """
    Partition algorithm used by median sort to split
    items based on pivot. Left side of pivot are items
    smaller than pivot. Right side are items greater
    than pivot.

    RUNTIME: Worst - O(n^2)
    """
    arr[righti], arr[pivoti] = arr[pivoti], arr[righti]

    correct_pivoti = lefti
    for i in range(lefti, righti):
        if arr[i] <= arr[righti]:
            arr[correct_pivoti], arr[i] = arr[i], arr[correct_pivoti]
            correct_pivoti += 1

    arr[correct_pivoti], arr[righti] = arr[righti], arr[correct_pivoti]

    return correct_pivoti


def median_element(arr, ki, lefti, righti):
    """
    This finds the actual median element by partitioning
    the array multiple times until median element is found
    """
    while True:
        pivoti = random.randint(lefti, righti)
        newp = pivot_partition(arr, lefti, righti, pivoti)
        if newp == ki:
            break
        elif ki < newp:
            righti = newp - 1
        else:
            lefti = newp + 1

    return arr


def median_sort_inplace(arr, lefti, righti):
    #TODO: Runtime needs confirmation
    """
    Sorts the elements by recursively finding the
    median of the arr, their sub-arrays and so on.

    RUNTIME: Best - O(n log n), Avg - O(n log n),
             Worst - O(n^2)
    """
    if righti <= lefti:
        return
    ki = lefti + (righti - lefti + 1)/2

    median_element(arr, ki, lefti, righti)

    median_sort_inplace(arr, lefti, ki-1)
    median_sort_inplace(arr, ki+1, righti)

    return arr

def merge_sorted_lists(arr, l1, r1, l2, r2):
    """
    Given 2 sorted lists of varying lengths, it
    merges both the list and preserve the sorting
    order in the process

    RUNTIME: O(N)
    """
    minl = min(l1,l2)
    maxr = max(r1, r2)
    sortedsize = maxr - minl + 1
    sortedarr = [0] * sortedsize
    sortedi = 0

    while l1 <= r1 and l2 <= r2:
        if arr[l1] <= arr[l2]:
            sortedarr[sortedi] = arr[l1]
            l1 += 1
            sortedi += 1
        elif arr[l2] <= arr[l1]:
            sortedarr[sortedi] = arr[l2]
            l2 += 1
            sortedi += 1

    while l1 <= r1:
        sortedarr[sortedi] = arr[l1]
        sortedi += 1
        l1 += 1

    while l2 <= r2:
        sortedarr[sortedi] = arr[l2]
        sortedi += 1
        l2 += 1

    for i, j  in zip(range(minl, maxr+1), range(sortedsize)):
        arr[i] = sortedarr[j]


def merge_sort_inplace(arr, lefti, righti):
    """
    Sorts the array by iteratively splitting the array
    into smaller and smaller array until, the array
    cannot be split anymore at which point they are
    joined together using the algorithm to merge 2
    sorted lists. The merges take place from inside out.

    RUNTIME: Best - O(n log n), Avg - O(n log n),
             Worst - O(n log n)
    """
    size = righti - lefti + 1
    if size < 2:
        return
    half = size/2 + lefti - 1

    merge_sort_inplace(arr, lefti, half)
    merge_sort_inplace(arr, half+1, righti)

    merge_sorted_lists(arr, lefti, half, half+1, righti)

    return arr


def quicksort_middle_pivot(arr):
    """
    Divide and Conquer algorithm. List broken down
    into smaller and smaller lists and then sorted.
    This is not inplace. Every recursive call
    creates 2 extra lists. Middle element is used
    as pivot

    RUNTIME: Best - O(n log n), Avg - O(n log n),
             Worst - O(n^2)
    """
    lenarr = len(arr)
    if lenarr <= 1:
        return arr
    pivot = lenarr/2

    lessp = list()
    largerp = list()

    for v in range(pivot):
        if arr[v] <= arr[pivot]:
            lessp.append(arr[v])
        else:
            largerp.append(arr[v])

    for v in range(pivot+1, lenarr):
        if arr[v] <= arr[pivot]:
            lessp.append(arr[v])
        else:
            largerp.append(arr[v])

    sleft = quicksort_middle_pivot(lessp)
    sright = quicksort_middle_pivot(largerp)

    sleft.append(arr[pivot])
    sleft.extend(sright)
    return sleft


def radix_sort(arr, minradix, maxradix):
    #TODO: Take another parameter that gives the max number of
    #      digits/chars for any single element in array
    """
    An implementation of MSD radix sort. Sorts elements
    based on the individual digits in the number or
    characters in a string. The runtime depends on the
    size of the array and the number of digits or characters
    in the biggest number or string respectively.

    RUNTIME: (nk)
    """
    if minradix >= maxradix:
        return arr
    buckets = dict()


    for v in arr:
        val_index = int(str(v)[minradix])
        l = buckets.get(val_index, [])
        l.append(v)
        buckets[val_index] = l

    for i in buckets.iterkeys():
        if len(buckets[i])>1:
            buckets[i] = radix_sort(buckets[i], minradix+1, maxradix)

    l = list()
    #for i in range(10):
        #l.extend(buckets.get(i, []))
    for i in sorted(buckets.keys()):
        l.extend(buckets[i])

    return l

def bucket_sort():
    pass

def sorting_test(fn, rndlist, *args):
    """
    This is a test function that takes a function
    as input and calls the function with a random
    list of numbers. Verifies that the returned
    list is sorted.
    """

    if args:
        rndlist = fn(rndlist, *args)
    else:
        rndlist = fn(rndlist)

    for i in range(1, len(rndlist)):
        if rndlist[i] < rndlist[i-1]:
            print rndlist
            print "Error at Index: ", i
            return False

    return True

def mk_rnd_ls(mn, mx, totalnums):
    l = [0] * totalnums
    for i in range(totalnums):
        l[i] = random.randint(mn, mx)
    return l

def counting_sort(arr, mx):
    """
    Used for sorting a list of elements N where
    each element is in the range [0, k). Counting
    sort is a good algorithm in situations where
    N is much greater than k.

    RUNTIME: Best - O(n), Avg - O(n), Worst - O(n)
    """
    mx += 1 #This is to compensate for the fact that counting sort
            #can only sort from [0, k).
    s = [0] * mx

    for v in arr:
        s[v] += 1

    idx = 0
    for i in range(mx):
        while s[i] > 0:
            arr[idx] = i
            idx += 1
            s[i] -= 1

    return arr


def main():
    for i in range(100):
        mn, mx, totalnums = 100, 500, 50
        assert sorting_test(insert_sort_inplace, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(insert_sort_inplace_variation, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(bubble_sort_inplace, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(selection_sort_inplace, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(quicksort_middle_pivot, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(merge_sort_inplace, mk_rnd_ls(mn, mx, totalnums), 0, totalnums-1)
        assert sorting_test(median_sort_inplace, mk_rnd_ls(mn, mx, totalnums), 0, totalnums-1)

    for i in range(100):
        counting_sort_list = mk_rnd_ls(0, 8, 200)
        assert sorting_test(counting_sort, counting_sort_list, max(counting_sort_list))

    for i in range(100):
        assert sorting_test(radix_sort, mk_rnd_ls(10, 99, 15), 0, 2)

main()
