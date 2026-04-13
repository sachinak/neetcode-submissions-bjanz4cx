class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        l = 0
        r = n

        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return -1