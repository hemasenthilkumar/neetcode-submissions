class TrieNode:

    def __init__(self):
        self.hashmap = {}
        self.flag = False
    
    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.hashmap:
                curr.hashmap[w] = TrieNode()
            curr = curr.hashmap[w]
        curr.flag = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        result, visit = set(), set()
    
        def dfs(r,c, node, word):
            # constraints
            if (r < 0 or c <0 ) or (r==ROWS or c==COLS) or ((r,c) in visit) or (board[r][c] not in node.hashmap):
                return
            # do something
            visit.add((r,c))
            node = node.hashmap[board[r][c]]
            word += board[r][c]
            if node.flag:
                result.add(word)
            # backtrack
            dfs(r-1,c, node, word)
            dfs(r+1,c, node, word)
            dfs(r,c-1, node, word)
            dfs(r,c+1, node, word)
            # undo something
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        
        return list(result)

