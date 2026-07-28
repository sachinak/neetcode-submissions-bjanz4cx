class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxarea = -1
        def dfs(r,c, ca):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            top = dfs(r-1,c, ca)
            bot = dfs(r+1,c, ca)
            lef = dfs(r, c-1, ca)
            ri = dfs(r, c+1, ca)
            cca = 1+top+bot+lef+ri
            return cca



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ca = dfs(i,j,0)
                    maxarea = max(maxarea, ca)
        

        return max(maxarea,0)