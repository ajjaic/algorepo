'''
algorepo: Test module.

Meant for use with py.test.
Write each test as a function named test_<something>.
Read more here: http://pytest.org/

Copyright 2015, Ajjai
Licensed under MIT
'''
import pytest
import itertools
import random
import string

from algorepo.basicSorts import (insert_sort_inplace,
                                    insert_sort_inplace_variation,
                                    bubble_sort_inplace,
                                    selection_sort_inplace,
                                    quicksort_middle_pivot)

from algorepo.Numerical import (merge_sorted_lists,
                                merge_sorted_lists_inplace,
                                randomly_rotated_sorted_largest,
                                fib_memoized,
                                fib_memoized_variation,
                                fib_iterative,
                                fib_unmemoized_naive,
                                permutate,
                                str_rev_recursive,
                                str_rev_inplace,
                                space_delimited_sentence_rev_inplace,
                                char_at_index_encoded_str)

class Test_basicSorts:

    @pytest.fixture
    def numlist(self):
        l = list(range(1000))
        random.shuffle(l)
        return l

    def test_insert_sort_inplace(self, numlist):
        a = numlist[:]
        assert sorted(a) == insert_sort_inplace(numlist)

    def test_insert_sort_inplace_variation(self, numlist):
        a = numlist[:]
        assert sorted(a) == insert_sort_inplace_variation(numlist)

    def test_bubble_sort_inplace(self, numlist):
        a = numlist[:]
        assert sorted(a) == bubble_sort_inplace(numlist)

    def test_selection_sort_inplace(self, numlist):
        a = numlist[:]
        assert sorted(a) == selection_sort_inplace(numlist)

    def test_quicksort_middle_pivot(self, numlist):
        a = numlist[:]
        assert sorted(a) == quicksort_middle_pivot(numlist)


class Test_Numerical:

    @pytest.fixture
    def mergelist(self):
        l = sorted(random.sample(xrange(1000), random.randint(5, 150)))
        r = sorted(random.sample(xrange(700, 1000), random.randint(5,150)))
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

    @pytest.fixture
    def rnd_str(self):
        n = random.randint(1, 9)
        rnd_str = random.sample("abcdefghijklmnopqrstuvwxyz123456789", n)
        rnd_str = ''.join(rnd_str)
        return rnd_str

    @pytest.fixture
    def rnd_sen(self):
        n = random.randint(1, 9)
        sentence = list()
        for i in range(n):
            sentence.append(self.rnd_str())

        return ' '.join(sentence)

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

    def test_fib_iterative(self, fib_helper):
        n = random.randint(100, 200)
        l = fib_iterative(n)
        assert fib_helper(l)

    def test_fib_unmemoized_naive(self, fib_helper):
        #For values of n greater than 25 the runtime
        #takes exponentially longer and longer.
        n = random.randint(5, 25)
        l = fib_unmemoized_naive(n)
        assert fib_helper(l)

    def test_permutate(self, rnd_str):
        m = dict()
        m.update(map(lambda x:(''.join(x), True), itertools.permutations(rnd_str)))
        q = permutate(rnd_str)
        if len(m) != len(q):
            assert False
        for v in q:
            assert m[v]

    def test_str_rev_recursive(self, rnd_str):
        assert str_rev_recursive(rnd_str) == ''.join(reversed(rnd_str))

    def test_str_rev_inplace(self, rnd_str):
        l = map(lambda x:x, rnd_str)
        lenl = len(l)
        str_rev_inplace(l, 0, lenl-1)
        assert ''.join(l) == ''.join(reversed(rnd_str))

    def test_space_delimited_sentence_rev_inplace(self, rnd_sen):
        t = ' '.join(reversed(rnd_sen[:].split(' ')))
        assert space_delimited_sentence_rev_inplace(rnd_sen) == t

    def test_char_at_index_encoded_str(self):
        r = (1,9)
        input_str = ''
        s = ''

        #for i in range(random.randint(*r)):
        #import pudb; pu.db
        for i in range(2):
            ws = ''.join(random.sample(string.ascii_letters, random.randint(*r)))
            n = random.randint(*r)
            input_str += ws + str(n)
            s += ws * n

        n = random.randrange(0, len(s))
        if not char_at_index_encoded_str(input_str, n) == s[n]:
            import pudb; pu.db
            char_at_index_encoded_str(input_str, n)






















