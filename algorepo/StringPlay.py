
def palindrome(p):

    b, e = 0, len(p)-1

    while b <= e:
        if p[b] != p[e]:
            return False
        b += 1
        e -= 1

    return True

def palin_rec(p):
    def help(p):
        return '' if not p else (help(p[1:]) + p[0])
    return p == help(p)

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

def str_rev_recursive(s):
    """
    Reversing a string recursively. As long as 's' is not too long,
    this function will reverse a given string. If 's' is too long,
    then this function could reach the maximum stack depth and crash.

    RUNTIME:
    """
    return '' if not s else (str_rev_recursive(s[1:]) + s[0])

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
