class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = defaultdict(list)
        res = []
        for s in strs:
            temp = "".join(sorted(s))
            if temp in dt:
                dt[temp].append(s)
            else:
                dt[temp].append(s)

        return list(dt.values())