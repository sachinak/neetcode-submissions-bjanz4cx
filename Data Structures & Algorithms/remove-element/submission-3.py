class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r = len(nums)-1
        
        
        while l < r:
            while r >=0 and nums[r] == val:
                r-=1
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
            l+=1
            
        
        return len(nums) - nums.count(val)