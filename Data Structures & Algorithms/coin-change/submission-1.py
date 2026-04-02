class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        INT_MAX = 10**9 - 7
        dp_array = {}
        def backtrack(i,target):
            if i == 0:
                if target % coins[i] == 0:
                    return target//coins[i]
                return INT_MAX
            if (i,target) in dp_array:
                return dp_array[(i, target)]
            nottake =  0 + backtrack(i-1, target)
            take = float('inf')
            if coins[i] <= target:
                take = 1 + backtrack(i, target-coins[i])
            dp_array[(i,target)] = min(nottake, take)
            return dp_array[(i,target)]

        ans = backtrack(len(coins)-1,amount) 
        if ans >= INT_MAX:
            return -1
        return ans