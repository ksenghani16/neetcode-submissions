class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        for num,freq in cnt.items():
            if freq==1:
                return num
        