class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            tar = target - n
            if tar in nums[i+1:]:
                return [i, nums.index(tar, i + 1)]

        return []