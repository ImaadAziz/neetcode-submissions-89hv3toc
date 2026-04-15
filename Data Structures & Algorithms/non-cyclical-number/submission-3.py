class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        if n == 1:
            return True
        while n != 1:
            nums = [i for i in str(n)]
            total = 0
            for i in nums:
                total += int(i) ** 2
            if total in seen:
                return False
            else:
                seen.add(total)
            n = total
        return True