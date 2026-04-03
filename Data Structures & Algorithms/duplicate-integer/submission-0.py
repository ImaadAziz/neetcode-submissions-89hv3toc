class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            num = nums[i]
            if num in nums[i+1:]:
                return True

        return False
        