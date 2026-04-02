class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        start = 0
        end = k-1
        freq_map = Counter(s1)
        while end < len(s2):
            window_map = Counter(s2[start:end+1])
            if freq_map == window_map:
                return True
            start += 1
            end += 1
        return False