class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for num in range(0,n+1):
            count=0
            for j in range(0,32):
                if num &(1<<j) !=0:
                    count+=1
            ans.append(count)
        return ans
        