class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0]*cols for _ in range(rows)]
        
        def dfs(x, y):
            if dp[x][y] != 0:
                return dp[x][y]
            maxLen = 1
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx = x+dx
                ny = y+dy
                
                if 0<=nx<rows and 0<=ny<cols and matrix[x][y] < matrix[nx][ny]:
                    maxLen = max(maxLen, 1 + dfs(nx, ny))
            
            dp[x][y] = maxLen 
            return maxLen
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i,j))
     
        return ans