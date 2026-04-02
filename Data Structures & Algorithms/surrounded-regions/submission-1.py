class Solution:
    def solve(self, board: List[List[str]]) -> None:   
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        # go through the board and mark the non-working Os
        # row 0, all cols
        # all rows , 0 col
        # last row, all cols
        # all rows, last col
        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or board[r][c] == 'X':
                return 
            # then its a valid 0 on the/connected to the boundary
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for c in range(COLS):
            dfs(0,c)
        for r in range(ROWS):
            dfs(r,0)
        for c in range(COLS):
            dfs(ROWS-1, c)
        for r in range(ROWS):
            dfs(r, COLS-1)

        # now change all remaining O's to X's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visit:
                    board[r][c] = 'X'
