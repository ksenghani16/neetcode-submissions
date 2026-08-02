class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        max_length=0
        for i in range(len(s)):
            char_set =set()
            for j in range(i,len(s)):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
            max_length=max(max_length,len(char_set))
        return max_length
        