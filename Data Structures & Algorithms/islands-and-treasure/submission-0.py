class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        while q:
            r,c,d = q.pop(0)

            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == -1:
                continue
            if grid[r][c] > 0 and grid[r][c] < 2147483647:
                continue
            if grid[r][c] == 0:
                q.append((r+1,c,1))
                q.append((r,c+1,1))
                q.append((r-1,c,1))
                q.append((r,c-1,1))
            else:
                grid[r][c] = d
                q.append((r+1,c,d+1))
                q.append((r,c+1,d+1))
                q.append((r-1,c,d+1))
                q.append((r,c-1,d+1))
        

