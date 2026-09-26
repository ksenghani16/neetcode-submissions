class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        answer=right
        while left<=right:
            current_sum=0
            sub_array=1
            capacity=(left+right)//2
            for num in nums:
                if current_sum+num>capacity:
                    current_sum=0
                    sub_array+=1
                current_sum+=num
            if sub_array<=k:
                answer=capacity
                right=capacity-1
            else:
                left=capacity+1
        return answer

        