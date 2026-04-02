class Trie:
    def __init__(self):
        self.hashmap = {}  
        self.flag = False  

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.hashmap:
                curr.hashmap[w] = Trie()
            curr = curr.hashmap[w]
        curr.flag = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            if w not in curr.hashmap:
                return False
            curr = curr.hashmap[w]
        return curr.flag


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for p in prefix:
            if p not in curr.hashmap:
                return False
            curr = curr.hashmap[p]
        return True