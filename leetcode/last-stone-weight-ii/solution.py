# First solution (beats 30%) (DP top down)
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        n = len(stones)
        _sum = sum(stones)
        half = (_sum+1) // 2
        cache = {}
        def dfs(i, total):
            if (i, total) not in cache:
                if total > half or i == n-1:
                    cache[(i, total)] = abs(total - (_sum - total))
                else:
                    cache[(i, total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))

            return cache[(i,total)]

        return dfs(0,0)

# Second solution (beats 90%) (DP bottom up)
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        n = len(stones)
        _sum = sum(stones)
        half = (_sum+1) // 2
        dp = [set() for _ in range(n)]
        dp[0] = {stones[0]}
        for i in range(1,n):
            tmp = set(dp[i-1])
            for j in dp[i-1]:
                if j < half:
                    tmp.add(j+stones[i])
            dp[i] = tmp
        return min({abs(i-(_sum-i)) for i in dp[n-1]})
