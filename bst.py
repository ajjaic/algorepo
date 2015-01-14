#TODO: Refactor
class Node(object):
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

class Bst(object):
    def __init__(self, cmpfn):
        self.cmpfn = cmpfn #-1 for less, 0 for equal, 1 for greater
        self.root = None

    def isEmpty(self):
        return (not self.root)

    def insert_element(self, element):
        if self.isEmpty():
            self.root = Node(element)
        else:
            temp = self.root
            #prev = None
            while temp:
                if self.cmpfn(element, temp.element) == -1:
                    #prev = temp
                    temp = temp.left
                else:
                    #prev = temp
                    temp = temp.right
            temp = Node(element)




def testing():
    s = Bst(cmp)
    import pudb; pu.db
    s.insert_element(20)
    s.insert_element(19)
    pass

testing()

