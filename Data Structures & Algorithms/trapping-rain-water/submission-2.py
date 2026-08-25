class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0]*n
        rmax = [0]*n
        l = 1
        r = n-2
        lmax[0] = -1
        rmax[n-1] = -1
        ll, rr = height[0], height[n-1]
        while l < n:
            
            lmax[l] = max(ll, lmax[l-1])
            rmax[r] = max(rr, rmax[r+1])
            ll = max(ll, height[l])
            rr = max(rr, height[r])
            l+=1
            r-=1
        res = 0
        # print(height)
        # print(lmax)
        # print(rmax)
        for i in range(1,n-1):
            if height[i] <= lmax[i] and height[i] <= rmax[i]:
                res+=min(lmax[i] - height[i], rmax[i] - height[i])
        return res