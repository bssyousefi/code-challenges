# First solution (beats 100%) (DFS, memoized)
class Solution:
    def __init__(self):
        self.cache = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        def dfs(j):
            if j == l:
                self.cache[j] = True
                return True
            if j in self.cache:
                return self.cache[j]
            for i in range(j,l):
                if s[j:i+1] in wordDict:
                    if dfs(i+1):
                        self.cache[j] = True
                        return True
            self.cache[j] = False
            return False

        return dfs(0)
# Second solution (beats 100%) (DP)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l+1)
        dp[-1] = True
        for i in range(l-1,-1,-1):
            if s[i:] in wordDict:
                dp[i] = True
                continue
            for j in range(i,l):
                if dp[j]:
                    if s[i:j] in wordDict:
                        dp[i] = True
                        break
        return dp[0]
