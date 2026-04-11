class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or digits == "":
            return []
        nums = {}
        letter = ord('a')
        for i in range(2, 10):
            if i != 7 and i != 9:
                nums[i] = [chr(letter), chr(letter+1), chr(letter+2)]
                letter += 3
            else:
                nums[i] = [chr(letter), chr(letter+1), chr(letter+2), chr(letter+3)]
                letter += 4
        res = []
        curr = ""
        self.helper(0, digits, curr, res, nums)
        return res
        

    def helper(self, i, digits, curr, res, nums):
        if len(curr) == len(digits):
            res.append(curr)
            return
        if i >= len(digits):
            return
        

        for c in nums[int(digits[i])]:
            curr += c
            self.helper(i + 1, digits, curr, res, nums)
            curr = curr[:-1]
        