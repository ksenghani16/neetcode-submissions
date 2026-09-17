class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandCentre(s,left,right):
            count=0
            while left >=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            return count
        
        res=0
        for i in range(len(s)):
            odd=expandCentre(s,i,i)
            even=expandCentre(s,i,i+1)
            if odd:
                res+=odd
            if even:
                res+=even
        return res
                

         

            