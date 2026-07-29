class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        n = len(nums)
        dp = [0]*n

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n-1):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        fi = dp[-2]
        dp = [0]*n
        dp[1] = nums[1]
        dp[2] = max(dp[1], nums[2])
        for i in range(3, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        
        li = dp[-1]
        
        return max(fi,li)