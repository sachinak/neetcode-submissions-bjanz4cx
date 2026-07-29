"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key=lambda x:x.start)

        pe = intervals[0].end

        for inte in intervals[1:]:
            st,e = inte.start, inte.end
            if st >= pe:
                pe = e
            else:
                return False
        return True
