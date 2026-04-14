class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = collections.defaultdict(list)
        for c, p in prerequisites:
            preMap[c].append(p)
        
        visit = set()
        res = []
        added = set()
        def dfs(i):
            if i in visit:
                return False
            if preMap[i] == []:
                if i not in added:
                    added.add(i)
                    res.append(i)
                return True
            visit.add(i)
            for c in preMap[i]:
                if not dfs(c):
                    return False
            visit.remove(i)
            preMap[i] = []
            res.append(i)
            added.add(i)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return list(res)
            