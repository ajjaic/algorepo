'''
algorepo: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2015, Ajjai
Licensed under MIT
'''
import pytest
import random

from algorepo.basicSorts import (insert_sort_inplace,
                                    insert_sort_inplace_variation,
                                    bubble_sort_inplace,
                                    selection_sort_inplace,
                                    quicksort_middle_pivot,
                                    merge_sort_inplace,
                                    median_sort_inplace,
                                    heap_sort_arr,
                                    counting_sort,
                                    radix_sort)

from algorepo.Numerical import (merge_sorted_lists_inplace,
                                merge_sorted_lists,
                                fib_memoized,
                                fib_memoized_variation,
                                fib_unmemoized_naive,
                                permutate,
                                randomly_rotated_sorted_largest)
#class Test_basicSorts:

    #@pytest.fixture
    #def numlist(self):
        #l = list(range(1000))
        #random.shuffle(l)
        #return l

    #def test_insert_sort_inplace(self, numlist):
        #a = numlist[:]
        #assert sorted(a) == insert_sort_inplace(numlist)

    #def test_insert_sort_inplace_variation(self, numlist):
        #a = numlist[:]
        #assert sorted(a) == insert_sort_inplace_variation(numlist)

    #def test_bubble_sort_inplace(self, numlist):
        #a = numlist[:]
        #assert sorted(a) == bubble_sort_inplace(numlist)

    #def test_selection_sort_inplace(self, numlist):
        #a = numlist[:]
        #assert sorted(a) == selection_sort_inplace(numlist)

    #def test_quicksort_middle_pivot(self, numlist):
        #a = numlist[:]
        #assert sorted(a) == quicksort_middle_pivot(numlist)


class Test_Numerical:

    @pytest.fixture
    def mergelist(self):
        l = sorted(random.sample(xrange(1000), random.randint(5, 15)))
        r = sorted(random.sample(xrange(700, 1000), random.randint(5,15)))
        lenl, lenr = len(l), len(r)
        lrange = 0, lenl-1
        rrange = lenl, lenl+lenr-1

        return l+r, lrange, rrange

    @pytest.fixture
    def fib_helper(self):
        def wrapper(l):
            m = True
            for i in range(2, len(l)):
                m = m and (l[i] == (l[i-1] + l[i-2]))
                if not m:
                    break
            return m
        return wrapper

    def test_merge_sorted_lists(self, mergelist):
        l, (ll, lr), (rl, rr) = mergelist
        assert sorted(l) == merge_sorted_lists(l, ll, lr, rl, rr)

    def test_merge_sorted_lists_inplace(self, mergelist):
        l, lr, rr = mergelist
        assert sorted(l) == merge_sorted_lists_inplace(l, lr, rr)

    def test_randomly_rotated_sorted_largest(self):
        l = sorted(random.sample(xrange(1000),500))
        r = random.randrange(len(l))
        nl = l[r:] + l[:r]
        assert l[-1] == randomly_rotated_sorted_largest(nl)

    def test_fib_memoized(self, fib_helper):
        n = random.randint(100, 200)
        l = fib_memoized(n)
        assert fib_helper(l)

    def test_fib_memoized_variation(self, fib_helper):
        n = random.randint(100, 200)
        l = fib_memoized_variation(n)
        assert fib_helper(l)

    def test_fib_unmemoized_naive(self, fib_helper):
        n = random.randint(5, 25)
        l = fib_unmemoized_naive(n)
        assert fib_helper(l)

    #def test_permutate(p):
        #l = map(lambda x:''.join(x), list(itertools.permutations(p)))
        #q = permutate(p)

        #for v in l:
            #assert v in q
