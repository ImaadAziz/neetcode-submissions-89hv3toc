class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = collections.defaultdict(set)
        for c, p in prerequisites:
            adj[c].add(p)

        res = []
        reqMap = {}
        def dfs(i):
            if i not in reqMap:
                reqMap[i] = set()
                for pre in adj[i]:
                    reqMap[i] |= dfs(pre)
            

            reqMap[i].add(i)
            
            return reqMap[i]

        for crs in range(numCourses):
            dfs(crs)

        
        
        for crs, pre in queries:
            res.append(pre in reqMap[crs])
       
        return res

