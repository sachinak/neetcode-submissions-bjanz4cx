class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subsets = []

        def rec(idx, current_sum):
            if current_sum == target:
                res.append(subsets.copy())
                return
            elif current_sum > target or idx >= len(nums):
                return
            
            subsets.append(nums[idx])
            rec(idx, current_sum + nums[idx])
            subsets.pop()
            rec(idx+1, current_sum)
        
        rec(0, 0)
        return res