class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def helper(grid,r,c,visit):
            if (min(r,c)< 0 or r==rows or c ==columns or (r,c) in visit or grid[r][c]==1):
                return 0
            if r==rows-1 and c==columns-1:
                return 1
            visit.add((r,c))

            count = 0
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                count+=helper(grid,r+dr,c+dc,visit)

            visit.remove((r,c))
            return count

        return helper(grid,0,0,set())
        