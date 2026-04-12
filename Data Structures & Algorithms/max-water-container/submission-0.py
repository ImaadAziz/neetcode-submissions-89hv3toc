class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            num1 = heights[l]
            num2 = heights[r]
            if num1 < num2:
                area = max(num1*(r-l), area)
                l += 1
            elif num2 < num1:
                area = max(num2 * (r-l), area)
                r -= 1
            else:
                area = max(num1*(r-l), area)
                l += 1

        return area