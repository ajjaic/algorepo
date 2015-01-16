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
class Test_basicSorts:

    @pytest.fixture
    def numlist(self):
        l = list(range(100))
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
