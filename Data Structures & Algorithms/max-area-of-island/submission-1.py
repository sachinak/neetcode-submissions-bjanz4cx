class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        maxArea = 0
        def dfs(i, j, num):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 
            

            grid[i][j] = 0
            num[0] += 1
            dfs(i+1,j, num)
            dfs(i,j-1, num)
            dfs(i-1,j, num)
            dfs(i,j+1, num)
            nonlocal maxArea
            maxArea = max(maxArea, num[0])
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j,[0])
        return maxArea
