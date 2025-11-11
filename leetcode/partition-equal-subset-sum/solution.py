# First solution (beats 8%) (DFS - memoized)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        s = sum(nums)
        if s%2==1:
            return False
        s = s / 2
        cache = {}
        def dfs(i, s):
            if s <= 0:
                return s == 0
            if i >= l:
                return False
            if (i,s) in cache:
                return cache[(i,s)]
            cache[(i,s)] = dfs(i+1, s) or dfs(i+1, s-nums[i])
            return cache[(i,s)]
        return dfs(0,s)
# Second solution (beats 35%) (DFS -memoized) (used list instead of dict)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        s = sum(nums)
        if s%2==1:
            return False
        s = s // 2
        cache = [[None]*(s+1) for _ in range(l)]
        def dfs(i, s):
            if s <= 0:
                return s == 0
            if i >= l:
                return False
            if cache[i][s] is not None:
                return cache[i][s]
            cache[i][s] = dfs(i+1, s) or dfs(i+1, s-nums[i])
            return cache[i][s]
        return dfs(0,s)
# Third solution (beats 43%) (DP)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        s = sum(nums)
        if s%2==1:
            return False
        s = s // 2
        dp = [[None]*(s+1) for _ in range(l)]
        for i in range(l-1,-1,-1):
            if nums[i] > s:
                return False
            dp[i][nums[i]] = True
            if i == l-1:
                continue
            for j in range(s+1):
                if dp[i+1][j]:
                    dp[i][j] = True
                    if j+nums[i] <= s:
                        dp[i][j+nums[i]] = True
        return dp[0][-1] if dp[0][-1] is not None else False
# Fourth solution (beats 58%) (DP) (used set)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        s = sum(nums)
        if s%2==1:
            return False
        s = s // 2
        dp = set()
        for i in range(l):
            new_set = set()
            for j in dp:
                if nums[i]+j <= s:
                    new_set.add(nums[i]+j)
            dp.update(new_set)
            dp.add(nums[i])
        return s in dp
# Fifth solution (beats 91%) (DP) (used set + return ASAP)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        s = sum(nums)
        if s%2==1:
            return False
        s = s // 2
        dp = set()
        for i in range(l):
            new_set = set()
            for j in dp:
                if nums[i]+j < s:
                    new_set.add(nums[i]+j)
                elif nums[i]+j == s:
                    return True
            dp.update(new_set)
            dp.add(nums[i])
        return s in dp
# Sixth solution (beats 98%)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        nums.sort()
        ret = {0}
        def _build(new):
            ret.update({new+i for i in ret})
        for n in nums:
            _build(n)
            if (s//2) in ret:
                return True
        return False
