"""
The heap datastructure implemented as an Array/List
"""

def heapify(heap, cmpfn):
    def hh(heap, pi, maxi, cmpfn):
        l = (2*pi)+1
        r = (2*pi)+2

        mx = pi
        mx = l if l <= maxi and cmpfn(heap[l], heap[mx]) == 1 else mx
        mx = r if r <= maxi and cmpfn(heap[r], heap[mx]) == 1 else mx

        if cmpfn(heap[mx], heap[pi]) == 1:
            heap[pi], heap[mx] = heap[mx], heap[pi]
            hh(heap, mx, maxi, cmpfn)

    alen = len(heap)
    maxi = alen - 1
    pi = maxi/2

    for i in range(pi, -1, -1):
        hh(heap, i, maxi, cmpfn)

    return heap


def heap_insert(heap, cmpfn, v):
    heap.append(v)
    lsteli = len(heap) - 1
    pi = (lsteli - 1)/2

    while pi >= 0 and cmpfn(heap[pi], heap[lsteli]) == -1:
        heap[pi], heap[lsteli] = heap[lsteli], heap[pi]
        lsteli = pi
        pi = (pi - 1)/2

    return heap

def extract_max(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    mx = heap[-1]
    heap = heap[:-1]
    if heap:
        heap = heapify(heap, cmp)
    return heap, mx

def heap_sort(heap):
    l = list()
    for i in range(len(heap)):
        heap, mx = extract_max(heap)
        l.append(mx)
    return l

l = [4, 10, 7, 1, 83, 47, 53,26, 31]
l = heapify(l, cmp)
print heap_sort(l)
l = list(range(10))
l = heapify(l, cmp)
print heap_sort(l)

