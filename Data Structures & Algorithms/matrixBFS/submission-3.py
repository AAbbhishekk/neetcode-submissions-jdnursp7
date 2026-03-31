class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 0

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r==rows-1 and c ==columns-1:
                    return length
                neighbours = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in neighbours:
                    if (min(r+dr,c+dc)<0 or r+dr==rows or c+dc==columns or (r+dr,c+dc) in visit or grid[r+dr][c+dc]==1):
                        continue
                    queue.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            length+=1

        return -1
        