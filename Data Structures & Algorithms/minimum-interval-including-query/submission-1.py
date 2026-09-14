import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res={}
        heap=[]
        intervals.sort()
        queries_sorted=sorted(queries)
        i=0
        for q in queries_sorted:
            while i <len(intervals) and intervals[i][0]<=q:
                length=intervals[i][1]-intervals[i][0]+1
                heapq.heappush(heap,(length,intervals[i][1]))
                i+=1
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            if heap:
                res[q]=heap[0][0]
            else:
                res[q]=-1
        return [res[q] for q in queries]



        