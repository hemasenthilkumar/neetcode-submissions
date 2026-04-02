class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        n= len(nums)
        prev2, prev = 0, nums[0]
        for i in range(1, len(nums)):
            left = nums[i]
            if i > 1:
                left = nums[i] + prev2
            curr = max(left, prev)
            prev2 = prev
            prev = curr
        return prev