class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = []
        for i in c:
            l.append([c[i],i ])
        l.sort(key=lambda x:x[0], reverse=True)
        ans = []
        print(l)
        for i in range(k):
            ans.append(l[i][1])
        return ans