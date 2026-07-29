class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        res = 0
        ne = intervals[0][1]
        for st, e in intervals[1:]:
            # ne = res[-1][1]
            
            if st >= ne:
                ne = e
            else:
                # res[-1] = [res[-1][0], min(e, res[-1][1])]
                ne = min(e, ne)
                res+=1
           
        
        return res