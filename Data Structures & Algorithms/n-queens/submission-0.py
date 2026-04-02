class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n  for _ in range(n)]
        cols = set()
        negative_diag = set()
        positive_diag = set()
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r+c) in positive_diag or (r-c) in negative_diag:
                    # skip it
                    continue
                cols.add(c)
                positive_diag.add(r+c)
                negative_diag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                positive_diag.remove(r+c)
                negative_diag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res