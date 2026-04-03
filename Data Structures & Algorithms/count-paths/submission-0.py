class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevrow = [0] * n

        for i in range(m - 1, -1, -1):
            currRow = [0] * n
            currRow[-1] = 1
            for j in range(n - 2, -1, -1):
                currRow[j] = prevrow[j] + currRow[j + 1]
            prevrow = currRow
        
        return prevrow[0]
        