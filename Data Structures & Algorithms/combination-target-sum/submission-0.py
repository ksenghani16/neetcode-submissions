class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        self.solve(0,[],nums,target,0,result)
        return result
    def solve(self,index,subset,nums,target,total,result):
        if total==target:
            result.append(subset.copy())
            return
        if total>target:
            return
        if index>=len(nums):
            return
        Sum=total+nums[index]
        subset.append(nums[index])
        self.solve(index,subset,nums,target,Sum,result)
        Sum=total
        subset.pop()
        self.solve(index+1,subset,nums,target,Sum,result)


        