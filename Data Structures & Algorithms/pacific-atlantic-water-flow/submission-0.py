class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        # check from top row, first col for pacific
        # check from last row, last col for atlantic

        def dfs(r,c, visit, prev):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or heights[r][c] < prev:
                return
            visit.add((r,c))
            prev = heights[r][c]
            dfs(r+1,c,visit, prev)
            dfs(r-1,c,visit, prev)
            dfs(r,c+1,visit, prev)
            dfs(r,c-1,visit, prev)

        # for pacific flow
        # first row
        for c in range(COLS):
            dfs(0,c,pacific_reachable,-1)
        # first col
        for r in range(ROWS):
            dfs(r,0,pacific_reachable,-1)

        # for atlantic flow
        # last row
        for c in range(COLS):
            dfs(ROWS-1,c,atlantic_reachable,-1)
        # last col
        for r in range(ROWS):
            dfs(r,COLS-1,atlantic_reachable,-1)
        
        return list(pacific_reachable & atlantic_reachable)
