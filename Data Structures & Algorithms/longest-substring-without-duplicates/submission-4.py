class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = set()
        sol = 0
        while r < len(s):
            c = s[r]
            if c not in res:
                res.add(c)
                sol = max(sol,len(res))
                r += 1
            else:
                sol = max(sol,len(res))
                while c in res:
                    res.remove(s[l])
                    l += 1
                

        return sol
            
            
        