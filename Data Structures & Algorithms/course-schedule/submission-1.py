class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for s, d in prerequisites:
            adj[s].append(d)

        
        visit = set()
        path = set()
        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
    
            visit.add(i)
            path.add(i)
            for d in adj[i]:
                if not dfs(d):
                    path.remove(i)
                    return False
            path.remove(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True