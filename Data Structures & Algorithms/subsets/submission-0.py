class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        idx = 0
        if nums:
            self.backTrack(res, current, nums, idx)
        return res

    def backTrack(self, res, current, nums, idx):
        if current not in res:
            res.append(current.copy())
        if idx >= len(nums):
            return
        self.backTrack(res, current.copy(), nums, idx+1)
        current.append(nums[idx])
        self.backTrack(res, current.copy(), nums, idx+1)
        current.pop()
        

        