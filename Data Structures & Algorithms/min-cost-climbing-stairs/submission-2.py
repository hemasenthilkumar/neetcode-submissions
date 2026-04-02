class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        dp_array = [-1] * (len(cost))
        def backtrack(i):
            if i >= len(cost):
                return 0
            if dp_array[i] != -1:
                return dp_array[i]
            dp_array[i] = cost[i] + min(backtrack(i+1),backtrack(i+2))
            return dp_array[i]
        
        return (min(backtrack(0), backtrack(1)))
        """

        prev2, prev = 0, 0
        for i in range(2,len(cost)+1):
            left = cost[i-1] + prev
            right =  float('inf')
            if i > 1:
                right = cost[i-2] + prev2
            prev2 = prev
            prev = min(left, right)
        return prev