class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        freq = {i:False for i in nums}
        res = []
        
        def backtrack(index, freq,comb):
            if index == len(nums):
                res.append(comb[:])
                return 
            
            for num, val in freq.items():
                if not val:
                    freq[num] = True
                    comb.append(num)
                    backtrack(index+1, freq, comb)
                    comb.pop()
                    freq[num] = False
        
        backtrack(0,freq, [])
        return res