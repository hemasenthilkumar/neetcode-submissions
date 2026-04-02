class TrieNode:

    def __init__(self):
        self.hashmap = {}
        self.flag = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.hashmap:
                curr.hashmap[w] = TrieNode()
            curr = curr.hashmap[w]
        curr.flag = True

    def search(self, word: str) -> bool:

        def dfs(start, root):
            curr = root

            for i in range(start, len(word)):
                if word[i] == '.':
                    # check all children
                    for child in curr.hashmap.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if word[i] not in curr.hashmap:
                        return False
                    curr = curr.hashmap[word[i]]
        
            return curr.flag

        return dfs(0, self.root)
        
