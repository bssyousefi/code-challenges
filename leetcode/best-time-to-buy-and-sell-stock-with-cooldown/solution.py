# First solution (beats 61%) (DP)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        for i in range(n-1,-1,-1):
            # buying
            buy = - prices[i]
            if i+1 < n:
                buy += dp[i+1][1]
                buy = max(buy, dp[i+1][0])

            dp[i][0] = buy if buy > 0 else 0

            # sell
            sell = prices[i]
            if i+2 < n:
                sell += dp[i+2][0]

            if i+1 < n:
                sell = max(sell, dp[i+1][1])

            dp[i][1] = sell

        return dp[0][0]

