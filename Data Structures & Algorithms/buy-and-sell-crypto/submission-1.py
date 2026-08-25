class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        rmax = [0]*n

        for i in range(n-2, -1,-1):
            rmax[i]=max(rmax[i+1], prices[i+1])
        
        maxP = 0
        print(rmax)
        for i in range(n):
            maxP = max(maxP, -prices[i] + rmax[i])
        return maxP