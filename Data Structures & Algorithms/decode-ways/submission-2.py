class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp_array = [-1] * (len(s)+1)
        """
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
        """
        next1,next2, curr = 1,0,0
        res = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = next1
                if  i+1 < len(s) and int(s[i:i+2]) < 27:
                    curr += next2
            next2 = next1
            next1 = curr
            curr = 0
        return next1
        
