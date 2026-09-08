class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=0
        res=0
        n=len(nums)+1
        for i in range(0,n):
            sum+=i
        for j in range(0,len(nums)):
            res+=nums[j]
        return (sum-res)
        