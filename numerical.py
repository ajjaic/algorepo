def fib(n):
    #memoized with a list
    def fib_d(n, l=[0, 1,1]):
        if n < len(l):
            return l, l[n]
        l, s1 = fib_d(n-1, l)
        l, s2 = fib_d(n-2, l)
        l.append(s1+s2)
        return l, s1+s2

    _, v = fib_d(n)
    return v

def anfib(n):
    #memoized with a list
    def fib_d(n, l=[0, 1,1]):
        if n < len(l):
            return l
        l.append(fib_d(n-1, l)[-1] + fib_d(n-2, l)[-2])
        return l

    return fib_d(n)[-1]

def anofib(n):
    #unmemoized
    if n == 1 or n == 2:
        return 1
    else:
        return anofib(n-1) + anofib(n-2)

def main():
    import sys
    opt, n = sys.argv[1], sys.argv[2]
    n = int(n)
    if opt == '1':
        print "fib"
        return fib(n)
    elif opt == '2':
        print "anfib"
        return anfib(n)
    else:
        print "anofib"
        return anofib(n)

main()
