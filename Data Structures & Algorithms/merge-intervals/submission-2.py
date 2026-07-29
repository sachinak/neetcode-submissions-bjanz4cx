class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        


        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for st, e in intervals:
            le = res[-1][1]
            if st <= le:
                res[-1] = [res[-1][0], max(le, e)]
            else:
                res.append([st, e])
        return res
