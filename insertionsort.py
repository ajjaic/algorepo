def insert_sort(arr):

    arrlen = len(arr)

    for i in range(1, arrlen):
        cmpindex = i - 1

        if arr[cmpindex] > arr[i]:

