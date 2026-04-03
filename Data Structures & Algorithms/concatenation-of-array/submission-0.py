class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums.copy()
        for n in nums:
            result.append(n)

        return result
        