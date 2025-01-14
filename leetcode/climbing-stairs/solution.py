# First solution (beats 100%) (DP)
class Solution:
    def __init__(self):
        self.cache = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        s2 = self.climbStairs(n-2)
        s1 = self.climbStairs(n-1)

        self.cache[n] = s1 + s2
        return self.cache[n]
