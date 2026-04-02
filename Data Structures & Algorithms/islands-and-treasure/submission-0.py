class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        visit = set()
        INF = 2147483647
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        counter = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = counter
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] != -1 and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))
            counter += 1
    
