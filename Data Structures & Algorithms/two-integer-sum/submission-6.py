class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i,n in enumerate(nums):
            d[n].append(i)
        
        for n in nums:
            if d.get(target-n):
                if n==target-n:
                    if len(d[n]) > 1:
                        return d[n][:2]
                    else:
                        continue
                return [d[n][0],d[target-n][0]]