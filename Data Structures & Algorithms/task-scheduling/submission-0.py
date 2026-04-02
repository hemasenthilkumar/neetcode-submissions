class Solution:
    from collections import Counter, deque
    import heapq

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-val for val in freq.values()]
        heapq.heapify(maxHeap)
        time = 0

        q = deque()

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time+n])

            if q and q[0][1] == time:
                # if top is ready
                count,_= q.popleft()
                heapq.heappush(maxHeap, count)

        return time


                




