class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        start = 0
        result = []

        for end in range(len(nums)):
            while q and nums[q[-1]] < nums[end]:
                q.pop()
            q.append(end)
            if q[0] < start:
                q.popleft()

            if (end+1) >=k:
                result.append(nums[q[0]])
                start += 1
        return result
            