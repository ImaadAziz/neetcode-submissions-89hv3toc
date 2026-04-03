class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1
        while L <= R:
            mid = int((L+R)/2)
            arrMid = matrix[mid]
            L1, R1 = 0, len(arrMid) - 1
            mid2 = 0
            while L1 <= R1:
                mid2 = int((L1 + R1) / 2)
                if arrMid[mid2] < target:
                    L1 = mid2 + 1
                elif arrMid[mid2] > target:
                    R1 = mid2 - 1
                elif arrMid[mid2] == target:
                    return True
            if arrMid[mid2] < target:
                L = mid + 1
            elif arrMid[mid2] > target:
                R = mid - 1
        return False
            
        