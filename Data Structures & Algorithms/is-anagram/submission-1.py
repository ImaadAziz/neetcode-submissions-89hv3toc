class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for n in s:
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1
        
        for n in t:
            if n not in seen:
                return False
            else:
                seen[n] -= 1
                if seen[n] == 0:
                    seen.pop(n)

        if seen == {}:
            return True
        else:
            return False