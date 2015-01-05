
class TrieNode(object):
    def __init__(self, key, terminalvalue):
        self.trie = dict()
        self.terminalvalue = terminalvalue

class TrieRootNode(object):
    def __init__(self):
        self.rootnode = dict()

    def isEmpty(self):
        pass

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

    def print_trie(self):
        def recprint(temp, word='', words=[]):
            for c in temp.keys():
                word += c
                if temp[c].terminalvalue:
                    words.append(word)
                word = recprint(temp[c].trie, word, words)

            if word:
                return word[:-1]
            else:
                return words

        print recprint(self.rootnode)





t = Trie()
t.insert_key('dom')
t.insert_key('door')
#import pudb; pu.db
t.print_trie()

    #has_key
    #retrieve_key
    #start_with_prefix

