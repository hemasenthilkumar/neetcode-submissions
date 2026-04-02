class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        min_value = nums[0]
        while low<= high:
            if nums[low] < nums[high]:
                min_value = min(min_value,nums[low])
                break
            mid = low + ((high-low)//2)
            min_value = min(min_value, nums[mid])
            if nums[mid] >= nums[low]:
                #pivot could be in left side
                low = mid + 1
            else:
                #pivot could be on the right side
                high = mid -1
        return min_value