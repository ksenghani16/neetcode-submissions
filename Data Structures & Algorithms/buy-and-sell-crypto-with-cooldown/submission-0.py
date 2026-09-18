class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for _ in range(2)]for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            buy=max(-prices[i]+dp[i+1][0],dp[i+1][1])
            sell=max(prices[i]+dp[i+2][1],dp[i+1][0])

            dp[i][1]=buy
            dp[i][0]=sell
        return dp[0][1]
        