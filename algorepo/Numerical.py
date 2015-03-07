"""
Numerical algorithms and their implementation
"""

def fib_memoized(n):
    """
    This implementation of the fibonacci algorithm
    memoizes the prerequisites for a given 'n'. For
    instance, calculating fib_memoized(4), memoizes,
    fib_memoized(3), fib_memoized(2) and fib_memoized(1)
    'n' cannot be greater than a certain limit, since beyond a
    certain value of 'n', this function reaches python's stack
    size limit.

    RUNTIME:
    """
    def fib_d(n, l=[0, 1,1]):
        if n < len(l):
            return l, l[n]
        l, s1 = fib_d(n-1, l)
        l, s2 = fib_d(n-2, l)
        t = s1+s2
        l.append(t)
        return l, t

    l, _ = fib_d(n)
    return l

def fib_memoized_variation(n):
    """
    This implementation of the fibonacci algorithm memoizes
    the prerequisites for a given 'n'. For instance, calculating
    fib_memoized(4), memoizes, fib_memoized(3), fib_memoized(2)
    and fib_memoized(1). The difference in this implementation
    and 'fib_memoized' is only in the re-ordering of statements
    to write it succinctly. No significant difference in runtime.
    'n' cannot be greater than a certain limit, since beyond a
    certain value of 'n', this function reaches python's stack
    size limit.

    RUNTIME:
    """
    def fib_d(n, l=[0, 1,1]):
        if n < len(l):
            return l
        l.append(fib_d(n-1, l)[-1] + fib_d(n-2, l)[-2])
        return l

    return fib_d(n)


def fib_iterative(n):
    """
    This is an iterative version of the fibonacci algorithm. And the
    simplest. A list is initialized with some starting values in the
    fibonacci series. The subsequent values are calculated as the sum
    of the values in the previous 2 indexes. This version, can calculate
    the series without any problems of reaching python's stack depth limit.

    RUNTIME:
    """
    l, i = [0, 1], 2
    n -= 2
    while n > 0:
        l.append(l[i-1]+l[i-2])
        i += 1
        n -= 1

    return l

def fib_unmemoized_naive(n):
    """
    This is the unmemoized, naive implementation of the fibonacci
    algorithm. The differences in runtime between this
    implementation and the implementations in 'fib_memoized'
    and 'fib_memoized_variation' are very significant.
    This implementation runs many orders of runtime, slower than
    either of the other 2 implementations

    RUNTIME:
    """
    def fib(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    l = list()
    for i in range(1, n+1):
        v = fib(i)
        l.append(v)
    return l

def permutate(s):
    """
    Naive implementation of permutation algorithm to
    permutate a string of symbols

    RUNTIME:
    """
    if len(s) == 1:
        return [s]

    l = permutate(s[1:])

    pl = list()
    for i in range(len(s)):
        for w in l:
            pl.append(w[:i] + s[0] + w[i:])

    return pl

def randomly_rotated_sorted_largest(l):
    """
    Algorithm to find the largest element in a sorted list
    that is also rotated

    RUNTIME:
    """

    llen = len(l)
    if llen == 1:
        return l[0]
    if llen == 2:
        return max(l[0], l[1])

    mid = (llen-1)/2

    if l[mid] > l[-1]:
        return randomly_rotated_sorted_largest(l[mid:])
    else:
        return randomly_rotated_sorted_largest(l[:(mid+1)])

def merge_sorted_lists_inplace(arr, (left_l, left_r), (right_l, right_r)):
    """
    Given a list and a pair of indices delimiting 2 sections
    of the list that are sorted, this function merges both
    the sections into 1 sorted section. The difference
    between this one and 'merge_sorted_lists' is that, in
    'merge_sorted_lists', a new temporary list is used for
    merging both the lists. Whereas in this one, no new
    temporary list is used for placing the final sorted list.

    RUNTIME:
    """
    templ = [arr[right_l]]
    right_l += 1

    while left_l <= left_r and right_l <= right_r:
        _, i = min((templ[0], 't'), (arr[left_l], 'l'), (arr[right_l], 'r'))

        if i == 'l':
            left_l += 1
        elif i == 't':
            if arr[left_l] < arr[right_l]:
                templ.append(arr[left_l])
                arr[left_l] = templ[0]
                templ = templ[1:]
                left_l += 1
            else:
                templ.append(arr[right_l])
                right_l += 1
        else:
            templ.append(arr[left_l])
            arr[left_l] = arr[right_l]
            right_l += 1

    m = right_l - (left_r - left_l) - 1
    for i in range(left_l, left_r+1):
        arr[m] = arr[i]
        m += 1

    for i,j in zip(range(left_l, right_l), range(len(templ))):
        arr[i] = templ[j]

    return arr

def merge_sorted_lists(arr, l1, r1, l2, r2):
    """
    Given a list and a pair of indices delimiting 2 sections
    of the list that are sorted, this function merges both
    the sections into 1 sorted section. This one makes use of
    a temporary list that is the size of both the sublists
    combined.

    RUNTIME:
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

    return arr

def combo(s, k):
    def fn(ss, kk, pre, combos):
        if not kk:
            combos.append(pre)
            return

        lenss = len(ss)
        for i in range(lenss-kk+1):
            fn(ss[i+1:], kk-1, pre+ss[i], combos)

        return combos

    return fn(s, k, '', list())

def numbo(numlist, num, size):

    def helper(l, s, nl):
        if not s:
            return nl

        for i in range(len(l)):
            nl.append(l[i])
            nl = helper(l[i+1:], s-1, nl)

            if len(nl) == size and sum(nl) == num:
                break
            else:
                nl = nl[:-1]

        return nl


    m = list()
    helper(numlist, size, m)
    return m


def kadane(l):
    max_till_here = 0
    max_so_far = 0

    m = list()
    for i in l:
        max_till_here += i
        if max_till_here < 0:
            m = list()
            max_till_here = 0

        if max_so_far < max_till_here:
            max_so_far = max_till_here

    return m, max_so_far

def subseqtarget(la, t):
    i = 0
    lalen = len(la)

    while i < lalen:
        s = i+1
        while s <= lalen:
            numl = la[i:s]
            ss = sum(numl)
            if ss == t:
                return numl
            if ss > t:
                break
            s += 1

        i += 1

    return []

def monies(coins, t):

    def helper(l, m, cns):

        for i, j in zip(cns, range(len(cns))):
            suml = sum(l)
            if suml == t:
                m.append(l)
                return l, m
            elif suml > t:
                return l, m
            else:
                l.append(i)
                l, m = helper(l, m, cns[j:])
                l = l[:-1]

        return l, m

    _, m = helper(list(), list(), coins)
    return m


def kth(l, k):

    def helper(l, i, j):
        l[k], l[j] = l[j], l[k]

        lessthanp = 0
        for m in range(j):
            if l[m] < l[j]:
                l[lessthanp], l[m] = l[m], l[lessthanp]
                lessthanp += 1
        l[lessthanp], l[j] = l[j], l[lessthanp]

        return lessthanp

    i = 0
    j = len(l)-1
    while True:
        nk = helper(l, i, j)
        if k == nk:
            return l[k]
        elif k < nk:
            j = nk-1
        else:
            i = nk+1


def subsequences(s):

    def helper(seq, size, l):

        if len(seq) < size:
            return l

        subseq = seq[:size]
        l.append(subseq)
        l = helper(seq[1:], size, l)

        return l

    l = []
    for size in range(1, len(s)):
        l.extend(helper(s, size, list()))

    return l


def colorfulNumber(s):
    s_dict = dict()
    for num in subsequences(s):
        if len(num) == 1:
            product_s = int(num)
        else:
            product_s = reduce(lambda x, y: int(x) * int(y), num)

        if s_dict.has_key(product_s):
            return False
        s_dict[product_s] = None
    return True

def pythonHash(s):
    slen = len(s)
    p = 0
    x = long(ord(s[p])) << 7
    while p < slen:
        x = (1000003 * x) ^ long(ord(s[p]))
        p += 1

    x = x ^ slen
    return x & (slen-1)

print pythonHash("ajai")
print pythonHash("a")
print pythonHash("ab")
