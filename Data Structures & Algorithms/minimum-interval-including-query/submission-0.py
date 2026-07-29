class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        res = [-1]*n
        intervals.sort(key=lambda x:x[0])
        for idx,q in enumerate(queries):
            for s,e in intervals:
                if s<=q<=e:
                    if res[idx] == -1:res[idx] = e-s+1
                    else:
                        res[idx] = min(res[idx], e-s+1)
        return res