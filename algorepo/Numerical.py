"""
Numerical algorithms and their implementation
"""
import itertools
import timeit
import random

def fib_memoized(n):
    """
    This implementation of the fibonacci algorithm
    memoizes the prerequisites for a given 'n'. For
    instance, calculating fib_memoized(4), memoizes,
    fib_memoized(3), fib_memoized(2) and fib_memoized(1)

    RUNTIME:
    """
    def fib_d(n, l=[0, 1,1]):
        if n < len(l):
            return l, l[n]
        l, s1 = fib_d(n-1, l)
        l, s2 = fib_d(n-2, l)
        l.append(s1+s2)
        return l, s1+s2

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

    RUNTIME:
    """
    def fib_d(n, l=[0, 1,1]):
        if n < len(l):
            return l
        l.append(fib_d(n-1, l)[-1] + fib_d(n-2, l)[-2])
        return l

    return fib_d(n)

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

def fib_timer():
    def wrapper(f, *args, **kwargs):
        def wrapped():
            return f(*args, **kwargs)
        return wrapped

    fib_wrap_1 = wrapper(fib_memoized, 100)
    fib_wrap_2 = wrapper(fib_memoized_variation, 100)
    fib_wrap_3 = wrapper(fib_unmemoized_naive, 25)

    f = 'fib_wrap_'
    for i in range(1,4):
        f += str(i)
        print timeit.timeit(eval(f), number=100)
        f = f[:-1]

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

    midl = mid - 1
    midr = mid + 1

    if l[mid] > l[midl] and l[mid] > l[midr]:
        return l[mid]

    if l[-1] < l[mid]:
        return randomly_rotated_sorted_largest(l[mid:])
    else:
        return randomly_rotated_sorted_largest(l[:mid])

#def randomly_rotated_sorted_largest_test(l):
    #r = random.randrange(len(l))
    #nl = l[r:] + l[:r]
    #assert l[-1] == randomly_rotated_sorted_largest(nl)

#def fib_test(l):
    #for i in range(2, len(l)):
        #assert l[i] == (l[i-1] + l[i-2])


#def permutate_test(p):
    #l = map(lambda x:''.join(x), list(itertools.permutations(p)))
    #q = permutate(p)

    #for v in l:
        #assert v in q


#def main():
    #randomly_rotated_sorted_largest_test(list(xrange(1, 100)))
    #fib_test(fib_memoized(100))
    #fib_test(fib_memoized_variation(100))
    #fib_test(fib_unmemoized_naive(30))
    #permutate_test("12345")

#main()
