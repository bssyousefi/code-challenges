# First solution (beats 100%) (memoizec DFS)
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i not in cache:
                cache[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return cache[i]
        return dfs(0)

# Second solution (beats 100%) (DP)
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(n-1,-1,-1):
            dp[i] = max(nums[i]+dp[i+2], dp[i+1])

        return dp[0]
