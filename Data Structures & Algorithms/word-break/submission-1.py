class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i):
            if i == len(s):
                return True
            
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        return True
            return False
        
        return dfs(0)