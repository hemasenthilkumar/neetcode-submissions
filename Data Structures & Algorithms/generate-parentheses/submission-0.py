class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # basecase: if open==closed==n
        # add open only if open < n
        # add closed only if closed < open

        stack = []
        result = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                result.append("".join(stack))
                return 
            if open_count < n:
                stack.append('(')
                backtrack(open_count+1, closed_count)
                stack.pop()
            if closed_count < open_count:
                stack.append(')')
                backtrack(open_count, closed_count+1)
                stack.pop()

        backtrack(0,0)
        return result            