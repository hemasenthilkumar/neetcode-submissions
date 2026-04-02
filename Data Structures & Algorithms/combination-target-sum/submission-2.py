class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()
        def backtrack(index, target, comb):
            if target == 0:
                res.append(comb[:])
                return
            if target < 0:
                return
            for i in range(index, len(nums)):
                if nums[i] > target:
                    break
                comb.append(nums[i])
                backtrack(i, target - nums[i], comb)
                # undo
                comb.pop()
        
        backtrack(0,target, [])
        return res
