"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        
        st = []
        e = []
        for inte in intervals:
            st.append(inte.start)
            e.append(inte.end)
        st.sort()
        e.sort()
        c = 0
        gc = c
        i = j =0
        while i<n and j<n:
            if st[i] < e[j]:
                c+=1
                gc=max(gc, c)
                i+=1
            else:
                c-=1
                j+=1
        return gc
    
