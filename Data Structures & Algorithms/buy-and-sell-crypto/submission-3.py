class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                prof = max(prof, prices[r]-prices[l])
            else:
                l = r
        return prof