class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        end = start + 1
        hash_set = set(s[0])
        longest = 1
        while end < len(s):
            if s[end] not in hash_set:
                hash_set.add(s[end])
                longest = max(longest, end-start+1)
                end += 1
            else:
                # we have encountered a duplicate
                start = start + 1
                end = start + 1
                hash_set = set(s[start])
        return longest