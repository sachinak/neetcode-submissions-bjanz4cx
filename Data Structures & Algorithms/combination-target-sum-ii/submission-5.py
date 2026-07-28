class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subsets = []
        candidates.sort()
        def rec(idx, current_sum):
            if current_sum == target:
                res.append(subsets.copy())
                return
            elif current_sum > target or idx >= len(candidates):
                return
            elif current_sum + candidates[idx] <= target:
                subsets.append(candidates[idx])
                rec(idx+1, current_sum+candidates[idx])
                kidx = idx
                while kidx < len(candidates) and candidates[idx] == candidates[kidx]: kidx+=1
                subsets.pop()
                rec(kidx, current_sum)
        
        rec(0, 0)
        return res