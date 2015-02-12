"""
The heap datastructure implemented as an Array/List
"""
#TODO: Doc strings required
#TODO: Refactor into class
def heapify(heap, hlen, cmpfn):
    def hh(heap, pi, halfwayi, maxi, cmpfn):
        l = (2*pi)+1
        r = (2*pi)+2

        mx = pi
        mx = l if l <= maxi and cmpfn(heap[l], heap[mx]) == 1 else mx
        mx = r if r <= maxi and cmpfn(heap[r], heap[mx]) == 1 else mx

        if cmpfn(heap[mx], heap[pi]) == 1:
            heap[pi], heap[mx] = heap[mx], heap[pi]
            if mx <= halfwayi:
                hh(heap, mx, halfwayi, maxi, cmpfn)

    maxi = hlen - 1
    halfwayi = maxi/2

    for i in range(halfwayi, -1, -1):
        hh(heap, i, halfwayi, maxi, cmpfn)

    return heap

def max_heapify(arr, cmpfn):
    arrl = len(arr)
    halfwayi = (arrl/2) - 1

    def sub_heapify(p):
        while p <= halfwayi:
            l = (2*p) + 1
            r = (2*p) + 2

            mxi = l if l < arrl and cmpfn(arr[l], arr[p]) == 1 else p
            mxi = r if r < arrl and cmpfn(arr[r], arr[mxi]) == 1 else mxi

            if p != mxi:
                arr[p], arr[mxi] = arr[mxi], arr[p]
                p = mxi
            else:
                break

    for i in range(halfwayi, -1, -1):
        sub_heapify(i)

    return arr



def heap_insert(heap, cmpfn, v):
    heap.append(v)
    lsteli = len(heap) - 1
    pi = (lsteli - 1)/2

    while pi >= 0 and cmpfn(heap[pi], heap[lsteli]) == -1:
        heap[pi], heap[lsteli] = heap[lsteli], heap[pi]
        lsteli = pi
        pi = (pi - 1)/2

    return heap

def extract_max(heap, lheap):
    if lheap == 1:
        return [], heap[0]

    heap[0], heap[-1] = heap[-1], heap[0]
    mx = heap[-1]
    heap = heap[:-1]
    lheap -= 1
    if lheap != 1:
        heap = heapify(heap, lheap, cmp)
    return heap, mx

def heap_depth(heap, maxi, i):
    if i>maxi:
        return 0
    left_sub_tree = 1 + heap_depth(heap, maxi, (2*i)+1)
    right_sub_tree = 1 + heap_depth(heap, maxi, (2*i)+2)

    return max(left_sub_tree, right_sub_tree)
