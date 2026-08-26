class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        dp = [[-1]*len(piles) for _ in range(len(piles))]
        def rec(l, r, even):

            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            left = piles[l] if even else 0
            right = piles[r] if even  else 0
            dp[l][r] = max(rec(l+1,r,not even) + left, rec(l,r-1,not even) + right)
            return dp[l][r]
        


        score = rec(0, len(piles) - 1, True)
        if score > sum(piles) - score:
            return True
        return False