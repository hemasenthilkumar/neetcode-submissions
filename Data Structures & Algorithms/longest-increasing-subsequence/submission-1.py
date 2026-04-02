class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = defaultdict(dict)
        def backtrack(index, prev):
            # base case
            if index == len(nums):
                return 0
            # not take
            if index in dp and prev in dp[index]:
                return dp[index][prev]
            lent = 0 + backtrack(index+1, prev)
            # take
            if prev == -1 or nums[index] > nums[prev]:
                lent = max(lent, 1 + backtrack(index+1, index))
                dp[index][prev] = lent
            # return
            return lent
        
        return backtrack(0, -1)

        
