class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            total = 0
            for j in range(len(matrix[0])):
                total += matrix[i][j]
                self.prefix[i].append(total)
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            prefixRight = self.prefix[i][col2]
            prefixLeft = self.prefix[i][col1 - 1] if col1 - 1 >= 0 else 0
            total += prefixRight - prefixLeft
        return total