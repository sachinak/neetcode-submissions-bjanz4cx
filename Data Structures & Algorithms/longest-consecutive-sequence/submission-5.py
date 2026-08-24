class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCnt = 0
        for n in s:
            if n - 1 not in s:
                l = 1
                while n+ l in s:
                    l+=1
                maxCnt = max(l, maxCnt)
        return maxCnt
            
                
