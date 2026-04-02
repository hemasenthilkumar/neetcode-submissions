class Solution:
    def longestPalindrome(self, s: str) -> str:
        # center expansion algorithm
        # we have to add for odd, even length strings
        # and we need to check from each char
        resultStr, resultLen = "",0
        for char in range(len(s)):
            # for each char
            # odd length
            # pointing to same index
            l,r = char,char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # its valid palindromic char
                currLen = r-l+1
                if currLen > resultLen:
                    resultStr = s[l:r+1]
                    resultLen = currLen
                l -= 1
                r += 1

            l,r = char,char+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # its valid palindromic char
                currLen = r-l+1
                if currLen > resultLen:
                    resultStr = s[l:r+1]
                    resultLen = currLen
                l -= 1
                r += 1
        
        return resultStr
            

