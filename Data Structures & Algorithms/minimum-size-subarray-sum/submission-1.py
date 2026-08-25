class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curSum = 0
        minLen = len(nums) + 1
        while  r < len(nums):
            # while r< len(nums) and curSum < target:
            curSum += nums[r]
            r+=1
            
            while l < r and curSum >= target:
                # print(l, r, nums[l], curSum)
                minLen = min(r - l, minLen)
                curSum -= nums[l]
                l+=1
            # print("out", l, r, nums[l], curSum)
            
        return minLen if minLen < len(nums) + 1 else 0
