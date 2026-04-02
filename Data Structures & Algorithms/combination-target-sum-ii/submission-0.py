class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()
        def backtrack(index, target, comb):
            if target == 0:
                res.append(comb[:])
                return
            if target < 0:
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    break
                comb.append(nums[i])
                backtrack(i+1, target - nums[i], comb)
                # undo
                comb.pop()
        
        backtrack(0,target, [])
        return res