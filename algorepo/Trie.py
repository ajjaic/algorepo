"""
Implementation of the Trie datastructure
"""
class TrieNode(object):
    def __init__(self, key, terminalvalue):
        self.trie = dict()
        self.terminalvalue = terminalvalue

class Trie(object):
    def __init__(self):
        self.rootnode = dict()

    def insert_key(self, key):
        temp = self.rootnode
        for c in key[:-1]:
            if not temp.has_key(c):
                temp[c] = TrieNode(c, None)

            temp = temp[c].trie

        lk = key[-1]
        temp[lk] = TrieNode(lk, None)
        temp[lk].terminalvalue = True

    def has_word(self, key):
        temp = self.rootnode
        tempNode = None

        for c in key:
            if not temp.has_key(c):
                return None

            tempNode = temp[c]
            temp = tempNode.trie

        return tempNode.terminalvalue

    def starts_with(self, partialkey):
        words = list()
        temp = self.rootnode
        tempNode = None

        for c in partialkey:
            if not temp.has_key(c):
                return None
            tempNode = temp[c]
            temp = tempNode.trie

        return self.retrieve_words(tempNode)


    def retrieve_words(self, root=None):
        temp = self.rootnode if not root else root.trie

        def recurse_trie(t, word=''):
            temp = None
            words = list()

            for c in t.keys():
                word += c
                temp = t[c]
                if temp.terminalvalue:
                    words.append(word)

                word, wordsr = recurse_trie(temp.trie, word)
                words = words + wordsr
                word = word[:-1]

            return word, words

        _, words = recurse_trie(temp)

        return words

    def print_trie(self):
        print self.retrieve_words()

def test():
    t = Trie()
    t.insert_key('dom')
    t.insert_key('door')
    t.has_word("door")
    import pudb; pu.db
    t.starts_with("do")
    t.print_trie()
