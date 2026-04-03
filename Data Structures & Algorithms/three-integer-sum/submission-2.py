class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r = 0, len(nums) - 1
        res = []
        nums.sort()
        for i in range(len(nums)):
            threeSum = 0
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum += nums[i]
                threeSum += nums[l]
                threeSum += nums[r]
                if threeSum == 0:
                    temp = [nums[i],nums[l],nums[r]]
                    if temp not in res:
                        res.append(temp)
                    l += 1
                    r -= 1

                elif threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                threeSum = 0
                

        return res

            

                