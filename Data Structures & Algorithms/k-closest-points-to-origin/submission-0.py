class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        for x,y in points:
            distance=x*x+y*y
            heapq.heappush(ans,(-distance,x,y))
            if len(ans)>k:
                heapq.heappop(ans)
        return [[x,y] for distance,x,y in ans]
        
        