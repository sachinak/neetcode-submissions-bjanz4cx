class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subsets = []

        def rec(idx):
            if idx >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[idx])
            rec(idx+1)
            kidx = idx
            while kidx < len(nums) and nums[idx] == nums[kidx]: kidx+=1
            subsets.pop()
            rec(kidx)
        
        rec(0)
        return res