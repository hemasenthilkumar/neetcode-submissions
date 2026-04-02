class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        def backtrack(index, sets):
            if index == len(nums):
                res.append(sets[:])
                return

            sets.append(nums[index])
            backtrack(index+1, sets)
            sets.pop()
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1, sets)
        
        backtrack(0, [])
        return res