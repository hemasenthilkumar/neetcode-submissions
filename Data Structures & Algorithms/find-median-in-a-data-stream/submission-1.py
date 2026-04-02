class MedianFinder:

    def __init__(self):
        self.maxHeap = []     
        self.minHeap = []
           
    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        # rebalancing
        if len(self.maxHeap) > len(self.minHeap) +1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > len(self.maxHeap) +1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)


    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0])/2
        