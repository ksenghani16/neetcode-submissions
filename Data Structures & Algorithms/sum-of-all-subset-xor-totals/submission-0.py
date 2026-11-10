class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def bactrack(i,xor):
            if i==len(nums):
                return xor
            include=bactrack(i+1,xor^nums[i])
            exclude=bactrack(i+1,xor)
            return include +exclude
        return bactrack(0,0)

        