class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def bfs(r,c):
            queue = collections.deque()
            visit.add((r,c))
            queue.append((r,c))
            while queue:
                ro,co = queue.popleft()
                for dr,dc in directions:
                    r,c = ro+dr,co+dc
                    if (r in range(rows)) and (c in range(cols)) and (r,c) not in visit and grid[r][c]=='1':
                        queue.append((r,c))
                        visit.add((r,c))
        

        for r in range(rows):
            for c in range(cols):
                print(visit, (r,c))
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands