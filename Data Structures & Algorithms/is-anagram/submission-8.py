class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ct1 = Counter(s)
        ct2 = Counter(t)
        return ct1 == ct2