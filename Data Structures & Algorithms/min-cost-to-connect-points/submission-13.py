class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        minH = [(0, 0)]
        visit = set()
        total = 0
        while minH:
            if visit == len(points):
                return total
            cost, pointIndex = heapq.heappop(minH)
            point = points[pointIndex]
            xi, yi = point[0], point[1]
            if pointIndex in visit:
                continue
            visit.add(pointIndex)
            total += cost
            for i in range(len(points)):
                if i not in visit:
                    x2, y2 = points[i]
                    dist = (abs(xi-x2)) + (abs(yi-y2))
                    heapq.heappush(minH, (dist, i))
            
        return total
        