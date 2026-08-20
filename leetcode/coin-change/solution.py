# First solution (beats 98%) (DP + BFS)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [0] * (amount+1)
        q = [0]

        while q:
            j = q.pop(0)
            for c in coins:
                if j+c <= amount and dp[j+c] == 0:
                    dp[j+c] = dp[j] + 1
                    q.append(j+c)
        return 0 if amount == 0 else dp[amount] if dp[amount] > 0 else -1

# Second solution (beats 73%) (DP)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        dp = [-1]*(amount+1)
        dp[0] = 0
        for coin in coins:
            i = 0
            while i <= amount:
                if dp[i] >= 0 and (i+coin) <= amount:
                    dp[i+coin] = dp[i] + 1 if dp[i+coin] < 0 else min(dp[i]+1, dp[i+coin])
                i += 1
        return dp[amount]
