class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def difference_count(s1, s2):
            total = sum(c1 != c2 for c1, c2 in zip(s1, s2))
            return total == 1

        if endWord not in wordList:
            return 0
        
        adj = defaultdict(set)
        wordList.append(beginWord)
        visit = set()
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if i == j:
                    continue
                if difference_count(wordList[i],wordList[j]):
                    adj[wordList[i]].add(wordList[j])
        q = deque()
        q.append([beginWord])
        visit.add(beginWord)
        while q:
            path = q.popleft()
            node = path[-1]
            if node == endWord:
                return len(path)
            
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(node)
                    q.append(path+[nei])
        return 0
        
