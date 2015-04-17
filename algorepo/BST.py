
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
        return newnode

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


    #TODO: This implemenation is totally wrong
    def isPerfectBinaryTree(self):
        if self.isEmpty():
            #TODO: better exception required
            raise Exception("Tree is empty")

        h = self.getTreeHeight()
        if (2**h)-1 == self.nodecount:
            return True
        return False

    #def isPerfectBinaryTree(self):

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

    def getListAtEveryLevelGlobalDict(self):

        def helper(t, l_dict, d):
            if t == None:
                return

            helper(t.left, l_dict, d+1)
            helper(t.right, l_dict, d+1)

            temp = l_dict.get(d, list())
            temp.append(t.element)
            l_dict[d] = temp

            return

        k = dict()
        helper(self.root, k, 0)
        return k

    def getListEveryLevelBFS(self):

        l = [[self.root]]
        i = 0

        while True:
            tmp = list()

            for n in l[i]:
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)

            i += 1
            if not tmp:
                break
            l.append(tmp)

        m = list()
        for i in l:
            tmp = list()
            for j in i:
                tmp.append(j.element)
            m.append(tmp)

        return m

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

    def getRandomNode(self):
        from random import random

        def helper(t):
            if not t:
                return 0, None

            lp = helper(t.left)
            rp = helper(t.right)
            tp = random(), t

            return max(tp, lp, rp)

        return helper(self.root)[1].element

    def nodeAncestors(self, n):

        if self.isEmpty() or n is None:
            return []

        def helper(t, ancestors):
            if t is None:
                return False, ancestors

            if t is n:
                return True, ancestors

            ancestors.append(t)
            nodefound, ancestors = helper(t.left, ancestors)
            if nodefound:
                return True, ancestors
            nodefound, ancestors = helper(t.right, ancestors)
            if nodefound:
                return True, ancestors
            ancestors = ancestors[:-1]
            return False, ancestors

        _, ancestors = helper(self.root, list())
        return ancestors


    def printTree(self, traverse_order):
        print self.__getTraverseOrder(traverse_order)


    def isBinarySearchTree(self):

        import sys
        mx = sys.maxint
        mn = -sys.maxint-1

        def helper(t, mn, mx):

            if t == None:
                return True

            if mn <= t.element and t.element < mx:
                lt = helper(t.left, mn, t.element)
                rt = helper(t.right, t.element, mx)
            else:
                return False

            return lt and rt

            #lt = True
            #if mn <= t.element:
                #lt = helper(t.left, mn, t.element)
            #else:
                #return False

            #rt = True
            #if t.element < mx:
                #rt = helper(t.right, t.element, mx)
            #else:
                #return False

            #return lt and rt

        return helper(self.root, mn, mx)
    #def isBinarySearchTree(self):
        #def helper(t):
            #lt = True
            #if t.left:
                #if t.element > t.left.element:
                    #lt = helper(t.left)
                #else:
                    #lt = False

            #rt = True
            #if t.right:
                #if t.element < t.right.element:
                    #rt = helper(t.right)
                #else:
                    #rt = False

            #return lt and rt

        #return helper(self.root)

    def isBalanced(self):

        def helper(t):
            if t is None:
                return 0, True

            left_height, left_isbalanced = helper(t.left)
            if not left_isbalanced:
                return None, False
            right_height, right_isbalanced = helper(t.right)
            if not right_isbalanced:
                return None, False

            return max(1+left_height, 1+right_height), abs(left_height-right_height) <= 1

        _, b = helper(self.root)

        return b

def testing():
    s = Bst(cmp)
    s.insertElement(10)
    s.insertElement(5)
    s.insertElement(2)
    s.insertElement(7)
    s.insertElement(15)
    s.insertElement(12)
    s.insertElement(17)
    s.insertElement(14)
    s.insertElement(14.5)
    import pudb; pu.db
    print s.isBinarySearchTree()

testing()

#def binTreeMinHt(sl):
    #def helper(s, e):
        #t = (e-s)+1
        #if t == 1:
            #return Node(sl[s])
        #if t == 2:
            #pn = Node(sl[s])
            #pn.right = Node(sl[e])
            #return pn
        #if t == 3:
            #pn = Node(sl[s+1])
            #pn.left = Node(sl[s])
            #pn.right = Node(sl[e])
            #return pn

        #mid = s+(t/2)
        #pn = Node(sl[mid])

        #ls = s
        #le = mid-1
        #ln = helper(ls, le)
        #pn.left = ln

        #rs = mid+1
        #re = e
        #rn = helper(rs, re)
        #pn.right = rn

        #return pn

    #return helper(0, len(sl)-1)


#sl = list(range(1,65))
#p = binTreeMinHt(sl)

#def printT(p):
    #if p == None:
        #return

    #printT(p.left)
    #print p.element
    #printT(p.right)

#def height(p):
    #if p == None:
        #return 0

    #l = 1 + height(p.left)
    #r = 1 + height(p.right)
    #return max(l, r)

#print printT(p)
#print height(p)
