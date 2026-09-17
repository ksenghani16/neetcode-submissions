class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd=nums[0]
        minProd=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            oldMax=maxProd
            oldMin=minProd
            maxProd=max(x,oldMax*x,oldMin*x)
            minProd=min(x,oldMax*x,oldMin*x)
            res=max(res,maxProd)
        return res
