class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []
        cur = []
        def backtrack(idx):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if idx >= len(nums):
                return
            
            cur.append(nums[idx])
            backtrack(idx+1)
            cur.pop()
            backtrack(idx+1)
        backtrack(0)
        return res
