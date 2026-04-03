class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        res = 0
        l = 0
        for r, char in enumerate(s):
            if char in char_map and char_map[char] >= l:
                l = char_map[char] + 1
            char_map[char] = r
            res = max(res, r - l + 1)
        return res


        