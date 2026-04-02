class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq_map, window_map = {},{}
        start = 0
        min_window, res = float('inf'), [-1,-1]
        for c in t:
            freq_map[c] = 1 + freq_map.get(c,0)
        have, need = 0, len(freq_map)
        for end in range(len(s)):
            window_map[s[end]] = 1+window_map.get(s[end],0)
            if s[end] in freq_map and window_map[s[end]] == freq_map[s[end]]:
                have += 1

            while have == need:
                if end-start+1 < min_window:
                    min_window = end-start+1
                    res = [start, end]
                window_map[s[start]] -= 1
                if s[start] in freq_map and window_map[s[start]] < freq_map[s[start]]:
                    have -= 1
                start += 1
        start,end = res    
        return s[start:end+1]