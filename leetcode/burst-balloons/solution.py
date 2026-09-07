# First solution (beats 25%) (DP Top down + memoization)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            _max = 0
            for k in range(i+1,j):
                coins = nums[i] * nums[k] * nums[j]
                coins += dfs(i,k) + dfs(k,j)
                if coins > _max:
                    _max = coins
            cache[(i,j)] = _max
            return _max

        return dfs(0,n-1)

# Second solution (beats 99%) (DP bottom up)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                _max = 0
                for k in range(i+1,j):
                    coins = nums[i] * nums[k] * nums[j]
                    coins += dp[i][k] + dp[k][j]
                    if coins > _max:
                        _max = coins
                dp[i][j] = _max
        return dp[0][n-1]
