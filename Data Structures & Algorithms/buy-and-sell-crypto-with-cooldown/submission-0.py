class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def recur(idx, b):
            if idx >= n:
                return 0
            if (idx, b) in dp:
                return dp[(idx, b)]
            cool = recur(idx+1, b)
            if b==0:
                buy = recur(idx+1, 1) - prices[idx]
                dp[(idx, b)]= max(buy, cool)
            else:
                sell = recur(idx+2, 0) + prices[idx]
                dp[(idx, b)]= max(sell, cool)
            return dp[(idx, b)]

        amt = recur(0,0)
        return amt