class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(idx, curSum):
            if curSum == target:
                res.append(cur.copy())
                return
            if idx >= len(nums) or curSum > target:
                return
            
            cur.append(nums[idx])
            backtrack(idx, curSum+nums[idx])
            cur.pop()
            backtrack(idx+1, curSum)


        backtrack(0, 0)
        return res