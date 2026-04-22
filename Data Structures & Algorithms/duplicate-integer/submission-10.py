class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ct = Counter(nums)
        return max(ct.values(), default=0) > 1