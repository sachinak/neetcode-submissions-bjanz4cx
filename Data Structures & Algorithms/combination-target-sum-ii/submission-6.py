class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []
        candidates.sort()
        def backtrack(idx, curSum):
            if curSum == target:
                res.append(cur.copy())
                return
            
            if idx >= len(candidates) or curSum > target:
                return
            
            elif curSum + candidates[idx] <= target:
                cur.append(candidates[idx])
                backtrack(idx+1, curSum + candidates[idx])
                kidx = idx
                while kidx < len(candidates) and candidates[idx] == candidates[kidx]:
                    kidx+=1
                cur.pop()
                backtrack(kidx, curSum)
        backtrack(0, 0)
        return res