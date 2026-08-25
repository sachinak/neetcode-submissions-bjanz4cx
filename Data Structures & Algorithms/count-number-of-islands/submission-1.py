class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # visited = [[False]*cols for _ in range(rows)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1':
                return
            
            grid[i][j] = '-1'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i, j+1)
            dfs(i,j-1)

        

        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    cnt+=1
                    dfs(i, j)
        return cnt