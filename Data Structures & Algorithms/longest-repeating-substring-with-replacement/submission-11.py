class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        left=0
        right=0
        maxi=0
        max_length=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0)+1
            maxi=max(maxi,count[s[right]])
            while ((right-left+1)-maxi)>k:
                count[s[left]]-=1
                left+=1
            max_length=max(max_length,right-left+1)
        return max_length



