class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def backtrack(i, total):
            if i >= len(cost):
                return total
            total += cost[i]
            return min(backtrack(i+1, total),backtrack(i+2, total))
        
        return min(backtrack(0,0), backtrack(1,0))
