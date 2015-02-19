
"""
Implementation of the Binary Search Tree
"""
class Node(object):
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

class Bst(object):
    inorder = 'inorder'
    preorder = 'preorder'
    postorder = 'postorder'

    def __init__(self, cmpfn):
        self.root = None
        self.cmpfn = cmpfn #-1 for less, 0 for equal, 1 for greater

    def isEmpty(self):
        return (not self.root)

    def __parent(self, element):

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
            return self

        p = self.__parent(element)

        if self.cmpfn(element, p.element) <= 0:
            p.left = newnode
        else:
            p.right = newnode

        return self

    def elementExists(self, element):

        p = self.__parent(element)

        if p.left and (p.left.element, element) == 0:
            return True

        if p.right and (p.right.element, element) == 0:
            return True

        return False


    def __traversal(self, traverse_type):

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
        print self.__traversal(t)

def testing():
    s = Bst(cmp)
    s.insertElement(10)
    s.insertElement(5)
    s.insertElement(2)
    s.insertElement(7)
    s.insertElement(15)
    s.insertElement(12)
    s.insertElement(17)
    print s.elementExists(11)
    s.printTree(Bst.inorder)

testing()
