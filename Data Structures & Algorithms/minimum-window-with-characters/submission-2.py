class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = {}
        for c in t:
            counts[c] = counts.get(c, 0) + 1
        l = 0
        window_counts = {}
        res1, res2 = -1,-1
        formed = 0
        for r in range(len(s)):
            char = s[r]
            # Add char to window logic here...
        
            if char in counts:
                window_counts[char] = window_counts.get(char, 0) + 1
                if window_counts[char] == counts[char]:
                    formed += 1

            while formed == len(counts):
                if res1 == -1 and res2 == -1:
                    res1, res2 = l, r
                elif r - l < res2 - res1:
                    res1, res2, = l, r
                
                if s[l] in window_counts:
                    window_counts[s[l]] = window_counts.get(s[l]) - 1
                    if window_counts[s[l]] < counts[s[l]]:
                        formed -= 1
                l += 1
        return s[res1:res2+1]

        