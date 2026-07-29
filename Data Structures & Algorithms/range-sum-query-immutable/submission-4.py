class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)
        print(prefix)
        self.prefix = prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - (self.prefix[left-1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)