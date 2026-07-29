class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            
            lo = 0
            hi = len(dp)
            
            while lo < hi:
                mid = (lo+hi)//2
                if nums[i] > dp[mid]:
                    lo = mid+1
                else:
                    hi = mid
            dp[lo] = nums[i]

       
        return len(dp)