class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = Counter(nums)
        return max(seen.values(), default=0) > 1