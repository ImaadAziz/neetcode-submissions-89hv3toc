class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, current, total):
            if total == target:
                res.append(current.copy())  # Make a copy
                return
            if i >= len(nums) or total > target:
                return
            
            # Option 1: Include nums[i] (can use it again)
            current.append(nums[i])
            backtrack(i, current, total + nums[i])
            current.pop()
            
            # Option 2: Skip nums[i] (move to next number)
            backtrack(i + 1, current, total)
        
        backtrack(0, [], 0)
        return res
        
        
        