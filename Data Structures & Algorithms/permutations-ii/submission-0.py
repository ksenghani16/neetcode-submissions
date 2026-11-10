class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        seen=set()
        if len(nums)==0:
            return [[]]
        perm=self.permuteUnique(nums[1::])
        for p in perm:
            for i in range(len(p)+1):
                p_copy=p.copy()
                p_copy.insert(i,nums[0])
                key=tuple(p_copy)
                if key not in seen:
                    seen.add(key)
                    result.append(p_copy)
        return result
        