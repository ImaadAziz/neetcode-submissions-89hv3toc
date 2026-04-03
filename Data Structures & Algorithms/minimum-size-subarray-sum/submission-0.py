class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        count = float('inf')
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                count = min(count, r-l+1)
                sum -= nums[l]
                l += 1
            
        if count == float('inf'):
            return 0
        return count