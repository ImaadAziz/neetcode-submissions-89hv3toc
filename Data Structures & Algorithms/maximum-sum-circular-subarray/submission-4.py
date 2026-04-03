class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        loop = False
        maxSum = nums[0]
        minSum = nums[0]
        totalSum = 0
     

        currSum = 0
        currMinSum = 0
        for n in nums:
            currMinSum = min(currMinSum, 0)
            currSum = max(currSum, 0)
            currMinSum += n
            currSum += n
            totalSum += n

            if currMinSum < minSum:
                minSum = currMinSum
            if currSum > maxSum:
                maxSum = currSum
            
            
        if totalSum - minSum == 0:
            return maxSum

        return max(maxSum, totalSum - minSum)
        