class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        n = len(nums) - 1

        while l < r:
            m = l + (r-l)//2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        lo = 0
        hi = len(nums) - 1
        if nums[l] <= target and target <= nums[n]:
            lo = l
        else:
            hi = l - 1
           
        
        while lo <= hi:
            m = (lo+hi)//2

            if nums[m] == target:
                return m
            elif target > nums[m]:
                lo = m + 1 
            else:
                hi = m - 1
        return -1
        