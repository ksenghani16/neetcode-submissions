class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        self.solve(0,[],result,nums)
        return result
    def solve(self,index,subset,result,nums):
        result.append(subset.copy())
        if index>len(nums):
            return
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            self.solve(i+1,subset,result,nums)
            subset.pop()

        