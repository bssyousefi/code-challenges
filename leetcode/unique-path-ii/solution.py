# First solution (beats 100%) (DP bottom-up)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        q = [(0,0)]
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                if obstacleGrid[i][j] == 0:
                    val = 0
                    if i-1 >= 0:
                        val += dp[i-1][j]
                    if j-1 >= 0:
                        val += dp[i][j-1]
                    dp[i][j] = val
        return dp[m-1][n-1]

