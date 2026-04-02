class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def backtrack(index, prev):
            # base case
            if index == len(nums):
                return 0
            # not take
            lent = 0 + backtrack(index+1, prev)
            # take
            if prev == -1 or nums[index] > nums[prev]:
                lent = max(lent, 1 + backtrack(index+1, index))
            # return
            return lent
        
        return backtrack(0, -1)

        
