class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def paths(i,j):
            if i ==0 or j ==0:
                return 1
            if i<0 or j<0 or i==m or j==n:
                return 0
            return paths(i-1,j) + paths(i,j-1)

        return paths(m-1,n-1)
        