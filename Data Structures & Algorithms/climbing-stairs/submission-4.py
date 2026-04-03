class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(k: int) -> int:
            if k <= 1:
                return 1
            if k == 2:
                return 2
            return dfs(k - 1) + dfs(k - 2)

        return dfs(n)