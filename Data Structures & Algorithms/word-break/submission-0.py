class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[n] = True

        wd = {word:idx for idx, word in enumerate(wordDict)}

        for i in range(n+1, -1, -1):

            for w in wordDict:
                wlen = len(w)
                if i + wlen > n:
                    continue
                # print(w, i, s[i:i+wlen], wd.get(s[i:i+wlen]))
                if s[i:i+wlen] == w:
                    if dp[i+wlen]:
                        dp[i] = True
        # print(dp)
        return dp[0]