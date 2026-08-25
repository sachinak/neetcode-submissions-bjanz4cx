class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        mini = prices[0]

        for p in prices:
            maxP = max(maxP, p - mini)
            mini = min(mini, p)
        return maxP