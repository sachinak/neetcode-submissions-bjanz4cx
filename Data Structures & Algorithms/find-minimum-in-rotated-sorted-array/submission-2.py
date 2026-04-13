class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        mini = nums[0]
        while l <=r:
            m= (l+r)//2
            
            if nums[l] < nums[r]:
                mini = min(nums[l], mini)
                break
            if nums[m] >= nums[l]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m - 1
            
            if mini == -1:
                mini = nums[m]
            else:
                if mini > nums[m]:
                    mini = nums[m]
        return mini