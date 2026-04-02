class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        import heapq
        maxheap = []
        for stone in stones:
            maxheap.append(-stone)
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            x = heapq.heappop(maxheap)
            y = heapq.heappop(maxheap)
            x = -x
            y = -y
            if x > y:
                heapq.heappush(maxheap, -(x-y))
            
        if maxheap:
            return -maxheap[0]
        return 0