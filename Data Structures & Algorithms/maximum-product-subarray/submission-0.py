class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_result = max(nums)
        currMin, currMax = 1,1

        for n in nums:
            if n == 0:
                currMin, currMax = 1,1
                continue
            old = n*currMax
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(old, n*currMin, n)
            max_result = max(currMax, currMin, max_result)
        
        return max_result
