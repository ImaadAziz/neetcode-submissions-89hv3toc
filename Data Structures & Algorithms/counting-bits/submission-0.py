class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        nums = [i for i in range(n+1)]
        for i in nums:
            c = 0
            while i > 0:
                if i & 1 == 1:
                    c += 1
                i = i // 2
            counts.append(c)
        return counts