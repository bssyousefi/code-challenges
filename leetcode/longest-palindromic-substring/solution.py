# First solution (beats 57%) (two pointers)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        max_ = 1
        ret = s[0]

        def check(i, j):
            nonlocal max_, ret
            while i > 0 and j < len(s)-1 and s[i-1] == s[j+1]:
                i -= 1
                j += 1
            if j-i+1 > max_:
                max_ = j-i+1
                ret = s[i:j+1]

        for i in range(len(s)):
            if i < len(s)-1 and s[i] == s[i+1]:
                check(i,i+1)
            if i > 0 and i < len(s)-1 and s[i-1]==s[i+1]:
                check(i-1, i+1)

        return ret
# Second solution (beats 39%) (DP)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        l = len(s)
        max_ = 0
        ret = ""
        dp = [[False]*l for _ in range(l)]
        for i in range(l-1,-1,-1):
            for j in range(i,l):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > max_:
                        max_ = j-i+1
                        ret = s[i:j+1]
        return ret
