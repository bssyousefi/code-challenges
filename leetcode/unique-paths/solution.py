# First solution (beats 100%) (Math)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = m + n - 2
        if m > n:
            m, n = n, m
        res = 1
        for i in range(n,t+1):
            res = res * i // (i-n+1)
        return res

# Second solution (beats 100%) (DP)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0] = [1] * n
        for i in range (1,m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]
