class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        res = []
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in counts:
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1
                    backtrack()
                    counts[n] += 1
                    perm.pop()

        backtrack()
        return res