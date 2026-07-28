class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def recur(idx):
            if idx >= len(nums):
                res.append(subsets[:])
                return
            
            subsets.append(nums[idx])
            recur(idx+1)
            subsets.pop()
            recur(idx+1)
        
        recur(0)
        return res