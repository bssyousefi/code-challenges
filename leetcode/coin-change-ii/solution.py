# First solution (Timeout)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        coins.sort()
        n = len(coins)
        def dfs(val, i):
            if (val, i) in cache:
                return cache[(val, i)]
            if val == 0:
                return 1
            count = 0
            for j in range(i,n):
                if coins[j] <= val:
                    count += dfs(val-coins[j], j)
                else:
                    break
            cache[(val,i)] = count
            return count

        return dfs(amount, 0)


# Second solution (beats 61%) (backtracking)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            i = 0
            while i+coin < amount+1:
                if dp[i] > 0:
                    dp[i+coin] += dp[i]
                i += 1
        return dp[-1]
