class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        s = set()
        le = len(nums)//3
        for n in nums:
            d[n] +=1 
            if d[n] > le:
                s.add(n)
        return list(s)