class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
       
        nums.sort()
        c = Counter(nums)
        perm = []
        res = []
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for num in c:
                if c[num]>0:
                    perm.append(num)
                    c[num] -= 1
                    dfs()
                    c[num] += 1
                    perm.pop()
        dfs()
        return res
                
            