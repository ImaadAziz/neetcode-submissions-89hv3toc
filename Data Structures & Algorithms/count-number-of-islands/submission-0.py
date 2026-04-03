class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visit:
                    islands +=1
                    self.dfs(grid, i, j, visit, rows, cols)
        return islands
        

    def dfs(self, grid, r, c, visit, rows, cols):
        if min(r, c) < 0 or r == rows or c == cols or (r, c) in visit or grid[r][c] == '0':
            return
        visit.add((r,c))
        grid[r][c] = '0'
        self.dfs(grid, r+1, c, visit, rows, cols)
        self.dfs(grid, r-1, c, visit, rows, cols)
        self.dfs(grid, r, c+1, visit, rows, cols)
        self.dfs(grid, r, c-1, visit, rows, cols)








        