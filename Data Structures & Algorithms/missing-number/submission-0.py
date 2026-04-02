class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        actual_diff = 0
        original_diff = 0

        for i in range(len(nums)+1):
            actual_diff ^= i
        
        for j in nums:
            original_diff ^= j

        return original_diff ^ actual_diff