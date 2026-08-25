class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i,j])
        
        t = 0
        while q:
            
            for _ in range(len(q)):
                x,y = q.popleft()
                if x - 1 >= 0  and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    q.append([x-1,y])
                if x + 1 < rows  and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    q.append([x+1,y])
                if y - 1 >= 0 and grid[x][y - 1] == 1:
                    grid[x][y-1] = 2
                    q.append([x,y-1])
                if y + 1 < cols and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    q.append([x,y+1])
            if len(q) > 0:
                t+=1
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return t