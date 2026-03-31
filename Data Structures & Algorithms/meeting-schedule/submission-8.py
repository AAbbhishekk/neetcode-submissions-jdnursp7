"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        last_end = 0
        last_start = 0
        default = True
        intervals.sort(key = lambda x: x.start)
        

        for interval in intervals:
            if interval.end >=last_start and interval.start >=last_end:
                last_end = interval.end
                last_start = interval.start
            else:
                default = False
        return default

