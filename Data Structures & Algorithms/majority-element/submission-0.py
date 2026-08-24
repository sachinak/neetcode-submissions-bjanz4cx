class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        mc = 0
        ans = -1
        for n in nums:
            d[n]+=1
            if mc < d[n]:
                ans = n
                mc = d[n]
        return ans