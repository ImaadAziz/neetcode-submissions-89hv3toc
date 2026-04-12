class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0,1],[1,0],[0,-1],[-1, 0]]
        while minH:
            h, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return h
            for dr, dc in directions:
                rowD, colD = r + dr, c + dc
                if rowD == N or rowD < 0 or colD == N or colD < 0 or (rowD, colD) in visit:
                    continue
                visit.add((rowD,colD))
                heapq.heappush(minH, [max(h, grid[rowD][colD]), rowD, colD])

        
