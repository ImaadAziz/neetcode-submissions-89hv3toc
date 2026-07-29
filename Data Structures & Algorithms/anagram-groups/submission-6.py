class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for n in strs:
            ct = [0] * 26
            for c in n:
                ct[ord(c) - ord('a')] += 1
            res[tuple(ct)].append(n)
        return list(res.values())