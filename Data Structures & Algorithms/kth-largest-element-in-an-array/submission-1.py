import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in range(len(nums)):
            heapq.heappush(ans,nums[i])
        while(len(ans)>k):
            heapq.heappop(ans)
        return ans[0]