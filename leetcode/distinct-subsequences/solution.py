# First solution (beats 17%) (DP Top down + memoization)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        cache = {}
        def dfs(i,j):
            if j == n:
                return 1
            if (i,j) in cache:
                return cache[(i,j)]
            ret = 0
            if i < m:
                if s[i] == t[j]:
                    ret = dfs(i+1, j+1)
                ret += dfs(i+1, j)
                cache[(i,j)] = ret
                return ret

            cache[(i,j)] = 0
            return 0
        return dfs(0,0)

# Second solution (beats 83%) (DP Bottom up)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,max(-1,n-m+i-1),-1):
                val = 0
                if s[i] == t[j]:
                    val = dp[i+1][j+1]
                val += dp[i+1][j]
                dp[i][j] = val
        return dp[0][0]

