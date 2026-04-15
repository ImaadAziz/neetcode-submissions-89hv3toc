class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = 0
        result = ""
        l, r = 0, 0
        while l < len(s):
            r = l
            while r < len(s):
                temp = s[l:r+1]
                if temp == temp[::-1]:
                    if len(temp) > res:
                        res = len(temp)
                        result = temp
                r += 1
            l += 1
        return result