class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        i = 0
        while i < k and i < len(nums):
            self.minheap.append(nums[i])
            i += 1
        heapq.heapify(self.minheap)

        for i in range(k, len(nums)):
            top  = self.minheap[0]
            if nums[i] > top:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, nums[i])
        print(self.minheap)
    def add(self, val: int) -> int:
        if not self.minheap or len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        else:
            top  = self.minheap[0]
            if val > top:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, val)
        
        return self.minheap[0]
        
