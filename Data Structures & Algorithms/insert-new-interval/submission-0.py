class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        ns, ne = newInterval

        i = 0

        while i < n and ns > intervals[i][1]:
            res.append(intervals[i])
            i+=1
        
        while i < n and ne >= intervals[i][0]:
            ns = min(ns, intervals[i][0])
            ne = max(ne, intervals[i][1])
            i+=1
        
        res.append([ns, ne])
        while i < n:
            res.append(intervals[i])
            i+=1
        return res
