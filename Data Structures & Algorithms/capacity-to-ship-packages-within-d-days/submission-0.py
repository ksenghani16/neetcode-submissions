class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        answer =right
        while left<=right:
            current_sum=0
            required_days=1
            capacity=(left+right)//2
            for weight in weights:
                if current_sum + weight>capacity:
                    current_sum=0
                    required_days+=1
                current_sum+=weight
            if required_days<=days:
                answer=capacity
                right=capacity-1
            else:
                left=capacity+1
        return answer
