class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = []
        dp.append(0)
        res = 0
        for i in range(len(nums)):
            nextDP = []
            for t in dp:
                add = t + nums[i]
                if add == target and i == len(nums) - 1:
                    res += 1
                nextDP.append(add)
                sub = t - nums[i]
                if sub == target and i == len(nums) - 1:
                    res += 1
                nextDP.append(sub)
            dp = nextDP
        
        return res