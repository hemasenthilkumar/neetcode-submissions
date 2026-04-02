class Solution:
    import math, heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for point in points:
            val = abs(0-point[0])**2 + abs(0-point[1])**2
            val = math.sqrt(val)
            minHeap.append([val, point])
        heapq.heapify(minHeap)
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res