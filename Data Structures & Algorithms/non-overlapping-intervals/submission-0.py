class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=[]
        count=0
        for interval in intervals:
            if not res or res[-1][1]<=interval[0]:
                res.append(interval)
            else:
                count+=1
            if res[-1][1]>interval[1]:
                res[-1]=interval
        return count

        