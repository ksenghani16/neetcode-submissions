class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandCentre(s,left,right):
            substring=''
            max_length=0
            while left >=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>max_length:
                    max_length=right-left+1
                    substring=s[left:right+1]
                left-=1
                right+=1
            return substring
        
        res=''
        for i in range(len(s)):
            odd=expandCentre(s,i,i)
            even=expandCentre(s,i,i+1)
            if len(odd)>len(res):
                res=odd
            if len(even)>len(res):
                res=even
        return res
                

         

            