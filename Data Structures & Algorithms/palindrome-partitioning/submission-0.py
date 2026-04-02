class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def check_palindrome(string):
            if string == string[::-1]:
                return True
            return False

        def backtrack(s, index, sub):
            if index == len(s):
                if sub:
                    res.append(sub[:])
                return
            for i in range(index, len(s)):
                if check_palindrome(s[index:i+1]):
                    sub.append(s[index:i+1])
                    backtrack(s,i+1 , sub)
                    sub.pop()
        
        backtrack(s,0, [])
        return res
            
            