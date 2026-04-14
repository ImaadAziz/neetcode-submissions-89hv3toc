class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        adj = {}
        for xi, yi in points:
            adj[xi,yi] = []
            for x2, y2 in points:
                adj[xi,yi].append([x2, y2, abs(xi-x2) + abs(yi-y2)])
        
        minH = [(0, points[0])]
        visit = set()
        total = 0
        while minH:
            cost, point = heapq.heappop(minH)
            xi, yi = point[0], point[1]
            if (xi, yi) in visit:
                continue
            visit.add((xi,yi))
            total += cost
            for x2, y2, dist in adj[xi, yi]:
                if (x2, y2) not in visit:
                    heapq.heappush(minH, (dist, [x2, y2]))
            
        return total
        