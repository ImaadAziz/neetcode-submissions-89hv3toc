class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = defaultdict(list)
        res = []
        for s in strs:
            temp = "".join(sorted(s))
            dt[temp].append(s)

        return list(dt.values())