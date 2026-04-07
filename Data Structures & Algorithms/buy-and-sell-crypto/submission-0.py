class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = max(prices)
        maxProfit = 0

        for p in prices:
            if p < minPrice:
                minPrice = p
            if maxProfit < p - minPrice:
                maxProfit = p - minPrice
        return maxProfit