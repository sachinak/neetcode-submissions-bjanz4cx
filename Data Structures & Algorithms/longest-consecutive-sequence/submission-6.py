class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        cnt = 0

        for x in nums:
            if x - 1 not in hs:
                l = 1
                while x + l in hs:
                    l+=1
                cnt = max(l, cnt)
        return cnt