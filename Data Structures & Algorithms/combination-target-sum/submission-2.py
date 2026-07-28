class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # move on without using the number
        # use it and stay

        res = []
        cur = []
        def backtrack(i, curSum):
            if curSum == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or curSum > target:
                return
            
            # use it and stay
            cur.append(nums[i])
            backtrack(i, curSum + nums[i])

            # move on without using the number
            cur.pop()
            backtrack(i+1, curSum)
        
        backtrack(0, 0)
        return res

