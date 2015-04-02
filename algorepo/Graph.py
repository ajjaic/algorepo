
samplegraph = dict(
        a = 'f',
        b = 'ec',
        c = 'f',
        d = '',
        e = 'fa',
        f = 'd')

def isRouteExistsBFS(n1, n2, graph):

    l = n1
    v = dict()
    i = 0

    while i < len(l):
        if not v.has_key(l[i]):
            if l[i] == n2:
                return True
            else:
                v[l[i]] = 1
                l += graph[l[i]]

        i += 1

    return False

def isRouteExistsDFS(n1, n2, graph):

    def helper(a, b, visited):
        if a == b:
            return True

        found = False
        visited[a] = 1
        for n in graph[a]:
            if visited.has_key(n):
                continue
            found = helper(n, b, visited)
            if found:
                break

        return found


    return helper(n1, n2, dict())

print isRouteExistsDFS('a', 'n', samplegraph)






