import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.ans=[]
        for i in range(len(nums)):
            heapq.heappush(self.ans,nums[i])
        while(len(self.ans)>k):
            heapq.heappop(self.ans)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.ans,val)
        while(len(self.ans)>self.k):
            heapq.heappop(self.ans)
        return self.ans[0]

        
