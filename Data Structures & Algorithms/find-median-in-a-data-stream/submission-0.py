class MedianFinder:

    def __init__(self):
        self.large=[]
        self.small=[]
    def addNum(self, num: int) -> None:
        if self.large and num>self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)
        if len(self.small)>len(self.large)+1:
            value=-heapq.heappop(self.small)
            heapq.heappush(self.large,value)
        if len(self.large)>len(self.small)+1:
            value=heapq.heappop(self.large)
            heapq.heappush(self.small,-value)
    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (-self.small[0]+self.large[0])/2
        if len(self.small)>len(self.large):
            return -self.small[0]
        return self.large[0]
        
        