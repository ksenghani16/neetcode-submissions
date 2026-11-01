class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count={}
        res=[]
        for num in nums:
            count[num]=count.get(num,0)+1
        for num,cnt in count.items():
            heapq.heappush(heap,(-cnt,num))
        while len(res)<k:
            cnt,num=heapq.heappop(heap)
            res.append(num)
        return res
            

        