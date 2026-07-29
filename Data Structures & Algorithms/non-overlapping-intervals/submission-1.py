class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]
        print(intervals)
        for st, e in intervals:
            ne = res[-1][1]
            print(st, e, ne, res)
            if st < ne:
                res[-1] = [res[-1][0], min(e, res[-1][1])]
                print(res)
            else:
                res.append([st, e])
        print(res)
        return len(intervals) - len(res)