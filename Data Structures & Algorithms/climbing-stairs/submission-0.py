class Solution:
    def climbStairs(self, n: int) -> int:
        
        total = 0
        def backtrack(n):
            nonlocal total
            if n == 0:
                total += 1
                return
            if n < 0:
                return 
            backtrack(n-1) 
            backtrack(n-2)
        
        backtrack(n)
        return total