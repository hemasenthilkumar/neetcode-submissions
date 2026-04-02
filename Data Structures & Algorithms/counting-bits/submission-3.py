class Solution:
    def countBits(self, n: int) -> List[int]:

        def count(w):
            c = 0
            while w:
                w = w & w-1
                c+= 1
            return c
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        res = [0,1]
        for i in range(2, n+1):
            res.append(count(i))
        return res