class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        v = [[c[k], k] for k in c]
        v.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(v[i][1])
        return res