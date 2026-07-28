class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        

        def rec(idx, subsets):
            if idx >= len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[idx])
            rec(idx+1, subsets)
            kidx = idx
            subsets.pop()
            while kidx < len(nums) and nums[idx] == nums[kidx]: kidx+=1
            
            rec(kidx, subsets)
        
        rec(0, [])
        return res