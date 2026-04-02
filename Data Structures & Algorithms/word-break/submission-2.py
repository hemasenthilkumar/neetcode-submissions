class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={}
        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dfs(i+len(w))
                    if dp[i]:
                        return dp[i]
            return False
        
        return dfs(0)