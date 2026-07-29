class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mn = mx = nums[0]
        res = mx
        for i in range(1, n):
            tmn = min(nums[i], nums[i]*mn, nums[i]*mx)
            tmx = max(nums[i], nums[i]*mn, nums[i]*mx)
            mn, mx = tmn, tmx
            res = max(mx, res)
        
        return res
        