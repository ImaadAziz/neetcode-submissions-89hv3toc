class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr, res = [], []
        self.helper(1, n, k, curr, res)
        return res

    def helper(self, i, n, k, curr, res):
        if len(curr) == k:
            res.append(curr.copy())
            return
        if i > n:
            return
        
        for j in range(i, n + 1):
            curr.append(j)
            self.helper(j + 1, n, k, curr, res)
            curr.pop()