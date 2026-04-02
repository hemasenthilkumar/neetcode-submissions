class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions =[[-1,0],[1,0],[0,1],[0,-1]]
        q = collections.deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        dist = 0
        while q and fresh > 0:
            for i in range(len(q)):
                row,col = q.popleft()
                for dr, dc in directions:
                    r,c=row+dr, col+dc
                    if r in range(rows) and \
                    c in range(cols) and \
                    grid[r][c] == 1 :
                        q.append((r,c))
                        grid[r][c] = 2
                        fresh -= 1
            dist += 1
        
        return dist if fresh==0 else -1


