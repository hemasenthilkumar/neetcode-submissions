class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(index, arr, res):
            if index == len(nums):
                res.append(arr[:])
                return
            arr.append(nums[index])
            backtrack(index+1, arr, res)
            arr.pop()
            backtrack(index+1, arr, res)
        
        res = []
        backtrack(0, [], res)
        return res