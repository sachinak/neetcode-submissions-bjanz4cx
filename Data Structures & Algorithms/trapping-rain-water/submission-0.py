class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmin = [0]*n
        rmin = [0]*n
        lmax = [0]*n
        rmax = [0]*n
        j = n-1
        for i in range(n):
            if i > 0:
                lmax[i] = max(lmax[i-1], height[i-1])
            if j < n-1:
                rmax[j] = max(rmax[j+1], height[j+1])
            j-=1
        totwater = 0
        for i in range(1,n-1):
            water = min(rmax[i], lmax[i]) - height[i]
            if water > 0:
                totwater+=water
        return totwater
        