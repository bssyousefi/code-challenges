# First solution (beats 100%) (Recursive, top down)
class Solution:
    def __init__(self):
        self.cache = {}
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        if s[0] == "0":
            return 0
        if s in self.cache:
            return self.cache[s]
        s1, s2 = 0, 0
        if len(s) > 1:
            if s[0] == "1":
                s2 = self.numDecodings(s[2:])
            elif s[0] == "2" and (s[1] != "9" and s[1] != "8" and s[1] != "7"):
                s2 = self.numDecodings(s[2:])
            else:
                s2 = 0
        s1 = self.numDecodings(s[1:])
        self.cache[s] = s1 + s2
        return s1 + s2
# Second solution (beats 100%) (DP)
class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        dp = [0]*l
        if s[l-1] != "0":
            dp[l-1] = 1

        for i in range(l-2,-1,-1):
            if s[i] != "0":
                dp[i] += dp[i+1]
                if i < l-1:
                    if s[i] == "1" or (s[i]=="2" and s[i+1]!="9" and s[i+1]!="8" and s[i+1]!="7"):
                        dp[i] += dp[i+2] if i+2<l else 1

        return dp[0]
