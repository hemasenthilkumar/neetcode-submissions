class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        max_area = 0

        def bfs(r,c):
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))
            area = 1
            while queue:
                ro,co = queue.popleft()
                for dr,dc in directions:
                    r,c = ro+dr,co+dc
                    if (r in range(rows)) and (c in range(cols)) and (r,c) not in visit and grid[r][c]==1:
                        queue.append((r,c))
                        visit.add((r,c))
                        area += 1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r,c)
                    max_area = max(max_area,area)

        return max_area