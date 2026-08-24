class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        r = n - 1
        
        
        
        while l < r:
            while l < n and nums[l] == 0:
                l+=1
            while r >=0 and nums[r] == 2:
                r-=1
            if l >= n or r < 0 or l > r:
                break
            
            if nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
            l+=1
        l = 0
        
        while l < r:
            while l < n and nums[l] == 0:
                l+=1
            if l >= n or l > r:
                break
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
            r-=1
            