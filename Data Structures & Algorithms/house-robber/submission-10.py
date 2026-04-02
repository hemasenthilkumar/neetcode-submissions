class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp_array = [-1] * (len(nums))
        def backtrack(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[i]
            if dp_array[i] != -1:
                return dp_array[i]
            left = nums[i] + backtrack(i-2)
            right = backtrack(i-1)
            dp_array[i] = max(left, right)
            return dp_array[i]
        
        data = backtrack(len(nums)-1)
        return data
        """
        n= len(nums)
        prev2, prev = -1, nums[0]

        for i in range(1, len(nums)):
            left = nums[i]
            if i > 1:
                left = nums[i] + prev2
            curr = max(left, prev)
            prev2 = prev
            prev = curr
        
        return prev

        
            