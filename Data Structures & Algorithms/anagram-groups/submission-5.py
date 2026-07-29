class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            ct = [0] * 26
            for c in s:
                ct[ord(c) - ord('a')] += 1
            ct = tuple(ct)
            res[ct].append(s)

        return list(res.values())