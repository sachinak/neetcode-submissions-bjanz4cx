"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)

        for i in intervals:
            mp[i.start]+=1
            mp[i.end]-=1
        
        gc=c=0
        for k in sorted(mp.keys()):
            c+=mp[k]
            gc = max(c, gc)
        return gc