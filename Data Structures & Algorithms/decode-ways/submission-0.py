class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp_array = [-1] * len(s)
        def backtrack(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if dp_array[i] != -1:
                return dp_array[i]
            res = backtrack(i+1) 
            if i + 1 < len(s) and int(s[i:i+2]) < 27:
                res  += backtrack(i+2)  
            dp_array[i] = res
            return res
        
        count = backtrack(0)
        return count
