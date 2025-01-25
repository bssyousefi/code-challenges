# First solution (beats 5%) (DP)
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[0]*l for _ in range(l)]
        for i in range(l-1,-1,-1):
            for j in range(i,l):
                if i > 0 and s[i:j+1] == s[j:i-1:-1]:
                    dp[i][j] += 1
                elif i == 0 and s[:j+1] == s[j::-1]:
                    dp[i][j] += 1
                if i<j:
                    dp[i][j] += dp[i][j-1]+dp[i+1][j] - dp[i+1][j-1]

        return dp[0][l-1]
# Second solution (beats 5%) (DP, improved palindrome check)
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[0]*l for _ in range(l)]
        m = {}
        for i in range(l-1,-1,-1):
            for j in range(i,l):
                if i == j or (i+1 == j and s[i] == s[j]) or (s[i] == s[j] and (i+1,j-1) in m):
                    m[(i,j)] = True
                    dp[i][j] += 1

                if i<j:
                    dp[i][j] += dp[i][j-1]+dp[i+1][j] - dp[i+1][j-1]
        return dp[0][l-1]
# Third solution (beats 34%) (DP, simpler solution)
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[False]*l for _ in range(l)]
        ret = 0
        for i in range(l-1,-1,-1):
            for j in range(i,l):
                if s[i] == s[j] and (j-i<2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    ret += 1
        return ret
# Fourth solutioin (beats 86%) (two pointers)
class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        ret = 0
        def check(i,j):
            nonlocal ret
            while s[i] == s[j]:
                ret += 1
                if i > 0 and j < l-1:
                    i -= 1
                    j += 1
                else:
                    break
        for i in range(l):
            check(i, i)
            if i < l-1 and s[i] == s[i+1]:
                check(i,i+1)
        return ret
