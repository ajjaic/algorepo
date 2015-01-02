from basic_sorts import sorting_test
from basic_sorts import mk_rnd_ls
from basic_sorts import insert_sort_inplace
from basic_sorts import insert_sort_inplace_variation
from basic_sorts import bubble_sort_inplace
from basic_sorts import selection_sort_inplace
from basic_sorts import quicksort_middle_pivot
from basic_sorts import merge_sort_inplace
from basic_sorts import median_sort_inplace
from basic_sorts import heap_sort_arr
from basic_sorts import counting_sort
from basic_sorts import radix_sort

def main():
    for i in range(100):
        mn, mx, totalnums = 100, 500, 50
        assert sorting_test(insert_sort_inplace, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(insert_sort_inplace_variation, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(bubble_sort_inplace, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(selection_sort_inplace, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(quicksort_middle_pivot, mk_rnd_ls(mn, mx, totalnums))
        assert sorting_test(merge_sort_inplace, mk_rnd_ls(mn, mx, totalnums), 0, totalnums-1)
        assert sorting_test(median_sort_inplace, mk_rnd_ls(mn, mx, totalnums), 0, totalnums-1)
        assert sorting_test(heap_sort_arr, mk_rnd_ls(mn, mx, totalnums))

    for i in range(100):
        l = mk_rnd_ls(0, 8, 200)
        assert sorting_test(counting_sort, l, max(l))

    for i in range(100):
        assert sorting_test(radix_sort, mk_rnd_ls(10, 99, 15), 0, 2)

main()
