class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0 
        r = n-1
        maxArea = -1

        while l < r:
            if min(heights[l], heights[r])*(r-l) > maxArea:
                maxArea = min(heights[l], heights[r])*(r-l)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea
