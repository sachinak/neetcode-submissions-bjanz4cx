class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mini = nums[0]
        while l <=r:
            
            if nums[l] < nums[r]:
                mini = min(nums[l], mini)
                break
            m= (l+r)//2
            mini = min(nums[m], mini)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            
        return mini