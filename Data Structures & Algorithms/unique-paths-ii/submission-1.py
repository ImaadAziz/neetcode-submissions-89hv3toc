class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        prevRow = [0] * cols

        for i in range(rows - 1, -1, -1):
            currRow = [0] * cols
            if i + 1 < rows:
                if obstacleGrid[i+1][-1] == 1:
                    obstacleGrid[i][-1] = 1
            if obstacleGrid[i][-1] != 1:
                currRow[-1] = 1
            else:
                currRow[-1] = 0
            for j in range(cols - 2, -1 , -1):
                if obstacleGrid[i][j] == 1:
                    currRow[j] = 0
                else:
                    currRow[j] = prevRow[j] + currRow[j+1]
            
            prevRow = currRow
        
        return prevRow[0]
        