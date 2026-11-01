class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count={}
        window={}
        min_length=float('inf')
        left=0
        right=0
        res=''
        have=0
        for i in range(len(t)):
            count[t[i]]=count.get(t[i],0)+1
            need=len(count)
        for right in range(len(s)):
            ch=s[right]
            window[ch]=window.get(ch,0)+1
            if ch in count and  count[ch]==window[ch]:
                have+=1
            while need==have:
                if right-left+1<min_length:
                    res=s[left:right+1]
                    min_length=right-left+1
                left_char=s[left]
                window[left_char]-=1
                if left_char in count and window[left_char]<count[left_char]:
                    have-=1
                left+=1
        return res

        
        