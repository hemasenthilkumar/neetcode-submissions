class Solution:
    def rob(self, nums: List[int]) -> int:

        dp_array = [-1] * len(nums)
        def backtrack(i):
            if i >= len(nums):
                return 0
            if dp_array[i] != -1:
                return dp_array[i]
            left = nums[i] + backtrack(i+2)
            right = backtrack(i+1)
            dp_array[i] = max(left, right)
            return dp_array[i]
        
        data = backtrack(0)
        print(dp_array)
        return data
            