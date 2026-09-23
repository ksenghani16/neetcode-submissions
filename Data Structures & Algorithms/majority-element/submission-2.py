class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k=len(nums)//2
        count={}
        
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
            if count[nums[i]]>k:
                res=nums[i]
        return res

        
        