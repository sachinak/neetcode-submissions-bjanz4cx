class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = list(s)
        nums = sorted(l)

        l = 0
        r = 1
        cnt= 1
        maxCnt = -1
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        while r<n:
            if nums[r] == nums[r-1] + 1:
                cnt+=1
                r+=1
            else:
                cnt=1
                l=r
                r=l+1
            maxCnt = max(maxCnt, cnt)
        print(nums)
        return maxCnt