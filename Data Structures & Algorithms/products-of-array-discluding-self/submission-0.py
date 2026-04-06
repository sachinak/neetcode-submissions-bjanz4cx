class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ls = [1]*n
        rs = [1]*n
        l = r = 1
        for i, v in enumerate(nums):
            if i == 0:
                ls[i] = l
            else:
                ls[i] = l*nums[i-1]
                l=ls[i]
        for i in range(n-1,-1,-1):
            if i == n-1:
                rs[i] = r
            else:
                rs[i] = r*nums[i+1]
                r=rs[i]
        ans = [0]*n
        for i in range(n):
            ans[i] = ls[i]*rs[i]
        return ans