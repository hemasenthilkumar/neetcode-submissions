class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i in range(k):
            minHeap.append(nums[i])
        heapq.heapify(minHeap)
        for i in range(k, len(nums)):
            if minHeap:
                if nums[i] > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappush(minHeap, nums[i])

        return minHeap[0]