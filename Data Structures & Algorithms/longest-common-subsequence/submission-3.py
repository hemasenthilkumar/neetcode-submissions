class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        rows,cols = len(text1), len(text2)
        dp_array = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
        """
        def backtrack(i,j):
            # base case
            if  i == 0 or j == 0:
                return 0
            if dp_array[i][j] != -1:
                return dp_array[i][j]
            # explore options
            if text1[i-1] == text2[j-1]:
                # matches -> move both pointers
                # add to count
                dp_array[i][j] = 1 + backtrack(i-1,j-1)
            else:
                dp_array[i][j] = max(backtrack(i,j-1), backtrack(i-1,j))
            return dp_array[i][j]
        # text1 index, text2 index
        # we will follow top down approach
        return backtrack(rows,cols)
        """
        for i in range(rows+1):
            dp_array[i][0] = 0
        for j in range(cols+1):
            dp_array[0][j] = 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if text1[i-1] == text2[j-1]:
                    dp_array[i][j] = 1 + dp_array[i-1][j-1]
                else:
                    dp_array[i][j] = max(dp_array[i][j-1], dp_array[i-1][j])
        return dp_array[rows][cols]