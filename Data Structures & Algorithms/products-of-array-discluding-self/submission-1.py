class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        n = len(nums)
        r = n - 2
        lp = [0]*(n)
        rp = [0]*(n)
        lr = nums[0]
        rr = nums[n-1]
        while l < n:
            lp[l] = lr
            lr*=nums[l]
            l+=1
            rp[r] = rr
            rr*=nums[r]
            r-=1
        res = [0]*n
        res[0] = rp[0]
        res[n-1] = lp[n-1]
        for i in range(1,n-1):
            res[i] = lp[i]*rp[i]
        return res