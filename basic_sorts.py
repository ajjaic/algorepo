def insert_sort_inplace(arr):
    """
    Sort all the elements in a list in place.
    As the elements are picked off from one end
    of the list, they are put in sorted order,
    at the other end.

    BIG(O):
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

    BIG(O):
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

    BIG(O): N^2
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

    BIG(O):
    """

    arrlen = len(arr)

    for i in range(0, arrlen - 1):
        cm = i
        for j in range(i+1, arrlen):
            if arr[j] < arr[cm]:
                cm = j
        arr[i], arr[cm] = arr[cm], arr[i]

    return arr

def quicksort_middle_pivot(arr):
    """
    Divide and Conquer algorithm. List broken down
    into smaller and smaller lists and then sorted.
    This is not inplace. Every recursive call
    creates 2 extra lists. Middle element is used
    as pivot

    BIG(O):
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

def sorting_test(fn, *args):
    """
    This is a test function that takes a function
    as input and calls the function with a random
    list of numbers. Verifies that the returned
    list is sorted.
    """
    import random
    rndlist = random.sample(xrange(100), 15)
    if args:
        rndlist = fn(rndlist, *args)
    else:
        rndlist = fn(rndlist)

    for i in range(1, len(rndlist)):
        if rndlist[i] < rndlist[i-1]:
            print "Error at Index: ", i
            return False

    return True

def main():
    assert sorting_test(insert_sort_inplace)
    assert sorting_test(insert_sort_inplace_variation)
    assert sorting_test(bubble_sort_inplace)
    assert sorting_test(selection_sort_inplace)
    assert sorting_test(quicksort_middle_pivot)

main()
