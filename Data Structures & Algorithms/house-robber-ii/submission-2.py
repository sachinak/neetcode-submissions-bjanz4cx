class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        def helper(nums):
            a, b = 0,0
            for num in nums:
                c = max(num + a, b)
                a = b
                b = c
            return b
        
        l1 = helper(nums[1:])
        l2 = helper(nums[:n-1])
        return max(l1, l2)