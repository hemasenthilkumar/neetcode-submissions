class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_value = max(piles)
        start, end = 1, max_value
        min_k = float('inf')
        while start <= end:
            mid = start + ((end-start)//2)
            hours = 0
            for banana in piles:
                hours += math.ceil(banana/mid)
            if hours <= h:
                min_k = min(min_k, mid)
                end = mid - 1
            else:
                start = mid + 1
        return min_k