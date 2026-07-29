class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix = []
        for r in matrix:
            temp = []
            total = 0
            for c in r:
                total += c
                temp.append(total)
            prefix.append(temp)
        self.prefix = prefix
        print(prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2+1):
            row = self.prefix[r]
            total += row[col2] - (row[col1 - 1] if col1 > 0 else 0)
        return total 



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)