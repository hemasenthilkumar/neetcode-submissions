class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp_array = [-1] * n
        def backtrack(n):
            if n == 0 or n == 1:
                return cost[n]
            if dp_array[n] != -1:
                return dp_array[n]
            right = float('inf')
            left = cost[n] + backtrack(n-1)
            if n > 1:
                right = cost[n] + backtrack(n-2)
            dp_array[n] = min(left, right)
            return dp_array[n]

        return (min(backtrack(n-1), backtrack(n-2)))
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
        """