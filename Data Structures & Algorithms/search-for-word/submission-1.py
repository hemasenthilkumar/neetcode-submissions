class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def backtrack(r,c,string):

            if string == word:
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit:
                return False
            string += board[r][c]
            visit.add((r,c))
            res = backtrack(r+1,c,string) or \
            backtrack(r,c+1,string) or \
            backtrack(r-1,c,string) or \
            backtrack(r,c-1,string) 
            string=string[:-1]
            visit.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,""):
                    return True
        return False
