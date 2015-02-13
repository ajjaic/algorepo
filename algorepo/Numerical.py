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

def str_rev_recursive(s):
    """
    Reversing a string recursively. As long as 's' is not too long,
    this function will reverse a given string. If 's' is too long,
    then this function might reach the maximum stack depth and crash.

    RUNTIME:
    """
    if len(s) == 1:
        return s
    else:
        return str_rev_recursive(s[1:]) + s[0]

def str_rev_inplace(s, start, end):
    """
    Reversing a string iteratively. This version does not have the stack
    depth limit problem like the recursive version.

    RUNTIME:
    """
    if (end - start) == 0:
        return s

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

def space_delimited_sentence_rev_inplace(st):
    """
    Reversing a the words in a string. This is an inplace implementation.
    The way it works is that, it reverses the entire sentence and then
    reverses the individual words in the sentence. Reversing the words,
    twice in the sentence, gets back the original word.

    RUNTIME:
    """
    l = map(lambda x:x, st)
    lenl, start = len(l), 0
    str_rev_inplace(l, 0, lenl-1)
    for v in range(lenl):
        if l[v] == ' ':
            str_rev_inplace(l, start, v-1)
            start = v + 1
    else:
            str_rev_inplace(l, start, v)

    return ''.join(l)

def char_at_index_encoded_str(s, index):
    """
    Given an encoded string find the character at a certain index
    without decoding it. For example if the string is "a2b1c3d4",
    then the decoded string is "aabcccdddd". If the index is '8',
    then the answer is 'd'. For '6' the answer is 'b'. But the catch,
    is to find the index without decoding the string.

    RUNTIME:
    """

    ti = 0
    for i in filter(lambda x: x%2 != 0, range(len(s))):
        ti += int(s[i])
        if ti >= index:
            return s[i-1]

    return None

def char_at_index_encoded_str_recursive_variation(s, index):
    """
    Given an encoded string find the character at a certain index
    without decoding it. For example if the string is "a2bc3d4",
    then the decoded string is "aabcbcbcdddd". If the index is '8',
    then the answer is 'd'. For '6' the answer is 'b'. But the catch,
    is to find the index without decoding the string.

    RUNTIME:
    """

    def fn(r, prefix, total):

        if not r:
            return None

        if r[0].isdigit():
            total += (int(r[0]) * len(prefix))
            if total > index:
                i = index%(len(prefix))
                return prefix[i]
            prefix = ''
        else:
            prefix += r[0]

        return fn(r[1:], prefix, total)

    return fn(s, '', 0)


def char_at_index_encoded_str_iteration_variation(s, index):
    """
    Given an encoded string find the character at a certain index
    without decoding it. For example if the string is "a2bc3d4",
    then the decoded string is "aabcbcbcdddd". If the index is '8',
    then the answer is 'd'. For '6' the answer is 'b'. But the catch,
    is to find the index without decoding the string.

    RUNTIME:
    """

    n = 0
    pc = 0

    for i in range(len(s)):
        try:
            v = int(s[i])
            pc = pc + (n * v)
            if pc <= index:
                n = 0
        except:
            n += 1

    m = s[(i-n):i]
    return m[index%n]

print char_at_index_encoded_str_iteration_variation("a2bc3d4", 8)

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


