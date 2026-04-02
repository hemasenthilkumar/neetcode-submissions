class Solution:
    def countSubstrings(self, s: str) -> int:
       # center expansion algorithm
        # we have to add for odd, even length strings
        # and we need to check from each char
        count = 0
        for char in range(len(s)):
            # for each char
            # odd length
            # pointing to same index
            l,r = char,char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            l,r = char,char+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # its valid palindromic char
                count += 1
                l -= 1
                r += 1
        
        return count
            
