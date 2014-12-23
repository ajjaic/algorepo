def insert_sort_inplace(arr):

    arrlen = len(arr)

    for i in range(1, arrlen):
        for j in range(0, i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def insert_sort_inplace_variation(arr):
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



def sorting_test(fn):
    rndlist = produce_test_input()
    rndlist = fn(rndlist)

    for i in range(1, len(rndlist)):
        if rndlist[i] < rndlist[i-1]:
            print "Error at Index: ", i
            return False

    return True


def produce_test_input():
    import random
    return random.sample(xrange(100), 15)

def main():
    assert sorting_test(insert_sort_inplace)
    assert sorting_test(insert_sort_inplace_variation)

main()
