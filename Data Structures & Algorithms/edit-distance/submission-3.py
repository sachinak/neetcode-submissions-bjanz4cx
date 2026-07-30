class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        rows,cols = len(word1),len(word2)
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        for row in range(rows+1):
            dp[row][0] = row
        for col in range(cols+1):
            dp[0][col] = col
            
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[rows][cols]