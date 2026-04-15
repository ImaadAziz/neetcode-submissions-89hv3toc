class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in nums[i+1:]:
                return [i, nums.index(tar, i+1)]

        return []