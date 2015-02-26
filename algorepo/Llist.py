class Node(object):
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def __unicode__(self):
        l = 'Node' if l.left else 'None'
        r = 'Node' if l.right else 'None'
        return '{0} {1} {2}'.format(l, self.element, r)


class LinkedList(object):
    def __init__(self):
        self.front = None
        self.end = None
        self.nodecount = 0

    def __setFront(self, n):
        self.front = n
        return self

    def __setEnd(self, n):
        self.end = n
        return self

    def __setNodeCount(self, n):
        self.nodecount = n
        return self

    def __incNodeCount(self):
        self.nodecount += 1
        return self

    def __decNodeCount(self):
        self.nodecount -= 1
        return self

    def isEmpty(self):
        return self.nodecount == 0

    def deleteNode(self, element):
        """
        Deletes first occurence of the `element`.
        Search and delete
        O(n)
        """

        t = self.front
        while True:
            if t.element == element:
                break
            if t.right == self.front:
                t = None
                break
            t = t.right

        if t:
            n = t.right
            p = t.left
            if n and p:
                p.right = n
                n.left = p
            elif n:
                self.front = n
                n.left = self.end
            else:
                self.end = p
                p.right = self.front

            self.__decNodeCount()
            del t

        return self

    def insertElement(self, e):
        """
        Insert an element
        O(1)
        """
        nn = Node(e)

        if self.isEmpty():
            nn.left = nn
            nn.right = nn
            self.front = nn
            self.end = nn
        else:
            self.end.right = nn
            nn.left = self.end
            nn.right = self.front
            self.end = nn

        self.__incNodeCount()
        return self

    def toList(self):
        l = list()
        if self.isEmpty():
            return l

        l.append(self.front.element)
        t = self.front.right

        while t != self.front:
            l.append(t.element)
            t = t.right

        return l

    def reverseListInPlace(self):

        def helper(t):
            if t.right == self.front:
                return t

            nxt = helper(t.right)

            nxt.right = t
            t.left = nxt
            return t

        helper(self.front)
        self.front, self.end = self.end, self.front
        self.front.left = self.end
        self.end.right = self.front
        return self

    def reverseList(self):

        def helper(t):
            if t.right == self.front:
                n = Node(t.element)
                return n, n

            front, nxt = helper(t.right)
            nnn = Node(t.element)

            nxt.right = nnn
            nnn.left = nxt

            return front, nnn

        front, end = helper(self.front)
        front.left = end
        end.right = front
        nll = LinkedList()
        nll.__setFront(front)
        nll.__setEnd(end)
        nll.__setNodeCount(self.nodecount)
        return nll

    def commonTailRec(self, ll):

        def helper(a, b, l, an, bn):
            if a == self.front and an == 0:
                a = None

            if b == ll.front and bn == 0:
                return l

            if a:
                l = helper(a.right, b, l, 0, 1)
                l.append(a.element)
                return l

            l = helper(None, b.right, l, 0, 0)
            l.append(b.element)
            return l

        l = helper(self.front, ll.front, list(), 1, 1)
        l1 = l[:ll.nodecount]
        l2 = l[ll.nodecount:]
        l1len = len(l1)
        l2len = len(l2)

        i = 0
        while i < l1len and i < l2len and l1[i] == l2[i]:
            i += 1

        return list(reversed(l1[:i]))

    def customTail(self, n):

        def helper(t, l):
            if t == self.front.right:
                return l

            l = helper(t.right, l)
            l.append(t.element)
            if n == 0:
                return l
            else:
                n -= 1

            return l

        return list(reversed(helper(self.front, list())))

    def commonTail(self, ll):
        l1 = self.reverseList().toList()
        l2 = ll.reverseList().toList()
        l1len = len(l1)
        l2len = len(l2)

        i = 0
        while i < l1len and i < l2len and l1[i] == l2[i]:
            i += 1

        return list(reversed(l1[:i]))

    def extend(self, ll):
        self.end.right = ll.front
        ll.front.left = self.end
        self.end = ll.end
        self.end.right = self.front
        self.nodecount += ll.nodecount
        del ll
        return self

def testing():
    l = LinkedList()
    l.insertElement(1)
    l.insertElement(2)
    l.insertElement(3)
    l.insertElement(4)
    l.insertElement(5)
    l.insertElement(6)
    print l.customTail(3)

    #m = LinkedList()
    #m.insertElement(11)
    #m.insertElement(21)
    #m.insertElement(31)
    #m.insertElement(4)
    #m.insertElement(5)
    #m.insertElement(6)

testing()
