"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_list = []
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            current_start,current_end = interval.start,interval.end
            intervals_list.extend((current_start,current_end))

        return sorted(intervals_list)==intervals_list


