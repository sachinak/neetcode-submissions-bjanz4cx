class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[n] = True

        
        for i in range(n+1, -1, -1):

            for w in wordDict:
                wlen = len(w)
                if i + wlen > n:
                    continue
                
                if  dp[i+wlen] and s[i:i+wlen] == w:
                    dp[i] = True
                    break
        return dp[0]