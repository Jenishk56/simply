class trieNode:
    def __init__(self):
        self.next = {}
        self.leaf = False

    def add_word(self, word):
        i = 0
        while i < len(word):
            k = word[i]
            if not k in self.next:
                node = trieNode()
                self.next[k] = node
            self = self.next[k]
            if i == len(word) - 1: 
                self.leaf = True
            else:
                self.leaf = False
            i += 1

    def traverse(self, word):
        if self.leaf:
            print (word)
        for i in self.next:
            s = word + i
            self.next[i].traversal(s)

    def autocomplete(self, word):
        i = 0
        s = ''
        while i < len(word):
            k = word[i]
            s += k
            if k in self.next:
                self = self.next[k]
            else:
                return 'NOT FOUND'
            i += 1
        self.traverse(s)
        return 'END'

search1 = trieNode()
search1.add_word("adasdsad")
search1.add_word("12121")
search1.add_word("hi")
search1.add_word("hello")
search1.add_word("how are you")

search1.autocomplete("h")