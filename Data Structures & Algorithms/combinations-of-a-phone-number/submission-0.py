class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, string):
            if len(string) == len(digits):
                res.append(string)
                return
            for c in digitToChar[digits[index]]:
                backtrack(index+1, string+c)

        if not digits:
            return []
        backtrack(0,"")
        return res
            