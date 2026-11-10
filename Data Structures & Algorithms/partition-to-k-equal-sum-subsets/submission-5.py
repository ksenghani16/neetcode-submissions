class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        length=sum(nums)//k
        s=[0]*k
        if sum(nums)/k != length:
            return False
        nums.sort(reverse=True)
        if nums[0]>length:
            return False
        
        def backtrack(i):
            if i==len(nums):
                return True
            seen=set()
            for j in range(k):
                if s[j] in seen:
                    continue
                seen.add(s[j])
                if s[j]+nums[i]<=length:
                    s[j]+=nums[i]
                    if backtrack(i+1):
                        return True
                    s[j]-=nums[i]
                    if s[j]==0:
                        break
            return False
        return backtrack(0)
        