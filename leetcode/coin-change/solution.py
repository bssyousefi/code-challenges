# First solution (beats 98%) (DP)
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
