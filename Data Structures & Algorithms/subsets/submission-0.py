class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        total_subset=1<<n
        for num in range(0,total_subset):
            lst=[]
            for i in range(0,n):
                if num & (1<<i) !=0:
                    lst.append(nums[i])
            ans.append(lst)
        return ans
        