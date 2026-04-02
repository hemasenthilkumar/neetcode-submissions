class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        def backtrack(index, target, comb):
            if target < 0 or index>=len(nums):
                return 
            if target == 0:
                print(comb)
                res.append(comb[:])
                return
            # pick
            comb.append(nums[index])
            backtrack(index, target - nums[index], comb)
            # undo
            comb.pop()
            # not pick
            backtrack(index +1, target, comb)
        
        backtrack(0,target, [])
        return res
