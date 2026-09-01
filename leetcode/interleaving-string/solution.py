# First solution (beats 42%) Top-down DP with memoization
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        cache = {}
        if m + n != l:
            return False

        def dfs(i,j,k):
            if (i,j,k) in cache:
                return cache[(i,j,k)]
            if i < m:
                if s1[i] == s3[k]:
                    if dfs(i+1,j,k+1):
                        cache[(i,j,k)] = True
                        return True

            if j < n and s2[j] == s3[k] and dfs(i,j+1,k+1):
                cache[(i,j,k)] = True
                return True

            cache[(i,j,k)] = i==m and j==n and k==l
            return cache[(i,j,k)]

        return dfs(0,0,0)

