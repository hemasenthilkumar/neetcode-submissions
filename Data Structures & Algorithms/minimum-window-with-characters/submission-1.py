class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq_map = Counter(t)
        start = 0
        end = 0
        min_window = float('inf')
        res = ""
        window_map = {}
        def check_validity():
            isvalid=True
            for k,v in freq_map.items():
                if window_map.get(k, 0) < v:
                    isvalid=False
                    break
            return isvalid

        while end <= len(s):
            # find untill all chars are in the window
            # then shrink it untill invalid
            # then start = start + 1
            if check_validity():
                while check_validity():
                    if s[start] in window_map:
                        window_map[s[start]] -= 1
                    start += 1
                start -= 1
                if end-start < min_window:
                    min_window = end-start
                    res = s[start:end]
                start += 2
            if end < len(s) and s[end] in freq_map:
                if s[end] not in window_map:
                    window_map[s[end]] = 0
                window_map[s[end]] += 1
            end += 1
        return res