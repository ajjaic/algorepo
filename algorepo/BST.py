
"""
Implementation of the Binary Search Tree
"""
class Node(object):
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

    def __unicode__(self):
        l = 'Node' if l.left else 'None'
        r = 'Node' if l.right else 'None'
        return '{0} {1} {2}'.format(l, self.element, r)

class Bst(object):
    inorder = 'inorder'
    preorder = 'preorder'
    postorder = 'postorder'

    def __init__(self, cmpfn):
        self.root = None
        self.cmpfn = cmpfn #-1 for less, 0 for equal, 1 for greater
        self.nodecount = 0

    def isEmpty(self):
        return (not self.root)

    def __getParent(self, element):

        if self.isEmpty():
            #TODO: better exception required
            raise Exception("Tree without root has no parent")

        def helper(curr_node, parent):
            if curr_node == None:
                return parent

            if self.cmpfn(element, curr_node.element) == 0:
                return parent

            elif self.cmpfn(element, curr_node.element) == -1:
                return helper(curr_node.left, curr_node)

            elif self.cmpfn(element, curr_node.element) == 1:
                return helper(curr_node.right, curr_node)

        return helper(self.root, None)

    def insertElement(self, element):
        newnode = Node(element)

        if self.isEmpty():
            self.root = newnode
        else:
            p = self.__getParent(element)

            if self.cmpfn(element, p.element) <= 0:
                p.left = newnode
            else:
                p.right = newnode

        self.nodecount += 1
        return self

    def isElementExists(self, element):

        p = self.__getParent(element)

        if p.left and (p.left.element, element) == 0:
            return True

        if p.right and (p.right.element, element) == 0:
            return True

        return False


    def isFullBinaryTree(self):

        if self.isEmpty():
            #TODO: better exception required
            raise Exception("Tree is empty")

        def helper(t):
            if t.left and t.right:
                return helper(t.left) and helper(t.right)
            elif not t.left and (not t.right):
                return True
            else:
                return False


        return helper(self.root)


    def getTreeHeight(self):

        def helper(t):
            if t == None:
                return 0

            llen = 1+helper(t.left)
            rlen = 1+helper(t.right)
            return max(llen, rlen)

        return helper(self.root)


    def isPerfectBinaryTree(self):
        if self.isEmpty():
            #TODO: better exception required
            raise Exception("Tree is empty")

        h = self.getTreeHeight()
        if (2**h)-1 == self.nodecount:
            return True
        return False

    def isCompleteBinaryTree(self):
        if self.isEmpty():
            #TODO: better exception required
            raise Exception("Tree is empty")

        def helper(t, index):
            if t == None:
                return True

            if index >= self.nodecount:
                return False

            l = helper(t.left, (2*index)+1)
            r = helper(t.right, (2*index)+2)

            return l and r

        return helper(self.root, 0)

    def getCounterClockwiseOrder(self):
        def leftside(t, l):
            if t == None:
                return l

            l.append(t.element)
            return leftside(t.left, l)

        def leaves(t, l):
            if t == None:
                return l

            l = leaves(t.left, l)
            if not t.left and (not t.right):
                l.append(t.element)

            return leaves(t.right, l)

        def rightside(t, l):
            if t == None:
                return l

            l = rightside(t.right, l)
            l.append(t.element)
            return l


        return leftside(self.root, list()) + \
                leaves(self.root, list())[1:] + \
                rightside(self.root, list())[1:-1]

    def getCircularLinkedList(self):
        def helper(t, (s, e)):
            if t == None:
                return (s, e)

            (s, e) = helper(t.left, (s,e))
            r = t.right
            if not s and (not e):
                t.left = t
                t.right = t
                s = t
                e = t
            else:
                e.right = t
                t.left = e
                e = t
            (s, e) = helper(r, (s, e))

            return (s, e)

        (s, e) = helper(self.root, (None, None))
        e.right = s
        s.left = e
        return (s, e)

    def getListAtEveryLevel(self):

        def helper(t, ldict, d):
            if t == None:
                return ldict

            l = ldict.get(d, list())
            l.append(t.element)
            ldict[d] = l

            ldict = helper(t.left, ldict, d+1)
            ldict = helper(t.right, ldict, d+1)

            return ldict

        return helper(self.root, dict(), 0)

    def getLevelOrder(self):
        l = list()
        m = [self.root]
        while m:
            n = m[0]
            l.append(n.element)
            if n.left:
                m.append(n.left)
            if n.right:
                m.append(n.right)
            m = m[1:]
        return l

    def __getTraverseOrder(self, traverse_type):

        def helper(curr_node, l):
            if curr_node == None:
                return l

            if traverse_type == Bst.inorder:
                l = helper(curr_node.left, l)
                l.append(curr_node.element)
                l = helper(curr_node.right, l)
            elif traverse_type == Bst.preorder:
                l.append(curr_node.element)
                l = helper(curr_node.left, l)
                l = helper(curr_node.right, l)
            elif traverse_type == Bst.postorder:
                l = helper(curr_node.left, l)
                l = helper(curr_node.right, l)
                l.append(curr_node.element)
            return l

        return helper(self.root, list())

    def printTree(self, t):
        print self.__getTraverseOrder(t)

def testing():
    s = Bst(cmp)
    s.insertElement(10)
    s.insertElement(5)
    s.insertElement(2)
    s.insertElement(7)
    s.insertElement(15)
    s.insertElement(12)
    s.insertElement(17)
    print s.getListAtEveryLevel()

testing()
