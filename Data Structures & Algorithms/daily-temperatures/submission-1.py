class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            if len(stack) != 0:
                while stack and t > temperatures[stack[-1]]:
                    index = stack.pop()
                    res[index] = i - index
            stack.append(i)

        return res

            