"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res=[]
        count=0
        intervals.sort(key=lambda x:x.start)
      
        for interval in intervals:
            if res and res[0] <=interval.start:
                heapq.heappop(res)
                heapq.heappush(res,interval.end)
            else:
                heapq.heappush(res,interval.end)
        return len(res)

            
        