class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        res = []
        for n in nums:
            if n not in s:
                res.append(n)
                s.add(n)
        
        for idx, v in enumerate(res):
            nums[idx] = v
        return len(res)