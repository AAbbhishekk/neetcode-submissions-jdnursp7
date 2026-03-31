class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        def helper(grid,r,c,visit:set):

            if (min(r,c)< 0 or r==rows or c == columns or grid[r][c]==1 or (r,c) in visit):
                return 0
            if r==rows-1 and c ==columns-1:
                return 1
            visit.add((r,c))

            count = 0
            count+=helper(grid,r+1,c,visit)
            count+=helper(grid,r-1,c,visit)
            count+=helper(grid,r,c-1,visit)
            count+=helper(grid,r,c+1,visit)
            visit.remove((r,c))
            return count

        return helper(grid,0,0,set())

        