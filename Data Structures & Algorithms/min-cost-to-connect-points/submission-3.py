class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
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
            for x2, y2 in points:
                if (x2, y2) not in visit:
                    dist = (abs(xi-x2)) + (abs(yi-y2))
                    heapq.heappush(minH, (dist, [x2, y2]))
            
        return total
        