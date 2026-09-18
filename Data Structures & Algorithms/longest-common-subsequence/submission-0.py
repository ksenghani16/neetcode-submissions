class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1 for _ in range(m+1)]for _ in range(n+1) ]
        for ind2 in range(0,m+1):
            dp[0][ind2]=0
        for ind1 in range(0,n+1):
            dp[ind1][0]=0
        for ind2 in range(1,m+1):
            for ind1 in range(1,n+1):
                if text1[ind1-1]==text2[ind2-1]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=0+max(dp[ind1][ind2-1],dp[ind1-1][ind2])
        return dp[ind1][ind2]

        