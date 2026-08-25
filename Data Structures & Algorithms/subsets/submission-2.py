class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subsets = []

        def rec(idx):
            if idx >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[idx])
            rec(idx+1)
            subsets.pop()
            rec(idx+1)
        
        rec(0)
        return res