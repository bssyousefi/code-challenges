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
