class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def recur(idx, cur):
            if idx == len(nums):
                if cur == target:
                    return 1
                else: return 0
            if dp.get((idx, cur)):
                return dp[(idx, cur)]
            
            dp[(idx, cur)] = recur(idx+1, cur + nums[idx]) + recur(idx+1, cur - nums[idx])
            return dp[(idx, cur)]

        
        ans = recur(0, 0)
        return ans